#!/usr/bin/env python3
"""Export the reviewed PBMC4k lookup used by both project websites.

The classifier was trained on PBMC3k. Its eight shared fine-label
probabilities are combined into six broad display categories for PBMC4k.
Dendritic cells are outside that model scope and are exported as reviewed
annotations without model probabilities.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


DISPLAY_CLASSES = [
    "B cells",
    "Classical monocytes",
    "CD16+ non-classical monocytes",
    "NK cells",
    "Cytotoxic T cells",
    "Non-cytotoxic T cells",
]

REVIEWED_TO_BROAD = {
    "B cells": "B cells",
    "Classical monocytes": "Classical monocytes",
    "CD16+ non-classical monocytes": "CD16+ non-classical monocytes",
    "NK cells": "NK cells",
    "Cytotoxic CD8 T cells": "Cytotoxic T cells",
    "Activated/transitional T cells": "Non-cytotoxic T cells",
    "IL7R+ memory/helper T cells": "Non-cytotoxic T cells",
    "Naive/resting T cells": "Non-cytotoxic T cells",
}

PROBABILITY_COLUMNS = {
    "B cells": ["probability__B cells"],
    "Classical monocytes": ["probability__Classical monocytes"],
    "CD16+ non-classical monocytes": [
        "probability__CD16+ non-classical monocytes"
    ],
    "NK cells": ["probability__NK cells"],
    "Cytotoxic T cells": [
        "probability__Activated/transitional T cells",
        "probability__Cytotoxic CD8 T cells",
    ],
    "Non-cytotoxic T cells": [
        "probability__IL7R+ memory/helper T cells",
        "probability__Naive/resting T cells",
    ],
}


def macro_f1(reviewed: list[str], predicted: list[str]) -> float:
    scores = []
    for label in DISPLAY_CLASSES:
        true_positive = sum(
            truth == label and guess == label
            for truth, guess in zip(reviewed, predicted)
        )
        false_positive = sum(
            truth != label and guess == label
            for truth, guess in zip(reviewed, predicted)
        )
        false_negative = sum(
            truth == label and guess != label
            for truth, guess in zip(reviewed, predicted)
        )
        denominator = 2 * true_positive + false_positive + false_negative
        scores.append(2 * true_positive / denominator if denominator else 0.0)
    return sum(scores) / len(scores)


def main() -> None:
    repository = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--reviewed-cells",
        type=Path,
        default=repository
        / "PBMC4k/results/tables/pbmc4k_phase4_xgboost_cell_predictions.csv",
    )
    parser.add_argument(
        "--shared8-predictions",
        type=Path,
        default=repository
        / "PBMC_integrated/results/tables/pbmc_shared8_pbmc4k_cell_predictions.csv",
    )
    parser.add_argument("--output", type=Path, action="append", required=True)
    args = parser.parse_args()

    with args.shared8_predictions.open(newline="", encoding="utf-8") as handle:
        shared_rows = {
            row["cell_id"]: row for row in csv.DictReader(handle)
        }

    with args.reviewed_cells.open(newline="", encoding="utf-8") as handle:
        reviewed_rows = list(csv.DictReader(handle))

    cells = []
    evaluated_reviewed: list[str] = []
    evaluated_predicted: list[str] = []
    dendritic_count = 0

    for number, row in enumerate(reviewed_rows, start=1):
        cell_id = row["cell_id"]
        barcode = cell_id.removeprefix("pbmc4k_")
        fine_reviewed = row["reviewed_cell_type"]

        if fine_reviewed == "Dendritic cells":
            dendritic_count += 1
            cells.append(
                {
                    "number": number,
                    "barcode": barcode,
                    "cell_id": cell_id,
                    "split": "external",
                    "reviewed": "Dendritic cells",
                    "original_reviewed": fine_reviewed,
                    "predicted": "Dendritic cells",
                    "confidence": None,
                    "probabilities": [],
                    "annotation_only": True,
                }
            )
            continue

        prediction_row = shared_rows.pop(cell_id)
        probabilities = [
            sum(float(prediction_row[column]) for column in PROBABILITY_COLUMNS[label])
            for label in DISPLAY_CLASSES
        ]
        total = sum(probabilities)
        if abs(total - 1.0) > 1e-5:
            raise ValueError(f"Probabilities for {cell_id} sum to {total}")

        predicted = DISPLAY_CLASSES[max(range(len(probabilities)), key=probabilities.__getitem__)]
        reviewed = REVIEWED_TO_BROAD[fine_reviewed]
        evaluated_reviewed.append(reviewed)
        evaluated_predicted.append(predicted)
        cells.append(
            {
                "number": number,
                "barcode": barcode,
                "cell_id": cell_id,
                "split": "external",
                "reviewed": reviewed,
                "original_reviewed": fine_reviewed,
                "predicted": predicted,
                "confidence": round(max(probabilities), 8),
                "probabilities": [round(value, 8) for value in probabilities],
                "annotation_only": False,
            }
        )

    if shared_rows:
        raise ValueError(f"{len(shared_rows)} shared-model rows were not exported")
    if len(cells) != 4131 or dendritic_count != 34:
        raise ValueError(
            f"Expected 4,131 cells and 34 dendritic cells; got "
            f"{len(cells)} and {dendritic_count}"
        )

    correct = sum(
        truth == guess
        for truth, guess in zip(evaluated_reviewed, evaluated_predicted)
    )
    accuracy = correct / len(evaluated_reviewed)
    f1 = macro_f1(evaluated_reviewed, evaluated_predicted)

    payload = {
        "dataset": "PBMC4k",
        "model": "PBMC3k-trained shared-eight XGBoost, displayed as six broad classes",
        "classes": DISPLAY_CLASSES,
        "cell_count": len(cells),
        "evaluated_cell_count": len(evaluated_reviewed),
        "reviewed_exception_count": dendritic_count,
        "external_accuracy": accuracy,
        "external_macro_f1": f1,
        "diagnostic_remapped_accuracy": 0.9592384671711008,
        "probability_policy": (
            "Fine-label probabilities were summed into six broad categories; "
            "the displayed prediction is the broad category with the largest sum."
        ),
        "cells": cells,
    }

    for output in args.output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(payload, separators=(",", ":")),
            encoding="utf-8",
        )

    print(
        f"Exported {len(cells):,} cells ({len(evaluated_reviewed):,} evaluated; "
        f"{dendritic_count} reviewed dendritic) to {len(args.output)} file(s)."
    )
    print(f"Six-class grouped-probability accuracy: {accuracy:.6%}")
    print(f"Six-class macro-F1: {f1:.6f}")


if __name__ == "__main__":
    main()
