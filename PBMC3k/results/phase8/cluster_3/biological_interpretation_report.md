# Biological Interpretation Report — Cluster 3

## Annotation assessment

- **Proposed cell type:** Classical monocytes
- **Support level:** strongly supported
- **Supporting genes:** S100A8, LGALS2, S100A9, FCN1, CST3, TYROBP, CD14, MS4A6A, LST1, AIF1
- **Supporting evidence:** DATASET OBSERVATION: the highest-ranked markers are S100A8, LGALS2, S100A9, FCN1, CST3, and the full representative set is enriched relative to cells outside this cluster. LITERATURE-SUPPORTED FACT: the supplied gene-level publications provide the module-specific contexts cited below (PMID:38898508, PMID:40325180, PMID:41448409, PMID:30105020, PMID:34279540, PMID:40023733, PMID:37854583, PMID:40925202). BIOLOGICAL INFERENCE: the combined pattern strongly supports the proposed Classical monocytes annotation, while no single supplied marker is treated as unique.

### Alternative interpretations

- A related inflammatory myeloid-cell state remains possible because several supplied gene contexts are not unique to classical monocytes.
- A broader monocyte interpretation without a resolved classical state remains possible.

### Additional evidence needed

- Protein-level measurements for the supplied representative genes.
- A cluster-level classification prediction or probability.
- Independent PBMC data showing that the complete supplied marker pattern is reproducible.
- Functional measurements that directly test the inferred biological program.

## Strongest dataset observations

- **S100A8** — DATASET OBSERVATION: S100A8 has rank 1, average log2 fold change 7.360887, adjusted p-value 7.621623e-225, expression prevalence 0.942231 inside versus 0.120318 outside the cluster, and marker score 121.000134. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **LGALS2** — DATASET OBSERVATION: LGALS2 has rank 2, average log2 fold change 7.016551, adjusted p-value 2.403732e-211, expression prevalence 0.908367 inside versus 0.050562 outside the cluster, and marker score 120.376605. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **S100A9** — DATASET OBSERVATION: S100A9 has rank 3, average log2 fold change 7.183323, adjusted p-value 2.211534e-238, expression prevalence 0.976096 inside versus 0.212079 outside the cluster, and marker score 109.763619. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **FCN1** — DATASET OBSERVATION: FCN1 has rank 4, average log2 fold change 5.470355, adjusted p-value 1.143427e-201, expression prevalence 0.936255 inside versus 0.146067 outside the cluster, and marker score 86.452124. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **CST3** — DATASET OBSERVATION: CST3 has rank 5, average log2 fold change 5.857136, adjusted p-value 2.283287e-223, expression prevalence 0.992032 inside versus 0.258427 outside the cluster, and marker score 85.936477. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.

## Functional modules

### Inflammatory classical-monocyte marker module

- **Genes:** S100A8, S100A9, FCN1, CD14, LGALS2
- **Confidence:** High — Confidence is High because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: S100A8 (pct_in=0.942231, pct_out=0.120318, avg_log2FC=7.360887, marker_score=121.000134), S100A9 (pct_in=0.976096, pct_out=0.212079, avg_log2FC=7.183323, marker_score=109.763619), FCN1 (pct_in=0.936255, pct_out=0.146067, avg_log2FC=5.470355, marker_score=86.452124), CD14 (pct_in=0.641434, pct_out=0.027154, avg_log2FC=6.178094, marker_score=75.901679), LGALS2 (pct_in=0.908367, pct_out=0.050562, avg_log2FC=7.016551, marker_score=120.376605). S100A8 has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied references discuss these genes in monocyte, myeloid, inflammatory, or innate immune contexts.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the inflammatory classical-monocyte marker module interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:30105020, PMID:34279540, PMID:40023733, PMID:38262391, PMID:39139822, PMID:39171604, PMID:19330599, PMID:36499335, PMID:39350165, PMID:27492899, PMID:38776909, PMID:39929053, PMID:32434457, PMID:38013255, PMID:39266214
### Myeloid signaling and effector-context module

- **Genes:** TYROBP, LST1, AIF1, MS4A6A
- **Confidence:** Moderate — Confidence is Moderate because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: TYROBP (pct_in=0.994024, pct_out=0.257491, avg_log2FC=5.471521, marker_score=80.599145), LST1 (pct_in=0.958167, pct_out=0.215356, avg_log2FC=4.502578, marker_score=66.891337), AIF1 (pct_in=0.958167, pct_out=0.237360, avg_log2FC=4.549419, marker_score=65.585132), MS4A6A (pct_in=0.681275, pct_out=0.035581, avg_log2FC=5.854212, marker_score=75.600639). TYROBP has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied references place these genes in myeloid-cell or innate immune publication contexts, while not establishing uniqueness to one monocyte state.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the myeloid signaling and effector-context module interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:38898508, PMID:40325180, PMID:41448409, PMID:16362817, PMID:24816991, PMID:41488617, PMID:30906402, PMID:40090082, PMID:41515934, PMID:36002854, PMID:39508103, PMID:40301889
### Protease-regulatory context module

- **Genes:** CST3
- **Confidence:** Moderate — Confidence is Moderate because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: CST3 (pct_in=0.992032, pct_out=0.258427, avg_log2FC=5.857136, marker_score=85.936477). CST3 has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied references discuss CST3 in publication-specific protease-regulatory and immune contexts.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the protease-regulatory context module interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:37854583, PMID:40925202, PMID:41167578

## Coordinated biological program

BIOLOGICAL INFERENCE: the modules jointly support the proposed Classical monocytes interpretation by combining the dominant identity-associated marker pattern with secondary state or contextual signals. The modules are coordinated at the level of co-enrichment in this cluster; the supplied evidence does not establish causal interaction among them.

## Supported conclusions

- DATASET OBSERVATION: all structured gene claims use only the ten supplied representative genes for this cluster.
- DATASET OBSERVATION: the highest-ranked genes combine fold-change, prevalence, specificity, statistical significance, and marker-score evidence.
- LITERATURE-SUPPORTED FACT: the cited references are the supplied verified gene-level references and are limited to their publication-specific contexts.
- BIOLOGICAL INFERENCE: the combined marker pattern strongly supports the proposed Classical monocytes annotation.

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

**High** — Overall confidence is High because the annotation assessment is strongly supported, the marker statistics provide direct dataset support, and verified references provide gene-level context. Confidence is limited by non-unique gene contexts, absence of a cluster-level model probability, and lack of direct functional measurements.

## Plain-language explanation

The measured gene pattern is most consistent with Classical monocytes. The strongest genes are enriched within this cluster, and the supplied publications provide context for the grouped biological modules. Some genes can occur in other cell types or states, and gene expression alone does not show that the inferred functions occurred. The supplied evidence is insufficient to determine one uniquely defined functional state.
