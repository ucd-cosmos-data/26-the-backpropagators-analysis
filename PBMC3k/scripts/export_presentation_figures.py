"""Export presentation-ready figures from the saved PBMC3k analysis objects.

Run from any directory with:

    PBMC3k/.venv/bin/python PBMC3k/scripts/export_presentation_figures.py

The script reads the immutable Phase 1–3 analysis artifacts and writes PNG
figures plus a compact source-value table. It does not refit or relabel data.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import anndata as ad
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


PROJECT = Path(__file__).resolve().parents[1]
PROCESSED = PROJECT / "data" / "processed"
FIGURES = PROJECT / "results" / "figures"
TABLES = PROJECT / "results" / "tables"
FIGURES.mkdir(parents=True, exist_ok=True)
TABLES.mkdir(parents=True, exist_ok=True)

DPI = 200
STARTING_CELLS = 2_700
STARTING_GENES = 32_738
MIN_GENES = 200
MAX_GENES = 2_500
MAX_MT_PERCENT = 5.0
SELECTED_GENES = 2_000
PCA_COMPONENTS = 10
NEIGHBORS = 15
LEIDEN_RESOLUTION = 0.5

sns.set_theme(style="whitegrid", context="talk")


def save_figure(fig: plt.Figure, filename: str) -> None:
    path = FIGURES / filename
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved {path.relative_to(PROJECT)}")


def scatter_categories(
    axis: plt.Axes,
    coordinates: np.ndarray,
    labels: pd.Series,
    title: str,
    palette: list[str] | None = None,
) -> None:
    categories = labels.astype("category")
    names = list(categories.cat.categories)
    colors = palette or sns.color_palette("tab10", len(names)).as_hex()
    for name, color in zip(names, colors, strict=False):
        mask = np.asarray(categories == name)
        axis.scatter(
            coordinates[mask, 0],
            coordinates[mask, 1],
            s=8,
            alpha=0.82,
            linewidth=0,
            color=color,
            label=str(name),
        )
    axis.set(title=title, xlabel="UMAP 1", ylabel="UMAP 2")
    axis.set_xticks([])
    axis.set_yticks([])
    axis.legend(
        bbox_to_anchor=(1.02, 0.5),
        loc="center left",
        frameon=False,
        fontsize=8,
        markerscale=2,
    )


phase1 = ad.read_h5ad(PROCESSED / "pbmc3k_phase1_qc_top2000sd.h5ad")
phase2 = ad.read_h5ad(PROCESSED / "pbmc3k_phase2_clustered.h5ad")
phase3 = ad.read_h5ad(PROCESSED / "pbmc3k_phase3_annotated.h5ad")


# Quality control: distributions of the cells that passed all three filters.
fig, axes = plt.subplots(1, 3, figsize=(15, 4.6))
sns.histplot(phase1.obs["total_counts"], bins=45, ax=axes[0], color="#4c78a8")
axes[0].set(title="Library size after QC", xlabel="UMI counts per cell", ylabel="Cells")
sns.histplot(phase1.obs["n_genes_by_counts"], bins=45, ax=axes[1], color="#59a14f")
axes[1].axvline(MIN_GENES, color="#b22222", linestyle="--", linewidth=1.5)
axes[1].axvline(MAX_GENES, color="#b22222", linestyle="--", linewidth=1.5)
axes[1].set(title="Detected genes after QC", xlabel="Genes per cell", ylabel="Cells")
sns.histplot(phase1.obs["pct_counts_mt"], bins=45, ax=axes[2], color="#f28e2b")
axes[2].axvline(MAX_MT_PERCENT, color="#b22222", linestyle="--", linewidth=1.5)
axes[2].set(title="Mitochondrial RNA after QC", xlabel="Mitochondrial counts (%)", ylabel="Cells")
fig.suptitle(
    f"QC retained {phase1.n_obs:,} of {STARTING_CELLS:,} cells "
    f"({100 * phase1.n_obs / STARTING_CELLS:.1f}%)",
    y=1.03,
)
fig.tight_layout()
save_figure(fig, "qc_retained_cell_distributions.png")


# Exploratory analysis: variance captured by PCs and the resulting UMAP.
variance_ratio = np.asarray(phase2.uns["pca"]["variance_ratio"])
fig, axes = plt.subplots(1, 2, figsize=(15, 5.8), gridspec_kw={"width_ratios": [1, 1.25]})
component_numbers = np.arange(1, min(20, len(variance_ratio)) + 1)
axes[0].plot(
    component_numbers,
    100 * variance_ratio[: len(component_numbers)],
    marker="o",
    color="#4c78a8",
)
axes[0].axvline(PCA_COMPONENTS, color="#b22222", linestyle="--", label="10 PCs used")
axes[0].set(
    title="PCA variance profile",
    xlabel="Principal component",
    ylabel="Variance explained (%)",
    xticks=[1, 5, 10, 15, 20],
)
axes[0].legend(frameon=False)
scatter_categories(
    axes[1],
    np.asarray(phase2.obsm["X_umap"]),
    phase2.obs["leiden"],
    "UMAP of the 15-neighbor graph",
    list(phase2.uns.get("leiden_colors", [])),
)
fig.suptitle("From high-dimensional expression to a two-dimensional cell map", y=1.02)
fig.tight_layout()
save_figure(fig, "eda_pca_umap.png")


# Clustering comparison: same coordinates, different partitioning assumptions.
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
scatter_categories(
    axes[0],
    np.asarray(phase2.obsm["X_umap"]),
    phase2.obs["kmeans"],
    "K-means: selected K = 2",
    list(phase2.uns.get("kmeans_colors", [])),
)
scatter_categories(
    axes[1],
    np.asarray(phase2.obsm["X_umap"]),
    phase2.obs["leiden"],
    "Leiden: resolution 0.5, 9 communities",
    list(phase2.uns.get("leiden_colors", [])),
)
ari = float(phase2.uns["leiden_model_selection"]["kmeans_agreement_ari"])
fig.suptitle(f"Clustering cross-check on the same UMAP (adjusted Rand index = {ari:.3f})", y=1.02)
fig.tight_layout()
save_figure(fig, "clustering_kmeans_leiden_comparison.png")


# Annotation: known lineage markers across the reviewed cell types.
marker_map = {
    "Cytotoxic CD8 T": ["CD8A", "CCL5"],
    "B": ["MS4A1", "CD79A"],
    "Memory/helper T": ["IL7R", "LTB"],
    "Classical mono.": ["S100A8", "FCN1"],
    "CD16+ mono.": ["FCGR3A", "LST1"],
    "NK": ["GNLY", "NKG7"],
    "Activated T": ["GZMK", "IL32"],
    "Naive T": ["CCR7", "MAL"],
    "Platelet": ["PPBP", "PF4"],
}
marker_genes = [gene for genes in marker_map.values() for gene in genes]
raw_gene_names = set(phase3.raw.var_names)
missing = [gene for gene in marker_genes if gene not in raw_gene_names]
if missing:
    raise ValueError(f"Marker genes missing from the normalized full-gene matrix: {missing}")

expression = phase3.raw[:, marker_genes].X
if hasattr(expression, "toarray"):
    expression = expression.toarray()
expression = np.asarray(expression)
labels = phase3.obs["cell_type"].astype(str)
cell_type_order = (
    phase3.obs.groupby("cell_type", observed=True).size().sort_values(ascending=False).index.tolist()
)
mean_expression = pd.DataFrame(expression, columns=marker_genes).groupby(
    labels.reset_index(drop=True), observed=True
).mean()
fraction_expressing = pd.DataFrame(expression > 0, columns=marker_genes).groupby(
    labels.reset_index(drop=True), observed=True
).mean()
mean_expression = mean_expression.loc[cell_type_order]
fraction_expressing = fraction_expressing.loc[cell_type_order]
scaled_mean = (mean_expression - mean_expression.min()) / (
    mean_expression.max() - mean_expression.min()
).replace(0, 1)

fig, axis = plt.subplots(figsize=(15, 6.8))
for row, cell_type in enumerate(cell_type_order):
    for column, gene in enumerate(marker_genes):
        axis.scatter(
            column,
            row,
            s=30 + 310 * fraction_expressing.loc[cell_type, gene],
            c=scaled_mean.loc[cell_type, gene],
            cmap="viridis",
            vmin=0,
            vmax=1,
            edgecolor="none",
        )
axis.set(
    title="Known marker programs support the reviewed cell-type labels",
    xlabel="Marker gene",
    ylabel="Reviewed cell type",
    xticks=np.arange(len(marker_genes)),
    xticklabels=marker_genes,
    yticks=np.arange(len(cell_type_order)),
    yticklabels=cell_type_order,
)
axis.tick_params(axis="x", rotation=45)
axis.invert_yaxis()
axis.grid(False)
for boundary in np.cumsum([len(genes) for genes in marker_map.values()])[:-1] - 0.5:
    axis.axvline(boundary, color="#d0d0d0", linewidth=0.8)
size_handles = [
    axis.scatter([], [], s=30 + 310 * fraction, color="#5b8c85", label=f"{int(100*fraction)}%")
    for fraction in (0.25, 0.5, 0.75)
]
axis.legend(
    handles=size_handles,
    title="Cells expressing",
    bbox_to_anchor=(1.01, 0.5),
    loc="center left",
    frameon=False,
)
fig.tight_layout()
save_figure(fig, "annotation_marker_dotplot.png")


annotation_counts = phase3.obs["cell_type"].astype(str).value_counts()
confidence_counts = phase3.obs[["leiden", "annotation_confidence"]].drop_duplicates()[
    "annotation_confidence"
].value_counts()
metrics = [
    ("preprocessing", "starting_cells", STARTING_CELLS, "02_qc_preprocessing.ipynb output"),
    ("preprocessing", "retained_cells", phase1.n_obs, "phase1 .h5ad"),
    ("preprocessing", "removed_cells", STARTING_CELLS - phase1.n_obs, "derived"),
    ("preprocessing", "starting_genes", STARTING_GENES, "02_qc_preprocessing.ipynb output"),
    ("preprocessing", "genes_after_detection_filter", phase1.raw.n_vars, "phase1 .h5ad raw"),
    ("preprocessing", "selected_genes", phase1.n_vars, "phase1 .h5ad"),
    ("clustering", "pca_components", PCA_COMPONENTS, "03_eda_clustering.ipynb"),
    ("clustering", "nearest_neighbors", NEIGHBORS, "phase2 .h5ad metadata"),
    ("clustering", "leiden_resolution", LEIDEN_RESOLUTION, "phase2 .h5ad metadata"),
    ("clustering", "leiden_clusters", phase2.obs["leiden"].nunique(), "phase2 .h5ad"),
    ("clustering", "kmeans_leiden_ari", ari, "phase2 .h5ad metadata"),
    ("annotation", "reviewed_cell_types", phase3.obs["cell_type"].nunique(), "phase3 .h5ad"),
    ("annotation", "high_confidence_clusters", confidence_counts.get("high", 0), "phase3 .h5ad"),
    ("annotation", "moderate_confidence_clusters", confidence_counts.get("moderate", 0), "phase3 .h5ad"),
]
for cell_type, count in annotation_counts.items():
    metrics.append(("annotation", f"cells_{cell_type}", int(count), "phase3 .h5ad"))

comparison_path = TABLES / "classification_model_comparison.csv"
report_path = TABLES / "classification_best_model_per_class.csv"
if comparison_path.is_file():
    comparison = pd.read_csv(comparison_path)
    selected = comparison.iloc[0]
    logistic = comparison.loc[comparison["model"] == "Logistic regression"].iloc[0]
    metrics.extend(
        [
            ("classification", "selected_model", selected["model"], "model-comparison CSV rank 1"),
            (
                "classification",
                "selected_validation_macro_f1",
                selected["validation_macro_f1"],
                "model-comparison CSV",
            ),
            (
                "classification",
                "selected_test_accuracy",
                selected["test_accuracy"],
                "model-comparison CSV",
            ),
            (
                "classification",
                "selected_test_macro_f1",
                selected["test_macro_f1"],
                "model-comparison CSV",
            ),
            (
                "classification",
                "logistic_test_accuracy",
                logistic["test_accuracy"],
                "model-comparison CSV",
            ),
            (
                "classification",
                "logistic_test_macro_f1",
                logistic["test_macro_f1"],
                "model-comparison CSV",
            ),
        ]
    )
if report_path.is_file():
    per_class = pd.read_csv(report_path, index_col=0)
    class_rows = per_class.loc[
        ~per_class.index.isin(["accuracy", "macro avg", "weighted avg"])
    ]
    metrics.append(
        (
            "classification",
            "test_cells",
            int(class_rows["support"].sum()),
            "best-model per-class CSV",
        )
    )
    for cell_type, row in class_rows.iterrows():
        metrics.extend(
            [
                (
                    "classification",
                    f"test_support_{cell_type}",
                    int(row["support"]),
                    "best-model per-class CSV",
                ),
                (
                    "classification",
                    f"test_recall_{cell_type}",
                    row["recall"],
                    "best-model per-class CSV",
                ),
            ]
        )

metrics_table = pd.DataFrame(metrics, columns=["stage", "metric", "value", "source"])
metrics_table.to_csv(TABLES / "presentation_source_values.csv", index=False)
print(f"Saved {(TABLES / 'presentation_source_values.csv').relative_to(PROJECT)}")
