# Biological Interpretation Report — Cluster 7

## Annotation assessment

- **Proposed cell type:** Naive/resting T cells
- **Support level:** partially supported
- **Supporting genes:** CCR7, CD3D, CD7, CD3E, PIK3IP1, LEF1, NOSIP
- **Supporting evidence:** DATASET OBSERVATION: the highest-ranked markers are CCR7, CD3D, LDHB, PRKCQ-AS1, NOSIP, and the full representative set is enriched relative to cells outside this cluster. LITERATURE-SUPPORTED FACT: the supplied gene-level publications provide the module-specific contexts cited below (PMID:35281921, PMID:40513067, PMID:41321019, PMID:16264327, PMID:33283362, PMID:35712757, PMID:35570001, PMID:35710869). BIOLOGICAL INFERENCE: the combined pattern partially supports the proposed Naive/resting T cells annotation, while no single supplied marker is treated as unique.

### Alternative interpretations

- A broader T-cell state without a resolved naive/resting designation remains plausible.
- A memory-like T-cell state remains plausible because the supplied evidence does not uniquely separate naive, resting, and memory contexts.

### Additional evidence needed

- Protein-level measurements for the supplied representative genes.
- A cluster-level classification prediction or probability.
- Independent PBMC data showing that the complete supplied marker pattern is reproducible.
- Functional measurements that directly test the inferred biological program.

## Strongest dataset observations

- **CCR7** — DATASET OBSERVATION: CCR7 has rank 1, average log2 fold change 2.896683, adjusted p-value 1.762786e-44, expression prevalence 0.540000 inside versus 0.125686 outside the cluster, and marker score 24.002754. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **CD3D** — DATASET OBSERVATION: CD3D has rank 2, average log2 fold change 1.829257, adjusted p-value 1.505187e-39, expression prevalence 0.860000 inside versus 0.450183 outside the cluster, and marker score 14.993219. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **LDHB** — DATASET OBSERVATION: LDHB has rank 3, average log2 fold change 1.895979, adjusted p-value 1.378755e-73, expression prevalence 0.953333 inside versus 0.617916 outside the cluster, and marker score 12.718891. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **PRKCQ-AS1** — DATASET OBSERVATION: PRKCQ-AS1 has rank 4, average log2 fold change 2.213363, adjusted p-value 1.508665e-19, expression prevalence 0.397778 inside versus 0.121572 outside the cluster, and marker score 11.506337. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **NOSIP** — DATASET OBSERVATION: NOSIP has rank 5, average log2 fold change 1.706754, adjusted p-value 2.413143e-35, expression prevalence 0.691111 inside versus 0.375229 outside the cluster, and marker score 10.782675. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.

## Functional modules

### T-cell identity module

- **Genes:** CD3D, CD3E, CD7
- **Confidence:** High — Confidence is High because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: CD3D (pct_in=0.860000, pct_out=0.450183, avg_log2FC=1.829257, marker_score=14.993219), CD3E (pct_in=0.764444, pct_out=0.428245, avg_log2FC=1.550029, marker_score=10.422377), CD7 (pct_in=0.642222, pct_out=0.311243, avg_log2FC=1.604004, marker_score=10.617835). CD3D has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied references connect CD3D and CD3E with T-cell development and discuss CD7 in T-cell contexts.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the t-cell identity module interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:16264327, PMID:33283362, PMID:35712757, PMID:35570001, PMID:35710869, PMID:28539325, PMID:40771729, PMID:41290542
### Trafficking and restrained T-cell-state module

- **Genes:** CCR7, PIK3IP1, LEF1, NOSIP
- **Confidence:** Moderate — Confidence is Moderate because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: CCR7 (pct_in=0.540000, pct_out=0.125686, avg_log2FC=2.896683, marker_score=24.002754), PIK3IP1 (pct_in=0.486667, pct_out=0.203382, avg_log2FC=1.766211, marker_score=10.006806), LEF1 (pct_in=0.364444, pct_out=0.124314, avg_log2FC=2.001486, marker_score=6.784429), NOSIP (pct_in=0.691111, pct_out=0.375229, avg_log2FC=1.706754, marker_score=10.782675). CCR7 has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied references discuss CCR7 in T-cell trafficking contexts, PIK3IP1 in inhibition of T-cell activation, LEF1 in early T-cell development, and NOSIP in persistent T-cell contexts.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the trafficking and restrained t-cell-state module interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:35281921, PMID:40513067, PMID:41321019, PMID:34127847, PMID:38589618, PMID:42385703, PMID:33782480, PMID:35660746, PMID:42440569, PMID:22706993, PMID:33024547, PMID:41571844
### Additional cellular-context module

