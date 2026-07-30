# Cluster 5: NK cells

## Assigned Cell Type

NK cells (Notebook 04 annotation confidence: high).

## Number of Cells

153 of 2,638 cells (5.8%).

## Top Marker Genes

`GZMB`, `FGFBP2`, `GNLY`, `PRF1`, `NKG7`, `CST7`, `SPON2`, `GZMA`, `CCL4`, `CTSW`

## Marker Ranking Table

| Rank | Gene | avg_log2FC | Adjusted p | pct_in | pct_out | Specificity | Marker score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | GZMB | 7.891 | 4.62e-85 | 0.974 | 0.068 | 0.906 | 142.959 |
| 2 | FGFBP2 | 6.923 | 1.18e-70 | 0.895 | 0.062 | 0.834 | 115.462 |
| 3 | GNLY | 7.359 | 2.05e-72 | 0.915 | 0.135 | 0.780 | 114.827 |
| 4 | PRF1 | 6.527 | 9.81e-83 | 0.967 | 0.106 | 0.861 | 112.412 |
| 5 | NKG7 | 6.985 | 4.39e-88 | 1.000 | 0.256 | 0.744 | 104.006 |
| 6 | CST7 | 5.520 | 6.50e-76 | 0.967 | 0.149 | 0.818 | 90.354 |
| 7 | SPON2 | 6.330 | 5.11e-48 | 0.739 | 0.039 | 0.699 | 88.511 |
| 8 | GZMA | 5.479 | 2.62e-74 | 0.954 | 0.151 | 0.803 | 88.033 |
| 9 | CCL4 | 5.431 | 4.90e-45 | 0.745 | 0.075 | 0.670 | 72.808 |
| 10 | CTSW | 4.689 | 1.01e-75 | 0.987 | 0.257 | 0.730 | 68.444 |

## What Makes This Cluster Different?

The selected markers have a median within-cluster expression fraction of 0.961 and a median specificity difference of 0.792. The top-ranked gene, GZMB, is detected in 97.4% of this cluster versus 6.8% outside it, with an average log2 fold change of 7.89. Across the full selected panel, positive fold changes, adjusted significance, broad within-cluster detection, and higher expression prevalence inside the cluster jointly distinguish this group; the conclusion does not rely on fold change alone.

## Biological Interpretation

The coordinated high and cluster-specific expression of cytotoxic-effector genes such as GNLY, GZMB, PRF1, NKG7, and FGFBP2 suggests that these cells are equipped for rapid target-cell killing. In this dataset, that expression program supports the assigned NK-cell identity and distinguishes the cluster from the T-cell clusters, even where shared genes such as NKG7 or CCL5 occur.

This is a dataset-grounded interpretation, not a literature-supported conclusion. No external sources were used in this notebook.

## Questions for Future Literature Search

- What is the biological function of GZMB?
- Is GZMB a known marker of NK cells?
- Which immune pathways involve GZMB?
- Has GZMB been associated with diseases, and in what experimental contexts?
- What is the biological function of FGFBP2?
- Is FGFBP2 a known marker of NK cells?
- Which immune pathways involve FGFBP2?
- Has FGFBP2 been associated with diseases, and in what experimental contexts?
- What is the biological function of GNLY?
- Is GNLY a known marker of NK cells?
- Which immune pathways involve GNLY?
- Has GNLY been associated with diseases, and in what experimental contexts?
- What is the biological function of PRF1?
- Is PRF1 a known marker of NK cells?
- Which immune pathways involve PRF1?
- Has PRF1 been associated with diseases, and in what experimental contexts?

## Limitations

This single PBMC3k expression dataset and its unsupervised clusters cannot determine:

- disease diagnosis;
- donor identity;
- race;
- ethnicity;
- personality.

Cluster labels and biological interpretations are analytical assignments, not direct measurements of those traits. The smallest populations are especially sensitive to sampling variability, and marker expression can overlap across related immune-cell states.
