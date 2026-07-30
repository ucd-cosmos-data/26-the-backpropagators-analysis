# PBMC3k–PBMC4k integrated analysis

This folder contains analyses that combine the two independently processed
datasets. The donor-specific PBMC3k and PBMC4k outputs remain unchanged.

Project assumption:

- PBMC3k is treated as Donor 1.
- PBMC4k is treated as Donor 2.

The public source metadata does not prove that these are different people, so
this is an explicit analysis assumption rather than a verified donor identity.

## Notebook 6: Harmony integration

[`notebooks/06_pbmc3k_pbmc4k_harmony.ipynb`](notebooks/06_pbmc3k_pbmc4k_harmony.ipynb)
rebuilds both reviewed cell sets from the original filtered count matrices,
keeps only shared genes, normalizes them consistently, creates an uncorrected
PCA/UMAP/Leiden baseline, and then runs Harmony using the dataset label.

The notebook evaluates:

- whether local neighborhoods mix better across datasets;
- whether reviewed cell-type neighborhoods remain coherent;
- whether clusters become less associated with dataset membership;
- how each shared cell type mixes across the two datasets;
- whether donor-specific rare populations remain visible.

The notebook keeps Leiden resolution 0.5 as the primary consistency setting
and includes a 0.4–1.0 sensitivity review. In the current result, dendritic
cells and platelets share a small cluster at resolution 0.5 but separate at
resolution 0.6; both assignments are saved and the distinction is reported
instead of hidden.

Harmony changes PCA coordinates only. It does not alter the count or normalized
gene-expression matrices, and Harmony coordinates must not be used as XGBoost
features.

Generated data are saved under `data/processed/`, figures under
`results/figures/`, and summary tables under `results/tables/`.

## Notebook 7: reverse external XGBoost validation

[`notebooks/07_pbmc4k_to_pbmc3k_xgboost.ipynb`](notebooks/07_pbmc4k_to_pbmc3k_xgboost.ipynb)
trains and tunes a new XGBoost pipeline using only PBMC4k, refits it on all
PBMC4k cells, and evaluates every PBMC3k cell as external data. It uses
normalized genes shared by both datasets, never Harmony coordinates.

Shared-class metrics are reported separately from PBMC3k platelets, which are
unknown to the PBMC4k-trained model. The notebook also saves a bidirectional
comparison with the frozen PBMC3k-to-PBMC4k result. These scores measure
agreement with reviewed marker-based labels, not definitive biological truth.

## Notebook 8: controlled shared-eight-class test

[`notebooks/08_shared8_pbmc3k_to_pbmc4k_xgboost.ipynb`](notebooks/08_shared8_pbmc3k_to_pbmc4k_xgboost.ipynb)
reproduces the original PBMC3k split, excludes platelets, and trains a separate
eight-class XGBoost model using the frozen model's selected settings. It tests
that model on PBMC4k after dendritic-cell exclusion and compares it on the same
4,097 cells with the frozen nine-class model.

This is an ablation experiment to isolate the effect of removing unsupported
rare classes. It does not overwrite either model or donor-specific dataset and
does not replace the required cross-dataset T-cell label review.

## Notebook 9: T-cell label compatibility

[`notebooks/09_tcell_label_compatibility.ipynb`](notebooks/09_tcell_label_compatibility.ipynb)
compares T-cell marker programs, bidirectional prediction errors, and a
T-cell-only Harmony representation. It records a non-destructive broad
six-class proposal in which the fine T-cell labels are retained as metadata but
mapped to `Cytotoxic T cells` or `Non-cytotoxic T cells` for cross-dataset
modeling.

The notebook re-scores existing predictions under that broad taxonomy only as
a diagnostic. It does not train a specialist or overwrite either donor's
reviewed labels.
