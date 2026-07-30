# Biological Interpretation Report — Cluster 6

## Annotation assessment

- **Proposed cell type:** Activated/transitional T cells
- **Support level:** partially supported
- **Supporting genes:** CCL5, IL32, CD3D
- **Supporting evidence:** DATASET OBSERVATION: the highest-ranked markers are CCL5, IL32, CD3D, RPL23A, RPS3, and the full representative set is enriched relative to cells outside this cluster. LITERATURE-SUPPORTED FACT: the supplied gene-level publications provide the module-specific contexts cited below (PMID:34514075, PMID:38797830, PMID:40397747, PMID:16264327, PMID:33283362, PMID:35712757, PMID:39435643, PMID:40330458). BIOLOGICAL INFERENCE: the combined pattern partially supports the proposed Activated/transitional T cells annotation, while no single supplied marker is treated as unique.

### Alternative interpretations

- A broader T-cell cluster without a resolved activated or transitional state remains plausible.
- A technically dominated T-cell cluster remains plausible because most representative genes have minimal specificity.

### Additional evidence needed

- Protein-level measurements for the supplied representative genes.
- A cluster-level classification prediction or probability.
- Independent PBMC data showing that the complete supplied marker pattern is reproducible.
- Functional measurements that directly test the inferred biological program.

## Strongest dataset observations

- **CCL5** — DATASET OBSERVATION: CCL5 has rank 1, average log2 fold change 2.067858, adjusted p-value 3.022016e-05, expression prevalence 0.523438 inside versus 0.305976 outside the cluster, and marker score 2.032417. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **IL32** — DATASET OBSERVATION: IL32 has rank 2, average log2 fold change 1.377941, adjusted p-value 2.033227e-06, expression prevalence 0.765625 inside versus 0.541434 outside the cluster, and marker score 1.758324. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **CD3D** — DATASET OBSERVATION: CD3D has rank 3, average log2 fold change 1.333352, adjusted p-value 6.311240e-07, expression prevalence 0.718750 inside versus 0.509960 outside the cluster, and marker score 1.725988. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **RPL23A** — DATASET OBSERVATION: RPL23A has rank 4, average log2 fold change 0.424583, adjusted p-value 1.431692e-04, expression prevalence 1.000000 inside versus 0.990837 outside the cluster, and marker score 0.014956. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **RPS3** — DATASET OBSERVATION: RPS3 has rank 5, average log2 fold change 0.475426, adjusted p-value 2.874728e-07, expression prevalence 1.000000 inside versus 0.995618 outside the cluster, and marker score 0.013629. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.

## Functional modules

### T-cell-associated marker module

- **Genes:** CCL5, IL32, CD3D
- **Confidence:** Moderate — Confidence is Moderate because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: CCL5 (pct_in=0.523438, pct_out=0.305976, avg_log2FC=2.067858, marker_score=2.032417), IL32 (pct_in=0.765625, pct_out=0.541434, avg_log2FC=1.377941, marker_score=1.758324), CD3D (pct_in=0.718750, pct_out=0.509960, avg_log2FC=1.333352, marker_score=1.725988). CCL5 has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied references discuss CD3D in T-cell contexts and CCL5 and IL32 in publication-specific immune contexts.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the t-cell-associated marker module interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:34514075, PMID:38797830, PMID:40397747, PMID:16264327, PMID:33283362, PMID:35712757, PMID:39435643, PMID:40330458, PMID:40997225
### Ribosomal-gene expression module

- **Genes:** RPL23A, RPS3, RPS12, RPS25, RPS14, RPL13
- **Confidence:** Low — Confidence is Low because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: RPL23A (pct_in=1.000000, pct_out=0.990837, avg_log2FC=0.424583, marker_score=0.014956), RPS3 (pct_in=1.000000, pct_out=0.995618, avg_log2FC=0.475426, marker_score=0.013629), RPS12 (pct_in=1.000000, pct_out=0.993227, avg_log2FC=0.389514, marker_score=0.007775), RPS25 (pct_in=0.984375, pct_out=0.980876, avg_log2FC=0.439362, marker_score=0.006043), RPS14 (pct_in=1.000000, pct_out=0.995618, avg_log2FC=0.326824, marker_score=0.004692), RPL13 (pct_in=1.000000, pct_out=0.997211, avg_log2FC=0.355120, marker_score=0.003637). RPL23A has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied references discuss these genes individually in publication-specific contexts but do not establish a shared activation mechanism in this cluster.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the ribosomal-gene expression module interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:40565588, PMID:40764361, PMID:41779063, PMID:37400220, PMID:37864923, PMID:42311670, PMID:37272618, PMID:41261408, PMID:20980806, PMID:32571542, PMID:34432872, PMID:28260789, PMID:35766008, PMID:29608488, PMID:37087770, PMID:40023134
### Broad transcript-associated context module

- **Genes:** MALAT1
- **Confidence:** Low — Confidence is Low because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: MALAT1 (pct_in=1.000000, pct_out=0.999602, avg_log2FC=0.902251, marker_score=0.006643). MALAT1 has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied references discuss MALAT1 in publication-specific cellular contexts; they do not establish an activated or transitional T-cell mechanism here.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the broad transcript-associated context module interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:35473929, PMID:38087169, PMID:38493144

## Coordinated biological program

BIOLOGICAL INFERENCE: the modules jointly support the proposed Activated/transitional T cells interpretation by combining the dominant identity-associated marker pattern with secondary state or contextual signals. The modules are coordinated at the level of co-enrichment in this cluster; the supplied evidence does not establish causal interaction among them.

## Supported conclusions

- DATASET OBSERVATION: all structured gene claims use only the ten supplied representative genes for this cluster.
- DATASET OBSERVATION: the highest-ranked genes combine fold-change, prevalence, specificity, statistical significance, and marker-score evidence.
- LITERATURE-SUPPORTED FACT: the cited references are the supplied verified gene-level references and are limited to their publication-specific contexts.
- BIOLOGICAL INFERENCE: the combined marker pattern partially supports the proposed Activated/transitional T cells annotation.

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

**Low** — Overall confidence is Low because the annotation assessment is partially supported, the marker statistics provide direct dataset support, and verified references provide gene-level context. Confidence is limited by non-unique gene contexts, absence of a cluster-level model probability, and lack of direct functional measurements.

## Plain-language explanation

The measured gene pattern is most consistent with Activated/transitional T cells. The strongest genes are enriched within this cluster, and the supplied publications provide context for the grouped biological modules. Some genes can occur in other cell types or states, and gene expression alone does not show that the inferred functions occurred. The supplied evidence is insufficient to determine one uniquely defined functional state.
