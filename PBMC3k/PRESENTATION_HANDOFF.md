# PBMC3k presentation content handoff

This is the frozen scientific-content package for the presentation team. Use
the claims and captions below with the exported figures in
`results/figures/`. Exact source values are also available in
`results/tables/presentation_source_values.csv`.

## Approved story

The project begins with 2,700 single-cell profiles from one healthy donor.
Quality control retains 2,638 cells, which are normalized and reduced to 2,000
high-variation genes for exploratory analysis. PCA, a 15-nearest-neighbor
graph, and UMAP reveal broad immune structure. Leiden community detection at
resolution 0.5 yields nine reviewed populations. Marker-gene evidence supports
seven labels at high confidence and two related T-cell labels at moderate
confidence. A leakage-safe comparison of nine classifier families selects
XGBoost by validation macro-F1. The result measures reproduction of the
reviewed labels within this dataset; it is not yet evidence of generalization
to other donors.

## Figure and copy package

### 1. Quality control and preprocessing

- **Asset:** `results/figures/qc_retained_cell_distributions.png`
- **Display title:** Quality control preserves 97.7% of cells
- **Caption:** Filters requiring 200–2,499 detected genes and less than 5%
  mitochondrial RNA retained 2,638 of 2,700 cells. Retained cells had a median
  of 2,213 UMI counts, 819 detected genes, and 2.01% mitochondrial RNA.
- **Conclusion:** The filters removed 62 low-quality or unusually complex
  profiles while retaining most of the dataset for downstream analysis.
- **Limitation:** The figure shows distributions after filtering. It does not
  prove that every retained profile is a singlet, and the thresholds are
  dataset-specific choices rather than universal biological rules.
- **Alt text:** Three histograms show UMI counts, detected genes, and
  mitochondrial RNA among 2,638 retained cells, with red dashed lines marking
  the gene-count and mitochondrial thresholds.
- **Sources:** `02_qc_preprocessing.ipynb` and
  `data/processed/pbmc3k_phase1_qc_top2000sd.h5ad`.

### 2. PCA and UMAP

- **Asset:** `results/figures/eda_pca_umap.png`
- **Display title:** Expression programs become a map of related cells
- **Caption:** PCA compresses the 2,000 selected genes before a
  15-nearest-neighbor graph and UMAP place transcriptionally similar cells
  near one another. The first 10 PCs, used to build the graph, account for
  10.2% of variance in the selected-gene matrix.
- **Conclusion:** The map contains coherent islands and gradients that support
  downstream community detection.
- **Limitation:** UMAP preserves local neighborhoods, not exact global
  distances or cluster sizes. The axes have no direct biological units, and a
  low two-dimensional separation is not by itself proof of a distinct cell
  type.
- **Alt text:** A PCA variance curve marks the 10 components used; beside it,
  a UMAP displays 2,638 cells colored into nine Leiden communities.
- **Sources:** `03_eda_clustering.ipynb` and
  `data/processed/pbmc3k_phase2_clustered.h5ad`.

### 3. Clustering comparison

- **Asset:** `results/figures/clustering_kmeans_leiden_comparison.png`
- **Display title:** Graph communities capture finer structure than K-means
- **Caption:** On the same UMAP, the diagnostic-selected K-means solution
  separates two broad groups, while Leiden at resolution 0.5 identifies nine
  graph communities. Their adjusted Rand index is 0.206, showing that the two
  methods encode different levels and shapes of structure.
- **Conclusion:** Leiden is used as the annotation reference because its nine
  communities provide biologically interpretable substructure; K-means serves
  as a broad cross-check.
- **Limitation:** Nine clusters were a team-selected configuration validated
  with sensitivity diagnostics, not the unique mathematically correct answer.
  Cluster boundaries can change with preprocessing, graph construction, and
  resolution.
- **Alt text:** Two panels plot identical UMAP coordinates. K-means colors two
  broad groups; Leiden divides the map into nine communities.
- **Sources:** `03_eda_clustering.ipynb` and the
  `kmeans_model_selection`/`leiden_model_selection` metadata in the Phase 2
  object.

### 4. Marker-gene annotation

- **Asset:** `results/figures/annotation_marker_dotplot.png`
- **Display title:** Known immune markers support nine reviewed populations
- **Caption:** Dot size is the fraction of cells expressing each gene; color
  is mean expression scaled within each gene. Concordant programs identify T,
  B, NK, monocyte, and platelet populations rather than relying on a single
  marker.
