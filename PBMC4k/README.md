# PBMC4k integration and cross-dataset classification plan

## Project goal

This extension adds the 10x Genomics PBMC4k dataset to the existing PBMC3k
analysis. The central research question is:

> Can PBMC cell populations be reproduced across two independent datasets, and
> can a classifier trained on one dataset accurately identify cells in the
> other?

The project has three connected goals:

1. **Integration:** determine whether Harmony can reduce dataset-specific
   technical separation.
2. **Biology:** determine whether the same cell populations and marker genes
   are reproduced in both datasets.
3. **Machine learning:** determine whether a classifier trained on one dataset
   generalizes to the other.

The PBMC4k dataset contains approximately 4,342 cells from one healthy donor.
The public documentation does not establish that the PBMC3k and PBMC4k samples
came from different people. They should therefore be described as two datasets
or samples, not definitively as two donors.

## Proposed repository structure

PBMC4k should remain separate from PBMC3k. Raw and individually processed files
must not be mixed together.

```text
26-the-backpropagators-analysis/
├── PBMC3k/
│   ├── data/
│   │   ├── raw/
│   │   ├── interim/
│   │   └── processed/
│   ├── notebooks/
│   └── results/
│
├── PBMC4k/
│   ├── data/
│   │   ├── raw/
│   │   ├── interim/
│   │   └── processed/
│   ├── notebooks/
│   └── results/
│
└── PBMC_integrated/
    ├── data/
    │   └── processed/
    ├── notebooks/
    │   └── 01_pbmc3k_pbmc4k_harmony.ipynb
    └── results/
```

The original PBMC3k files remain under `PBMC3k/data/raw/`. Original PBMC4k
files belong under `PBMC4k/data/raw/`. Only combined PBMC3k and PBMC4k objects
belong under `PBMC_integrated/data/processed/`.

Large raw and processed data files should remain excluded from Git. Only folder
placeholders, notebooks, source code, documentation, and selected result tables
or figures should be committed.

## Required download

Harmony does not require the BAM, BAM index, molecule-information file, or every
Cell Ranger output. The filtered gene-by-cell count matrix is sufficient for
this analysis.

The PBMC4k filtered matrix is approximately 72 MB. Expected download times are:

- fast connection: under 1 minute;
- typical connection: 1–5 minutes;
- slow connection: 5–15 minutes;
- extraction: usually a few seconds.

Downloading the complete Cell Ranger output would require substantially more
time and storage and is unnecessary for this workflow.

Dataset source:

