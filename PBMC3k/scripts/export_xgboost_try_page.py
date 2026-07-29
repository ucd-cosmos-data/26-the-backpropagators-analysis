"""Train the selected PBMC3k XGBoost pipeline and export website artifacts."""

from __future__ import annotations

import json
from pathlib import Path

import anndata as ad
import joblib
import numpy as np
from scipy import sparse
from sklearn.feature_selection import SelectKBest, VarianceThreshold, f_classif
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier


RANDOM_STATE = 42
TRAIN_SIZE = 0.70
VALIDATION_SIZE = 0.20
TEST_SIZE = 0.10
N_SELECTED_GENES = 2_000

PROJECT = Path(__file__).resolve().parents[1]
WORKSPACE = PROJECT.parents[1]
INPUT = PROJECT / "data" / "processed" / "pbmc3k_phase3_annotated.h5ad"
MODEL_PATH = PROJECT / "models" / "pbmc_cell_classifier.joblib"
METADATA_PATH = PROJECT / "models" / "pbmc_cell_classifier_metadata.json"
WEB_DATA_PATHS = [
    WORKSPACE
    / "26-the-backpropagators"
    / "static"
    / "data"
    / "pbmc3k-cell-predictions.json",
    WORKSPACE
    / "26-the-backpropagators-presentation"
    / "public"
    / "data"
    / "pbmc3k-cell-predictions.json",
]


def main() -> None:
    adata = ad.read_h5ad(INPUT)
    if adata.raw is None or "cell_type" not in adata.obs:
        raise ValueError("The annotated object must contain raw expression and cell_type labels.")

    expression = adata.raw.X.astype(np.float64).copy()
    if not sparse.issparse(expression):
        expression = sparse.csr_matrix(expression)
    else:
        expression = expression.tocsr()

    gene_names = np.asarray(adata.raw.var_names).astype(str)
    encoder = LabelEncoder()
    labels = encoder.fit_transform(adata.obs["cell_type"].astype(str))
    class_names = encoder.classes_.astype(str)

    indices = np.arange(adata.n_obs)
    development_idx, test_idx = train_test_split(
        indices,
        test_size=TEST_SIZE,
        stratify=labels,
        random_state=RANDOM_STATE,
    )
    validation_fraction = VALIDATION_SIZE / (TRAIN_SIZE + VALIDATION_SIZE)
    train_idx, validation_idx = train_test_split(
        development_idx,
        test_size=validation_fraction,
        stratify=labels[development_idx],
        random_state=RANDOM_STATE,
    )

    pipeline = Pipeline(
        [
            ("variance", VarianceThreshold()),
            (
                "select",
                SelectKBest(
                    score_func=f_classif,
                    k=min(N_SELECTED_GENES, expression.shape[1]),
                ),
            ),
            (
                "classifier",
                XGBClassifier(
                    objective="multi:softprob",
                    eval_metric="mlogloss",
                    n_estimators=250,
                    max_depth=6,
                    learning_rate=0.1,
                    subsample=0.8,
                    colsample_bytree=0.8,
                    tree_method="hist",
                    random_state=RANDOM_STATE,
                    n_jobs=1,
                ),
            ),
        ]
    )
    pipeline.fit(expression[train_idx], labels[train_idx])

    test_predictions = pipeline.predict(expression[test_idx])
    test_accuracy = accuracy_score(labels[test_idx], test_predictions)
    test_macro_f1 = f1_score(labels[test_idx], test_predictions, average="macro")

    # Catch a broken preprocessing or split while allowing small library-version
    # differences from the notebook's saved XGBoost run.
    if test_accuracy < 0.85 or test_macro_f1 < 0.80:
        raise RuntimeError(
            "Exported model scores are unexpectedly low: "
            f"accuracy={test_accuracy:.6f}, macro-F1={test_macro_f1:.6f}"
        )

    probabilities = pipeline.predict_proba(expression)
    predictions = probabilities.argmax(axis=1)

    split_names = np.full(adata.n_obs, "development", dtype=object)
    split_names[train_idx] = "training"
    split_names[validation_idx] = "validation"
    split_names[test_idx] = "test"

    cells = []
    for index in range(adata.n_obs):
        probability_values = probabilities[index]
        cells.append(
            {
                "number": index + 1,
                "barcode": str(adata.obs_names[index]),
                "split": str(split_names[index]),
                "reviewed": str(class_names[labels[index]]),
                "predicted": str(class_names[predictions[index]]),
                "confidence": round(float(probability_values[predictions[index]]), 4),
                "probabilities": [round(float(value), 4) for value in probability_values],
            }
        )

    metadata = {
        "model": "XGBoost",
        "classes": class_names.tolist(),
        "gene_names": gene_names.tolist(),
        "selected_gene_count": N_SELECTED_GENES,
        "training_cells": int(len(train_idx)),
        "validation_cells": int(len(validation_idx)),
        "test_cells": int(len(test_idx)),
        "test_accuracy": float(test_accuracy),
        "test_macro_f1": float(test_macro_f1),
        "random_state": RANDOM_STATE,
        "cell_numbering": "One-based position in pbmc3k_phase3_annotated.h5ad",
    }
    web_payload = {
        "model": "XGBoost",
        "classes": class_names.tolist(),
        "cell_count": int(adata.n_obs),
        "test_accuracy": round(float(test_accuracy), 4),
        "test_macro_f1": round(float(test_macro_f1), 4),
        "cells": cells,
    }

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH, compress=3)
    METADATA_PATH.write_text(json.dumps(metadata, indent=2) + "\n")
    serialized_web_payload = json.dumps(web_payload, separators=(",", ":")) + "\n"
    for web_data_path in WEB_DATA_PATHS:
        web_data_path.parent.mkdir(parents=True, exist_ok=True)
        web_data_path.write_text(serialized_web_payload)

    reloaded_pipeline = joblib.load(MODEL_PATH)
    if not np.array_equal(
        reloaded_pipeline.predict(expression[test_idx]),
        test_predictions,
    ):
        raise RuntimeError("Predictions changed after reloading the saved pipeline.")

    print(f"Saved model: {MODEL_PATH}")
    print(f"Saved metadata: {METADATA_PATH}")
    for web_data_path in WEB_DATA_PATHS:
        print(f"Saved website data: {web_data_path}")
    print(f"Cells exported: {adata.n_obs:,}")
    print(f"Test accuracy: {test_accuracy:.3f}")
    print(f"Test macro-F1: {test_macro_f1:.3f}")


if __name__ == "__main__":
    main()