- **Genes:** LDHB, PRKCQ-AS1, C6orf48
- **Confidence:** Low — Confidence is Low because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: LDHB (pct_in=0.953333, pct_out=0.617916, avg_log2FC=1.895979, marker_score=12.718891), PRKCQ-AS1 (pct_in=0.397778, pct_out=0.121572, avg_log2FC=2.213363, marker_score=11.506337), C6orf48 (pct_in=0.755556, pct_out=0.502285, avg_log2FC=1.339001, marker_score=6.782583). LDHB has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied references discuss these genes in publication-specific metabolic, regulatory, or transcriptomic contexts, but direct evidence for a shared resting-state mechanism is limited.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the additional cellular-context module interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:15962222, PMID:38246423, PMID:41455820, PMID:36090994, PMID:38326896, PMID:39731912, PMID:38229689, PMID:38243290, PMID:40433053

## Coordinated biological program

BIOLOGICAL INFERENCE: the modules jointly support the proposed Naive/resting T cells interpretation by combining the dominant identity-associated marker pattern with secondary state or contextual signals. The modules are coordinated at the level of co-enrichment in this cluster; the supplied evidence does not establish causal interaction among them.

## Supported conclusions

- DATASET OBSERVATION: all structured gene claims use only the ten supplied representative genes for this cluster.
- DATASET OBSERVATION: the highest-ranked genes combine fold-change, prevalence, specificity, statistical significance, and marker-score evidence.
- LITERATURE-SUPPORTED FACT: the cited references are the supplied verified gene-level references and are limited to their publication-specific contexts.
- BIOLOGICAL INFERENCE: the combined marker pattern partially supports the proposed Naive/resting T cells annotation.

## Reasonable inferences

- BIOLOGICAL INFERENCE: co-enrichment of several annotation-associated markers is more informative than any single marker considered alone.
- BIOLOGICAL INFERENCE: the highest-confidence module is the dominant biological program represented in the supplied marker set.
- BIOLOGICAL INFERENCE: lower-confidence modules may describe context or state, but their functional contribution is unresolved.

## Weak or uncertain interpretations

- UNKNOWN OR UNCERTAIN: transcript enrichment does not establish protein abundance or functional activity.
- UNKNOWN OR UNCERTAIN: publication findings from other biological settings may not transfer directly to this PBMC3K cluster.
- UNKNOWN OR UNCERTAIN: the supplied evidence does not establish that every cell in the cluster has the same state.
- The supplied evidence is insufficient to determine one uniquely defined functional state.

## Contradictory evidence

- No supplied result directly disproves the proposed annotation, but the literature summaries repeatedly state that gene contexts are not unique to one cell type.
- Several supplied references are contextual, computational, review-based, or indirect, which limits mechanistic interpretation.

## Limitations

- Only the ten supplied representative genes are interpreted.
- Held-out per-class model metrics are not a cluster-level probability.
- Transcript measurements do not establish protein abundance, localization, or functional activity.
- Evidence grades describe the selected publications and do not make every reported mechanism universal.
- The supplied evidence is insufficient to determine causal relationships among the modules.

## Overall confidence

**Moderate** — Overall confidence is Moderate because the annotation assessment is partially supported, the marker statistics provide direct dataset support, and verified references provide gene-level context. Confidence is limited by non-unique gene contexts, absence of a cluster-level model probability, and lack of direct functional measurements.

## Plain-language explanation

The measured gene pattern is most consistent with Naive/resting T cells. The strongest genes are enriched within this cluster, and the supplied publications provide context for the grouped biological modules. Some genes can occur in other cell types or states, and gene expression alone does not show that the inferred functions occurred. The supplied evidence is insufficient to determine one uniquely defined functional state.