- [4k PBMCs from a Healthy Donor — 10x Genomics](https://www.10xgenomics.com/datasets/4-k-pbm-cs-from-a-healthy-donor-2-standard-1-3-0)

## Phase 1: process PBMC4k separately

PBMC4k should first receive its own quality-control and preprocessing analysis.
The general procedure should match PBMC3k, but numerical QC thresholds should
be selected from PBMC4k's distributions rather than copied blindly.

The initial PBMC4k workflow should:

1. Read the filtered count matrix.
2. Calculate cell- and gene-level QC metrics.
3. Inspect genes detected per cell, total counts, and mitochondrial percentage.
4. Remove low-quality cells.
5. Remove very lowly expressed genes.
6. investigate possible doublets.
7. Preserve raw counts in an AnnData layer.
8. Normalize and log-transform expression.
9. Save a separately processed PBMC4k AnnData object.

For example:

```python
adata.layers["counts"] = adata.X.copy()
```

## Phase 2: make the datasets compatible

Before concatenation:

1. Standardize gene identifiers.
2. Resolve duplicated gene names.
3. Determine the genes shared by both datasets.
4. Confirm that normalization is consistent.
5. Prefix cell barcodes with their dataset.
6. Add an explicit `dataset` column to cell metadata.

Example identifiers:

```text
cell_id                     dataset
pbmc3k_AAACATACAACCAC-1     PBMC3k
pbmc4k_AAACCTGAGAAACCAT-1   PBMC4k
```

Prefixes are required because identical barcode sequences can occur
independently in separate 10x experiments.

The combined AnnData object should retain:

- original counts;
- normalized expression;
- dataset membership;
- QC metrics;
- the original cell barcode;
- any reviewed labels available for PBMC3k.

## Phase 3: establish an uncorrected baseline

Before running Harmony, calculate PCA, neighbors, UMAP, and exploratory clusters
without batch correction.

Create plots colored by:

- dataset;
- Leiden cluster;
- major cell-type markers;
- reviewed PBMC3k cell type, where available.

These plots establish whether cells primarily separate by biology or by their
dataset of origin. They also provide a baseline against which Harmony can be
evaluated.

## Phase 4: integrate with Harmony

The integration order should be:

```text
Normalization
     ↓
Batch-aware variable-gene selection
     ↓
Scaling
     ↓
PCA
     ↓
Harmony using dataset
     ↓
Neighbor graph
     ↓
UMAP and Leiden clustering
```

In Scanpy, Harmony should run after PCA and before calculating the neighbor
graph:

```python
import scanpy.external as sce

sce.pp.harmony_integrate(
    adata,
    key="dataset",
    basis="X_pca",
    adjusted_basis="X_pca_harmony",
)

sc.pp.neighbors(adata, use_rep="X_pca_harmony")
sc.tl.umap(adata)
sc.tl.leiden(adata)
```

Harmony modifies the low-dimensional PCA coordinates. It does not produce
batch-corrected gene-expression counts.

Use the Harmony representation for:

- neighbor construction;
- UMAP;
- clustering;
- visualization of integrated structure.

Use the original normalized expression for:

- marker-gene testing;
- differential expression;
- gene-level biological interpretation;
- classifier inputs.

Harmony reference:

- [Scanpy Harmony integration documentation](https://scanpy.readthedocs.io/en/stable/generated/scanpy.external.pp.harmony_integrate.html)
- [Korsunsky et al., 2019](https://www.nature.com/articles/s41592-019-0619-0)

## Phase 5: validate the integration

A visually mixed UMAP is not sufficient evidence of successful integration.
The analysis must determine whether Harmony removed technical separation while
preserving meaningful biology.

Validation questions include:

- Do cells from both datasets mix within the same biological populations?
- Are B cells still distinct from monocytes, NK cells, and T cells?
- Are rare populations such as platelets preserved?
- Do known marker genes remain biologically coherent?
- Did Harmony incorrectly merge distinct T-cell populations?
- Are any clusters composed almost entirely of one dataset?
- Are populations present before Harmony lost afterward?

The desired result is:

```text
Remove dataset separation
Preserve cell-type separation
```

Both before- and after-Harmony plots should be retained.

## Phase 6: annotate PBMC4k independently

PBMC4k requires reviewed cell-type labels before it can fairly evaluate the
classifier.

Integrated clusters may help align populations across datasets, but PBMC4k
labels should be supported by marker-gene review. Candidate markers include:

| Population | Example markers |
|---|---|
| B cells | `CD79A`, `MS4A1`, `CD37` |
| NK cells | `NKG7`, `GNLY`, `PRF1` |
| Classical monocytes | `LYZ`, `S100A8`, `S100A9`, `CTSD` |
| Non-classical monocytes | `FCGR3A`, `LST1`, `FCER1G` |
| Memory/helper T cells | `IL7R`, `LTB`, `MALAT1` |
| Cytotoxic T cells | `CD3D`, `CD8A`, `CST7`, `NKG7` |
| Platelets | `PPBP`, `GNG11`, `PF4`, `ITGA2B` |

The PBMC3k classifier's predictions must not be used as PBMC4k ground truth.
Doing so would create circular evaluation:

```text
Model creates PBMC4k labels
            ↓
Same model is evaluated against those labels
```

## Phase 7: evaluate the existing PBMC3k classifier

The first model experiment should not involve retraining.

Keep the current XGBoost pipeline frozen:

```text
Train: PBMC3k
Test:  PBMC4k
```

PBMC4k expression must be aligned to the gene names, gene order, and
normalization expected by the saved PBMC3k pipeline.

Report:

- accuracy;
- balanced accuracy;
- macro-F1;
- weighted F1;
- per-cell-type precision and recall;
- multiclass ROC/AUC where appropriate;
- confusion matrix;
- confidence distributions;
- percentage of uncertain predictions.

This test answers whether the model learned transferable immune-cell biology or
mainly PBMC3k-specific patterns.

The PBMC4k test data must not influence:

- PBMC3k feature selection;
- XGBoost hyperparameters;
- confidence thresholds;
- model-family selection.

## Phase 8: reverse the experiment

After PBMC4k has independently reviewed labels, train a comparable classifier
on PBMC4k and test it on PBMC3k:

```text
Train: PBMC4k
Test:  PBMC3k
```

The two transfer experiments provide stronger evidence than a random
within-dataset cell split:

```text
PBMC3k → PBMC4k
PBMC4k → PBMC3k
```

If the same cell populations are recognized in both directions, their marker
patterns are more likely to be reproducible.

## Phase 9: train a combined model

Only after the external transfer experiments are complete should a final
combined model be trained.

```text
Training data = reviewed PBMC3k cells + reviewed PBMC4k cells
```

The combined model should:

- use genes shared by both datasets;
- use consistent normalization;
- perform feature selection only inside training folds;
- account for class imbalance;
- learn from both datasets' technical variation;
- report calibrated or clearly described confidence values;
- save the full preprocessing and classifier pipeline.

After this model has seen both datasets, neither PBMC3k nor PBMC4k remains a
fully independent final test. A third compatible PBMC dataset would be required
for an untouched evaluation of the combined model.

Harmony coordinates should not be the default classifier input. A classifier
using common normalized genes is easier to apply to future datasets. Harmony is
primarily used here for integrated structure, clustering, and annotation.

## Proposed analyses and website outputs

### Integrated cell atlas

Create an interactive UMAP containing both datasets with controls for:

```text
Color by:
○ Cell type
○ Dataset
○ Leiden cluster
○ Model prediction
```

Add a comparison control:

```text
[ Before Harmony ]  [ After Harmony ]
```

### Cross-dataset model dashboard

Display transfer results separately:

```text
PBMC3k → PBMC4k
Accuracy: ...
Macro-F1: ...

PBMC4k → PBMC3k
Accuracy: ...
Macro-F1: ...
```

### Marker reproducibility

Compare marker lists for matched cell types:

```text
NK-cell markers

PBMC3k: NKG7, GNLY, CST7
PBMC4k: NKG7, GNLY, PRF1
Shared: NKG7, GNLY
```

### Error explorer

Allow users to inspect cells where:

- reviewed and predicted labels disagree;
- prediction confidence is low;
- performance differs between datasets;
- biologically related T-cell populations are confused.

### Descriptive population comparison

Compare cell-type proportions between datasets, but do not attribute
differences to donor biology. With one sample per dataset, donor, collection,
sequencing, processing, and batch effects are confounded.

## Expected timing

Approximate working times:

- create folder structure: 5 minutes;
- download and extract the filtered PBMC4k matrix: 1–15 minutes;
- verify and load the matrix: 5 minutes;
- PBMC4k QC and preprocessing: 30–60 minutes;
- combine datasets and run an initial Harmony analysis: 20–40 minutes;
- validate clusters, markers, and dataset mixing: 1–2 hours;
- produce a careful, presentation-ready analysis: approximately 3–5 hours.

The download is the smallest part of the work. The important time is spent
checking data compatibility, choosing defensible QC thresholds, reviewing
markers, and validating that integration does not erase real biology.

## Decision sequence

The project should follow this order:

1. Download PBMC4k filtered counts.
2. Process and QC PBMC4k independently.
3. Standardize genes and cell identifiers.
4. Build an uncorrected combined baseline.
5. Run Harmony.
6. Validate integration.
7. Annotate PBMC4k using marker review.
8. Test the frozen PBMC3k model on PBMC4k.
9. Train PBMC4k and test on PBMC3k.
10. Compare shared markers and classification errors.
11. Train a final combined model.
12. Seek a third dataset for an untouched final evaluation.