- **Conclusion:** Seven cluster labels have high-confidence marker support.
  Activated/transitional T cells and naive/resting T cells remain
  moderate-confidence labels because related T-cell states share markers.
- **Limitation:** The annotations are manual interpretations of expression
  patterns, not independent experimental ground truth. The platelet group has
  only 11 cells, and ambient RNA or doublets can distort rare populations.
- **Alt text:** A dot plot compares 18 known marker genes across nine reviewed
  cell types; canonical B-cell, monocyte, NK-cell, T-cell, and platelet marker
  pairs peak in their expected populations.
- **Sources:** `04_marker_gene_discovery.ipynb`,
  `results/tables/leiden_9_cell_type_annotations.csv`, and the Phase 3 object.

### 5. Model comparison

- **Asset:** `results/figures/classification_model_comparison.png`
- **Display title:** XGBoost wins the prespecified validation comparison
- **Caption:** Nine model families use the same stratified 70% train, 20%
  validation, and 10% test partitions. Feature selection and tuning occur
  within training data. XGBoost has the highest validation macro-F1 (0.928)
  and is therefore selected before test-set inspection.
- **Conclusion:** The selected XGBoost model reaches 90.2% test accuracy and
  0.893 test macro-F1 when reproducing the reviewed labels.
- **Limitation:** Logistic regression has higher post-selection test estimates
  (93.2% accuracy and 0.934 macro-F1), but test results must not retroactively
  choose the winner. The 264-cell test set is small and contains only one
  platelet.
- **Alt text:** A grouped bar chart compares validation and test macro-F1 and
  one-vs-rest ROC AUC for nine classifiers; XGBoost ranks first by validation
  macro-F1.
- **Sources:** `05_classification_model_comparison.ipynb` and
  `results/tables/classification_model_comparison.csv`.

### 6. Confusion matrix and per-class performance

- **Assets:** `results/figures/classification_confusion_matrix.png` and
  `results/tables/classification_best_model_per_class.csv`
- **Display title:** Most remaining errors occur between related T-cell states
- **Caption:** The row-normalized untouched-test confusion matrix shows strong
  separation for B cells, monocytes, NK cells, and platelets. The largest
  weakness is the activated/transitional T-cell class, where recall is 53.8%.
- **Conclusion:** Broad immune lineages are easier to reproduce than subtle,
  transcriptionally overlapping T-cell states.
- **Limitation:** Per-class results for rare groups are unstable: the platelet
  test result is based on one cell, and activated/transitional T cells have 13
  test examples. Percentages should always be shown with support counts.
- **Alt text:** A nine-by-nine normalized confusion matrix for XGBoost is
  strongly diagonal, with the most visible off-diagonal errors among related
  T-cell labels.
- **Sources:** `05_classification_model_comparison.ipynb` and
  `results/tables/classification_best_model_per_class.csv`.

### Optional supporting visuals

- `results/figures/classification_class_balance.png` shows the strong class
  imbalance and the 11-cell platelet population.
- `results/figures/classification_top_selected_genes.png` shows the 25 highest
  training-only ANOVA feature scores for the selected XGBoost pipeline. These
  are association scores, not causal effects or XGBoost feature importance.

## Required wording for the model result

Use:

> XGBoost was selected because it achieved the highest validation macro-F1.
> Logistic regression produced the highest test-set estimate, but the test set
> was reserved for final evaluation and did not determine model selection.

Do not call logistic regression the “winner,” and do not claim that XGBoost is
proven to generalize to new donors.

## Project-level limitations

- PBMC3k contains one healthy donor, so donor-level and batch-level
  generalization are untested.
- The classifier targets labels inferred from the same expression dataset;
  accuracy measures label reproduction, not independent biological truth.
- Random cell splits can place very similar cells from the same donor in
  training and test sets.
- UMAP and clustering depend on preprocessing and hyperparameter choices.
- Rare-population estimates, especially platelets, have very wide uncertainty.

The next scientific phase is external validation on independently processed
donors using group-aware splits, consistent gene identifiers and normalization,
and ideally expert or orthogonal reference labels.

## Reproduction

From the analysis repository:

```bash
PBMC3k/.venv/bin/python PBMC3k/scripts/export_presentation_figures.py
```

To regenerate the classification tables and figures, execute
`PBMC3k/notebooks/05_classification_model_comparison.ipynb` from top to bottom
in the project environment.
