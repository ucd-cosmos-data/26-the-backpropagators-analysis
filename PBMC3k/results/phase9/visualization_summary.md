# Phase 9 Visualization Summary

## Execution status

- Figures complete or partial: **8**
- Figures skipped or failed: **2**
- Manifest: `results/phase9/figure_manifest.csv`

## Figures successfully generated

- Figure 2: Cluster and cell-type composition (COMPLETE)
- Figure 3: Representative marker-gene heatmap (COMPLETE)
- Figure 4: Marker specificity summary (COMPLETE)
- Figure 5: Machine-learning model comparison (COMPLETE)
- Figure 7: Phase 8 biological reasoning summary (COMPLETE)
- Figure 8: Evidence and validation overview (COMPLETE)
- Figure 9: Complete project pipeline diagram (COMPLETE)
- Figure 10: Cluster summary table (COMPLETE)

## Figures skipped or failed

- Figure 1: Final annotated UMAP — unhashable type: 'list'
- Figure 6: Confusion matrix for the best classifier — Phase 5 did not save held-out true labels and predictions. Regenerating the split or retraining/rerunning a classifier is prohibited, so counts and normalized confusion matrices cannot be produced without fabrication.

## Source files used

- data/processed/pbmc3k_phase3_annotated.h5ad
- notebooks/01_explore_all_pbmc3k_files.ipynb
- notebooks/02_qc_preprocessing.ipynb
- notebooks/03_eda_clustering.ipynb
- notebooks/04_marker_gene_discovery.ipynb
- notebooks/05_classification_model_comparison.ipynb
- notebooks/06_cluster_biological_interpretation.ipynb
- notebooks/07_literature_integration.ipynb
- notebooks/08_evidence_grounded_biological_reasoning.ipynb
- results/phase6/selected_marker_genes.csv
- results/phase7/evidence_reuse_report.csv
- results/phase7/literature_summary.csv
- results/phase7/phase7_coverage_summary.csv
- results/phase7/phase7_validation_report.json
- results/phase7/references.csv
- results/phase8/all_clusters_summary.csv
- results/tables/classification_model_comparison.csv
- results/tables/leiden_9_cell_type_annotations.csv

## Key visual findings

- The largest cluster is C2 (IL7R+ memory/helper T cells; 602 cells, 22.8%).
- The smallest cluster is C8 (Platelets; 11 cells, 0.4%).
- XGBoost remains the Phase 5 validation-selected classifier; Phase 9 does not reinterpret the selection using held-out test metrics.
- Phase 8 reports 9 validation passes and 0 failures.

## Missing-data limitations

- unhashable type: 'list'
- Phase 5 did not save held-out true labels and predictions. Regenerating the split or retraining/rerunning a classifier is prohibited, so counts and normalized confusion matrices cannot be produced without fabrication.

## Output paths

- `results/phase9/biological_reasoning_summary.csv`
- `results/phase9/cell_type_color_mapping.json`
- `results/phase9/cluster_composition.csv`
- `results/phase9/figure_10_cluster_summary_table.pdf`
- `results/phase9/figure_10_cluster_summary_table.png`
- `results/phase9/figure_1_annotated_umap.pdf`
- `results/phase9/figure_1_annotated_umap.png`
- `results/phase9/figure_1_annotated_umap.svg`
- `results/phase9/figure_2_cluster_cell_counts.png`
- `results/phase9/figure_2_cluster_percentages.png`
- `results/phase9/figure_3_marker_gene_heatmap.pdf`
- `results/phase9/figure_3_marker_gene_heatmap.png`
- `results/phase9/figure_3_marker_gene_heatmap.svg`
- `results/phase9/figure_4_marker_specificity.png`
- `results/phase9/figure_5_model_comparison.pdf`
- `results/phase9/figure_5_model_comparison.png`
- `results/phase9/figure_5_model_comparison.svg`
- `results/phase9/figure_7_biological_reasoning_summary.png`
- `results/phase9/figure_8_evidence_validation_overview.png`
- `results/phase9/figure_9_complete_pipeline.pdf`
- `results/phase9/figure_9_complete_pipeline.png`
- `results/phase9/figure_9_complete_pipeline.svg`
- `results/phase9/figure_manifest.csv`
- `results/phase9/final_cluster_summary.csv`
- `results/phase9/marker_gene_heatmap_matrix.csv`
- `results/phase9/marker_specificity_summary.csv`
- `results/phase9/model_comparison_summary.csv`
- `results/phase9/visualization_summary.md`
