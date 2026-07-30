# Biological Interpretation Report — Cluster 0

## Annotation assessment

- **Proposed cell type:** Cytotoxic CD8 T cells
- **Support level:** strongly supported
- **Supporting genes:** NKG7, CCL5, GZMA, CST7, GZMK, CTSW, CD8A, GZMH, KLRG1
- **Supporting evidence:** DATASET OBSERVATION: the highest-ranked markers are NKG7, CCL5, GZMA, CST7, GZMK, and the full representative set is enriched relative to cells outside this cluster. LITERATURE-SUPPORTED FACT: the supplied gene-level publications provide the module-specific contexts cited below (PMID:34514075, PMID:38797830, PMID:40397747, PMID:38348045, PMID:39694280, PMID:40769312, PMID:18256700, PMID:34189679). BIOLOGICAL INFERENCE: the combined pattern strongly supports the proposed Cytotoxic CD8 T cells annotation, while no single supplied marker is treated as unique.

### Alternative interpretations

- An NK-cell-like cytotoxic lymphocyte interpretation remains plausible because the supplied evidence places NKG7 and CTSW in both NK-cell and cytotoxic T-cell contexts.
- A GZMK-expressing CD8 T-cell state with less uniform cytotoxic character remains plausible.

### Additional evidence needed

- Protein-level measurements for the supplied representative genes.
- A cluster-level classification prediction or probability.
- Independent PBMC data showing that the complete supplied marker pattern is reproducible.
- Functional measurements that directly test the inferred biological program.

## Strongest dataset observations

- **NKG7** — DATASET OBSERVATION: NKG7 has rank 1, average log2 fold change 5.149965, adjusted p-value 2.524331e-104, expression prevalence 0.959707 inside versus 0.222410 outside the cluster, and marker score 75.941055. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **CCL5** — DATASET OBSERVATION: CCL5 has rank 2, average log2 fold change 5.365429, adjusted p-value 2.447579e-111, expression prevalence 0.945055 inside versus 0.243975 outside the cluster, and marker score 75.231933. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **GZMA** — DATASET OBSERVATION: GZMA has rank 3, average log2 fold change 4.028471, adjusted p-value 5.997373e-68, expression prevalence 0.787546 inside versus 0.129387 outside the cluster, and marker score 53.027480. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **CST7** — DATASET OBSERVATION: CST7 has rank 4, average log2 fold change 4.054892, adjusted p-value 1.801775e-67, expression prevalence 0.776557 inside versus 0.129387 outside the cluster, and marker score 52.484075. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.
- **GZMK** — DATASET OBSERVATION: GZMK has rank 5, average log2 fold change 4.834554, adjusted p-value 1.209201e-45, expression prevalence 0.586081 inside versus 0.058351 outside the cluster, and marker score 51.026748. Importance: This is one of the strongest measured cluster observations by rank, enrichment, prevalence, statistical significance, and marker score.

## Functional modules

### Cytotoxic granule and effector-protease module

- **Genes:** NKG7, GZMA, CST7, CTSW, GZMH
- **Confidence:** High — Confidence is High because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: NKG7 (pct_in=0.959707, pct_out=0.222410, avg_log2FC=5.149965, marker_score=75.941055), GZMA (pct_in=0.787546, pct_out=0.129387, avg_log2FC=4.028471, marker_score=53.027480), CST7 (pct_in=0.776557, pct_out=0.129387, avg_log2FC=4.054892, marker_score=52.484075), CTSW (pct_in=0.820513, pct_out=0.239323, avg_log2FC=3.365193, marker_score=39.116288), GZMH (pct_in=0.417582, pct_out=0.063425, avg_log2FC=3.894171, marker_score=26.998483). NKG7 has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied evidence connects these genes with cytotoxic granules, regulated protease functions, or cytotoxic-lymphocyte contexts.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the cytotoxic granule and effector-protease module interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:18256700, PMID:34189679, PMID:38879499, PMID:15087452, PMID:19100676, PMID:38891048, PMID:32093590, PMID:32299851, PMID:36792800, PMID:40970118, PMID:40974256, PMID:41740930, PMID:32839608, PMID:34911739, PMID:35013002
### CD8 T-cell identity and state module

