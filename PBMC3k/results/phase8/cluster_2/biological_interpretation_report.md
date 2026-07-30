# Biological Interpretation Report — Cluster 2

## Annotation assessment

- **Proposed cell type:** IL7R+ memory/helper T cells
- **Support level:** partially supported
- **Supporting genes:** IL7R, CD3D, CD3E, CD2, TRAT1, LTB
- **Supporting evidence:** DATASET OBSERVATION: the highest-ranked markers are IL32, IL7R, CD3D, LTB, CD3E, and the full representative set is enriched relative to cells outside this cluster. LITERATURE-SUPPORTED FACT: the supplied gene-level publications provide the module-specific contexts cited below (PMID:2482743, PMID:7693022, PMID:37798328, PMID:16264327, PMID:33283362, PMID:35712757, PMID:35570001, PMID:35710869). BIOLOGICAL INFERENCE: the combined pattern partially supports the proposed IL7R+ memory/helper T cells annotation, while no single supplied marker is treated as unique.

### Alternative interpretations

- A broader T-cell state without a resolved memory/helper designation remains plausible.
- An IL7R-associated lymphocyte state remains plausible because the supplied IL7R evidence is not unique to memory/helper T cells.

### Additional evidence needed

- Protein-level measurements for the supplied representative genes.
- A cluster-level classification prediction or probability.
- Independent PBMC data showing that the complete supplied marker pattern is reproducible.
- Functional measurements that directly test the inferred biological program.

## Strongest dataset observations

- **IL32** — DATASET OBSERVATION: IL32 has rank 1, average log2 fold change 2.521231, adjusted p-value 7.213826e-91, expression prevalence 0.933555 inside versus 0.439587 outside the cluster, and marker score 24.908120. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **IL7R** — DATASET OBSERVATION: IL7R has rank 2, average log2 fold change 2.425345, adjusted p-value 1.521022e-74, expression prevalence 0.764120 inside versus 0.295678 outside the cluster, and marker score 22.722657. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **CD3D** — DATASET OBSERVATION: CD3D has rank 3, average log2 fold change 2.239499, adjusted p-value 1.647630e-73, expression prevalence 0.906977 inside versus 0.405697 outside the cluster, and marker score 22.452293. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **LTB** — DATASET OBSERVATION: LTB has rank 4, average log2 fold change 2.441446, adjusted p-value 3.179300e-104, expression prevalence 0.980066 inside versus 0.622299 outside the cluster, and marker score 17.469413. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **CD3E** — DATASET OBSERVATION: CD3E has rank 5, average log2 fold change 1.974084, adjusted p-value 8.421711e-60, expression prevalence 0.823920 inside versus 0.385560 outside the cluster, and marker score 17.307204. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.

## Functional modules

### T-cell identity and signaling module

- **Genes:** CD3D, CD3E, CD2, TRAT1
- **Confidence:** High — Confidence is High because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: CD3D (pct_in=0.906977, pct_out=0.405697, avg_log2FC=2.239499, marker_score=22.452293), CD3E (pct_in=0.823920, pct_out=0.385560, avg_log2FC=1.974084, marker_score=17.307204), CD2 (pct_in=0.624585, pct_out=0.227898, avg_log2FC=2.075754, marker_score=16.468491), TRAT1 (pct_in=0.408638, pct_out=0.103635, avg_log2FC=2.327359, marker_score=14.197043). CD3D has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied references connect CD3D, CD3E, CD2, and TRAT1 with T-cell development, recognition, adhesion, or signaling contexts.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the t-cell identity and signaling module interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:2482743, PMID:7693022, PMID:37798328, PMID:16264327, PMID:33283362, PMID:35712757, PMID:35570001, PMID:35710869, PMID:36184729, PMID:41074026, PMID:41076046
### IL7R-associated memory/helper context module

- **Genes:** IL7R, LTB, IL32
- **Confidence:** Moderate — Confidence is Moderate because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: IL7R (pct_in=0.764120, pct_out=0.295678, avg_log2FC=2.425345, marker_score=22.722657), LTB (pct_in=0.980066, pct_out=0.622299, avg_log2FC=2.441446, marker_score=17.469413), IL32 (pct_in=0.933555, pct_out=0.439587, avg_log2FC=2.521231, marker_score=24.908120). IL32 has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied references discuss IL7R in lymphocyte contexts, LTB in memory T-cell contexts, and IL32 in publication-specific inflammatory transcriptomic contexts.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the il7r-associated memory/helper context module interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:39435643, PMID:40330458, PMID:40997225, PMID:38956225, PMID:39982469, PMID:40993240, PMID:33748804, PMID:41241792
### Cellular transport and metabolic context module

- **Genes:** AQP3, LDHB, SPOCK2
- **Confidence:** Low — Confidence is Low because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: AQP3 (pct_in=0.406977, pct_out=0.096267, avg_log2FC=2.529479, marker_score=15.718668), LDHB (pct_in=0.958472, pct_out=0.591356, avg_log2FC=1.990060, marker_score=14.611665), SPOCK2 (pct_in=0.438538, pct_out=0.141454, avg_log2FC=2.015473, marker_score=11.975311). AQP3 has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied references discuss these genes in transport, metabolic, or publication-specific cellular contexts, but direct evidence for a shared function in this cluster is limited.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the cellular transport and metabolic context module interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:36010640, PMID:38279209, PMID:38726865, PMID:36090994, PMID:38326896, PMID:39731912, PMID:37165378, PMID:39115722, PMID:39741186

## Coordinated biological program

BIOLOGICAL INFERENCE: the modules jointly support the proposed IL7R+ memory/helper T cells interpretation by combining the dominant identity-associated marker pattern with secondary state or contextual signals. The modules are coordinated at the level of co-enrichment in this cluster; the supplied evidence does not establish causal interaction among them.

## Supported conclusions

- DATASET OBSERVATION: all structured gene claims use only the ten supplied representative genes for this cluster.
- DATASET OBSERVATION: the highest-ranked genes combine fold-change, prevalence, specificity, statistical significance, and marker-score evidence.
- LITERATURE-SUPPORTED FACT: the cited references are the supplied verified gene-level references and are limited to their publication-specific contexts.
- BIOLOGICAL INFERENCE: the combined marker pattern partially supports the proposed IL7R+ memory/helper T cells annotation.

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

The measured gene pattern is most consistent with IL7R+ memory/helper T cells. The strongest genes are enriched within this cluster, and the supplied publications provide context for the grouped biological modules. Some genes can occur in other cell types or states, and gene expression alone does not show that the inferred functions occurred. The supplied evidence is insufficient to determine one uniquely defined functional state.