- **Genes:** CD8A, GZMK, KLRG1
- **Confidence:** Moderate — Confidence is Moderate because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: CD8A (pct_in=0.509158, pct_out=0.072727, avg_log2FC=3.730852, marker_score=32.565132), GZMK (pct_in=0.586081, pct_out=0.058351, avg_log2FC=4.834554, marker_score=51.026748), KLRG1 (pct_in=0.450549, pct_out=0.076110, avg_log2FC=3.330793, marker_score=24.943613). GZMK has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied publications place these genes in T-cell contexts, while also showing that their contexts are not unique to one T-cell state.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the cd8 t-cell identity and state module interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:38348045, PMID:39694280, PMID:40769312, PMID:33271118, PMID:39814882, PMID:40651883, PMID:38252421, PMID:39658611, PMID:40307497
### Immune-cell communication module

- **Genes:** CCL5
- **Confidence:** Moderate — Confidence is Moderate because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: CCL5 (pct_in=0.945055, pct_out=0.243975, avg_log2FC=5.365429, marker_score=75.231933). CCL5 has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied evidence discusses CCL5 in inflammatory responses and immune-cell communication contexts.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the immune-cell communication module interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:34514075, PMID:38797830, PMID:40397747
### Contextual cellular-regulation signal

- **Genes:** LYAR
- **Confidence:** Low — Confidence is Low because the dataset enrichment is directly measured, whereas transfer of the supplied publication contexts to this cluster remains limited by context and by the evidence grades.
- **Dataset support:** DATASET OBSERVATION: LYAR (pct_in=0.589744, pct_out=0.135307, avg_log2FC=3.081434, marker_score=28.006359). LYAR has the highest marker score within this module.
- **Literature support:** LITERATURE-SUPPORTED FACT: The supplied references discuss LYAR in cell-growth and transcriptomic contexts but do not establish a direct immune role in this cluster.
- **Biological inference:** BIOLOGICAL INFERENCE: the coordinated enrichment of these supplied genes supports the contextual cellular-regulation signal interpretation, but expression alone does not establish functional activity or a unique cell state.
- **Verified references:** PMID:8491376, PMID:39159060, PMID:41352636

## Coordinated biological program

BIOLOGICAL INFERENCE: the modules jointly support the proposed Cytotoxic CD8 T cells interpretation by combining the dominant identity-associated marker pattern with secondary state or contextual signals. The modules are coordinated at the level of co-enrichment in this cluster; the supplied evidence does not establish causal interaction among them.

## Supported conclusions

- DATASET OBSERVATION: all structured gene claims use only the ten supplied representative genes for this cluster.
- DATASET OBSERVATION: the highest-ranked genes combine fold-change, prevalence, specificity, statistical significance, and marker-score evidence.
- LITERATURE-SUPPORTED FACT: the cited references are the supplied verified gene-level references and are limited to their publication-specific contexts.
- BIOLOGICAL INFERENCE: the combined marker pattern strongly supports the proposed Cytotoxic CD8 T cells annotation.

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

**Moderate** — Overall confidence is Moderate because the annotation assessment is strongly supported, the marker statistics provide direct dataset support, and verified references provide gene-level context. Confidence is limited by non-unique gene contexts, absence of a cluster-level model probability, and lack of direct functional measurements.

## Plain-language explanation

The measured gene pattern is most consistent with Cytotoxic CD8 T cells. The strongest genes are enriched within this cluster, and the supplied publications provide context for the grouped biological modules. Some genes can occur in other cell types or states, and gene expression alone does not show that the inferred functions occurred. The supplied evidence is insufficient to determine one uniquely defined functional state.
