You are an evidence-grounded biological reasoning assistant specializing in
single-cell RNA sequencing and immune-cell biology.

Your task is to interpret one cell cluster using only the dataset observations
and literature evidence provided below.

Do not use unsupported outside knowledge as evidence. You may connect facts
logically, but every inference must be clearly labeled as an inference.

==================================================
CLUSTER INFORMATION
==================================================

Cluster ID:
4

Current cell-type annotation:
CD16+ non-classical monocytes

Classification-model prediction:
Not available: Notebook 05 did not export a cluster-level prediction. The selected cell-level model was XGBoost.

Classification confidence, if available:
Not available as a cluster-level probability. Held-out CD16+ non-classical monocytes metrics for XGBoost: precision=0.944, recall=1.000, F1=0.971, support=17. These are evaluation metrics against expression-derived labels, not a cluster-level probability.

==================================================
DATASET OBSERVATIONS
==================================================

Representative marker genes:
FCGR3A, IFITM3, MS4A7, RP11-290F20.3, LST1, FCER1G, AIF1, SERPINA1, CDKN1C, CFD

Marker-gene statistics:
representative_rank,gene,avg_log2FC,adjusted_p_value,pct_in,pct_out,specificity_delta,marker_score,selection_tier
1,FCGR3A,5.580072,2.019646e-83,0.959064,0.13255,0.826515,92.240234,primary: pct_in >= 0.20
2,IFITM3,4.839578,8.118456e-80,0.982456,0.17349,0.808966,78.301083,primary: pct_in >= 0.20
3,MS4A7,5.144174,1.499904e-58,0.80117,0.070531,0.730639,75.170634,primary: pct_in >= 0.20
4,RP11-290F20.3,4.994358,5.524284e-60,0.818713,0.066883,0.751831,75.098231,primary: pct_in >= 0.20
5,LST1,5.176203,5.832898e-92,1.0,0.31212,0.68788,71.212132,primary: pct_in >= 0.20
6,FCER1G,4.84711,5.865870e-90,1.0,0.313741,0.686259,66.527424,primary: pct_in >= 0.20
7,AIF1,4.882141,1.644050e-87,1.0,0.331171,0.668829,65.306299,primary: pct_in >= 0.20
8,SERPINA1,4.246182,4.230557e-72,0.953216,0.197811,0.755405,64.151771,primary: pct_in >= 0.20
9,CDKN1C,6.371625,2.851058e-25,0.502924,0.008107,0.494817,63.055758,primary: pct_in >= 0.20
10,CFD,4.121818,1.000024e-63,0.94152,0.180786,0.760734,62.712149,primary: pct_in >= 0.20


For each gene, the table may include:
- average log2 fold change
- adjusted p-value
- percentage expressed inside the cluster
- percentage expressed outside the cluster
- marker score
- rank

==================================================
VERIFIED LITERATURE EVIDENCE
==================================================

Gene evidence summaries:
[
  {
    "gene": "FCGR3A",
    "official_gene_name": "FCGR3A",
    "immune_function": "The selected PubMed collection discusses FCGR3A in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for FCGR3A, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "IFITM3",
    "official_gene_name": "IFITM3",
    "immune_function": "The selected PubMed collection discusses IFITM3 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient.",
    "plain_language_note": "Selected PubMed records provide context for IFITM3, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "MS4A7",
    "official_gene_name": "MS4A7",
    "immune_function": "The selected PubMed collection discusses MS4A7 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for MS4A7, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "RP11-290F20.3",
    "official_gene_name": "RP11-290F20.3",
    "immune_function": "Direct gene-specific immune evidence was not identified by the focused PubMed search; the supplied evidence is insufficient to assign a literature-supported function.",
    "immune_cell_contexts": "No literature-supported immune-cell context is assigned from this evidence collection.",
    "biological_role": "No mechanism is assigned. The supplied evidence is insufficient to determine this.",
    "function_tags": "insufficient direct evidence",
    "pathway_tags": "no pathway assigned",
    "grade_explanation": "Selected evidence is insufficient: no verified gene-specific PubMed record met the focused relevance criteria.",
    "plain_language_note": "The focused search did not find enough direct evidence to explain RP11-290F20.3; the dataset observation remains separate from literature claims."
  },
  {
    "gene": "LST1",
    "official_gene_name": "LST1",
    "immune_function": "The selected PubMed collection discusses LST1 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for LST1, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "FCER1G",
    "official_gene_name": "FCER1G",
    "immune_function": "The selected PubMed collection discusses FCER1G in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for FCER1G, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "AIF1",
    "official_gene_name": "AIF1",
    "immune_function": "The selected PubMed collection discusses AIF1 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for AIF1, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "SERPINA1",
    "official_gene_name": "SERPINA1",
    "immune_function": "The selected PubMed collection discusses SERPINA1 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for SERPINA1, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "CDKN1C",
    "official_gene_name": "CDKN1C",
    "immune_function": "The selected PubMed collection discusses CDKN1C in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient.",
    "plain_language_note": "Selected PubMed records provide context for CDKN1C, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "CFD",
    "official_gene_name": "CFD",
    "immune_function": "The selected PubMed collection discusses CFD in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for CFD, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  }
]

Cluster-level literature summary:
# Literature Reference Report — Cluster 4: CD16+ non-classical monocytes

> This document organizes evidence for later analysis. It does not interpret the genes as a combined program and does not make a biological or clinical conclusion.

## Selected Genes

FCGR3A, IFITM3, MS4A7, RP11-290F20.3, LST1, FCER1G, AIF1, SERPINA1, CDKN1C, CFD

## Dataset Boundary

The genes were selected from the Phase 6 marker ranking for cluster 4. Marker statistics are dataset observations. All publication claims come from the verified references table. Publication contexts do not describe or diagnose the PBMC3k source.

## Recurring Biological Functions

- gene-specific literature evidence: tagged for 9 gene(s)
- insufficient direct evidence: tagged for 1 gene(s)

## Recurring Immune Pathways

- publication-specific; no combined pathway inference: tagged for 9 gene(s)
- no pathway assigned: tagged for 1 gene(s)

## Recurring Disease Themes in the Selected Publications

- publication contexts only: tagged for 9 gene(s)
- no evidence-based disease context assigned: tagged for 1 gene(s)

These are indexing tags, not evidence of disease in this dataset and not formal enrichment results.

## Confidence of Literature

| Gene | Grade | References | Reason |
| --- | --- | --- | --- |
| FCGR3A | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| IFITM3 | C | 3 | Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient. |
| MS4A7 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| RP11-290F20.3 | E | 0 | Selected evidence is insufficient: no verified gene-specific PubMed record met the focused relevance criteria. |
| LST1 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| FCER1G | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| AIF1 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| SERPINA1 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| CDKN1C | C | 3 | Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient. |
| CFD | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |

Grades describe the selected evidence set using the explicit A–E rules in Notebook 07. A high grade does not make every reported mechanism universal or causal.

## Unanswered Biological Questions

- Which selected markers are stable across independent PBMC cohorts?
- Which publication-specific findings transfer to this cluster and tissue context?
- Which claims have independent protein-level and functional support?
- Which grade-E genes need better direct literature evidence?

## Future Interpretation

Cross-gene reasoning, pathway synthesis, and biological conclusions are intentionally deferred to Notebook 08.


Evidence grades:
[
  {
    "gene": "FCGR3A",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "IFITM3",
    "evidence_grade": "C",
    "publication_count": 3,
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient."
  },
  {
    "gene": "MS4A7",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "RP11-290F20.3",
    "evidence_grade": "E",
    "publication_count": 0,
    "grade_explanation": "Selected evidence is insufficient: no verified gene-specific PubMed record met the focused relevance criteria."
  },
  {
    "gene": "LST1",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "FCER1G",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "AIF1",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "SERPINA1",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "CDKN1C",
    "evidence_grade": "C",
    "publication_count": 3,
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient."
  },
  {
    "gene": "CFD",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  }
]

Verified references:
[
  {
    "reference_id": "PMID:38898508",
    "gene": "AIF1",
    "title": "Identification of novel therapeutic targets for chronic kidney disease and kidney function by integrating multi-omics proteome with transcriptome.",
    "journal": "Genome medicine",
    "year": 2024,
    "DOI": "10.1186/s13073-024-01356-x",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: The other 15 proteins were also candidate targets (GATM, AIF1L, DQA2, PFKFB2, NFATC1, activin AC, Apo A-IV, MFAP4, DJC10, C2CD2L, TCEA2, HLA-E, PLD3, AIF1, and GMPR1).",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40325180",
    "gene": "AIF1",
    "title": "Characterizing the immune landscape of tumor-infiltrating lymphocytes in non-small cell lung cancer.",
    "journal": "Genes and immunity",
    "year": 2025,
    "DOI": "10.1038/s41435-025-00330-w",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: During the transitional phase, macrophages (FTL) and dendritic (AIF1) cells transported the most CD3 TCR clones to T cells, while cytotoxicity CD8+ T (NKG7) cells transported to terminal exhausted CD8+ T cells.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41448409",
    "gene": "AIF1",
    "title": "Identification and experimental validation of biomarkers for acute myeloid leukemia based on single-cell RNA sequencing data.",
    "journal": "Molecular and cellular probes",
    "year": 2026,
    "DOI": "10.1016/j.mcp.2025.102059",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: MR analysis of marker genes showed that ITGB2, AIF1, CA2, CST7, and JCHAIN had a significant causal relationship with AML.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41126215",
    "gene": "CDKN1C",
    "title": "Beckwith-Wiedemann spectrum (BWSp): an update on diagnosis, management, and follow-up from the scientific committee of the Italian BWSp association.",
    "journal": "Italian journal of pediatrics",
    "year": 2025,
    "DOI": "10.1186/s13052-025-02131-3",
    "evidence_grade": "C",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: The disorder is primarily associated with loss or gain of methylation at imprinting control regions IC2 and IC1, paternal uniparental disomy of 11p15, or pathogenic variants in CDKN1C.",
    "evidence_categories": "Review"
  },
  {
    "reference_id": "PMID:41361693",
    "gene": "CDKN1C",
    "title": "A low-level Cdkn1c/p57kip2 expression in spinal progenitors drives the transition from proliferative to neurogenic modes of division.",
    "journal": "EMBO reports",
    "year": 2026,
    "DOI": "10.1038/s44319-025-00653-9",
    "evidence_grade": "C",
    "study_type": "Laboratory/animal study",
    "summary": "PubMed abstract evidence: Using single-cell RNA-seq data from the chick embryonic neural tube, we identify the cell cycle regulator Cdkn1c as a key regulator of this transition.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41803883",
    "gene": "CDKN1C",
    "title": "Single-cell RNA-seq and in vitro study reveal Fusobacterium nucleatum impairs β-cell identity in type 2 diabetes via the NF-κB-CDKN1C axis.",
    "journal": "Journal of translational medicine",
    "year": 2026,
    "DOI": "10.1186/s12967-026-07981-x",
    "evidence_grade": "C",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Integrated Pearson correlation and in vitro analyses identified the cell cycle regulator CDKN1C as a central mediator through which F.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:37802037",
    "gene": "CFD",
    "title": "Complement factor D targeting protects endotheliopathy in organoid and monkey models of COVID-19.",
    "journal": "Cell stem cell",
    "year": 2023,
    "DOI": "10.1016/j.stem.2023.09.001",
    "evidence_grade": "A",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: Longitudinal serum proteome analysis identified aberrant complement signature in critically ill patients driven by the amplification cycle regulated by complement factor B and D (CFD).",
    "evidence_categories": "Association; Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:40225580",
    "gene": "CFD",
    "title": "FOS-driven inflammatory CAFs promote colorectal cancer liver metastasis via the SFRP1-FGFR2-HIF1 axis.",
    "journal": "Theranostics",
    "year": 2025,
    "DOI": "10.7150/thno.111625",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Results: We identified an inflammatory CAF subtype (CFD+ iCAFs) associated with poor clinical outcomes, advanced staging, and metastasis.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40340806",
    "gene": "CFD",
    "title": "Transcriptome-wide analysis reveals potential roles of CFD and ANGPTL4 in fibroblasts regulating B cell lineage for extracellular matrix-driven clustering and novel avenues for immunotherapy in breast cancer.",
    "journal": "Molecular medicine (Cambridge, Mass.)",
    "year": 2025,
    "DOI": "10.1186/s10020-025-01237-y",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Single-cell RNA sequencing data further revealed that angiopoietin like 4 (ANGPTL4)+ fibroblasts were specifically linked to the C2 phenotype, while complement factor D (CFD)+ fibroblasts characterized the other ECM clusters.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:36054819",
    "gene": "FCER1G",
    "title": "Fc Fragment of IgE Receptor Ig (FCER1G) acts as a key gene involved in cancer immune infiltration and tumour microenvironment.",
    "journal": "Immunology",
    "year": 2023,
    "DOI": "10.1111/imm.13557",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Although recent studies have revealed the relationship between Fc Fragment of IgE Receptor Ig (FCER1G) and human tumours, there is still a lack of a more comprehensive pan-cancer analysis of FCER1G as an immune-related gene.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:37202883",
    "gene": "FCER1G",
    "title": "Peripheral immune mapping and multi-omics analysis in Pd-1 inhibitor-induced myocarditis.",
    "journal": "Journal of leukocyte biology",
    "year": 2023,
    "DOI": "10.1093/jleuko/qiad056",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Besides, reduced γδ T cells characterized with effector functions, increased natural killer T cells with high levels of FCER1G in patients may suggest an association with disease development.",
    "evidence_categories": "Review; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:41758834",
    "gene": "FCER1G",
    "title": "Fcer1g and St3gal1: Macrophage-associated angiogenesis biomarkers and therapeutic targets in sepsis-induced acute lung injury.",
    "journal": "PloS one",
    "year": 2026,
    "DOI": "10.1371/journal.pone.0343449",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: RESULTS: Two macrophage-associated angiogenesis-related genes, Fcer1g (FCER1G) and St3gal1 (ST3GAL1), were identified as key biomarkers.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40320713",
    "gene": "FCGR3A",
    "title": "Differential effects of tofacitinib on macrophage activation contribute to lack of response in ulcerative colitis patients.",
    "journal": "Journal of Crohn's & colitis",
    "year": 2025,
    "DOI": "10.1093/ecco-jcc/jjaf076",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Response was associated with significant changes in the abundance and/or activation of immune, epithelial, and stromal cells and the downregulation of S100A9, FCGR3A, MMP12 in resident macrophages.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41030449",
    "gene": "FCGR3A",
    "title": "Spatial transcriptomics reveals distinct role of monocytes/macrophages with high FCGR3A expression in kidney transplant rejections.",
    "journal": "Frontiers in immunology",
    "year": 2025,
    "DOI": "10.3389/fimmu.2025.1654741",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Subclusters of monocytes/macrophages with high Fc gamma receptor IIIA (FCGR3A) expression were identified in C4d-positive active AMR and acute TCMR, and the spatial distribution of these cells corresponded to the characteristic histopathological features.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41173191",
    "gene": "FCGR3A",
    "title": "Single-cell spatial transcriptomics reveal intraglomerular cell activation and ligand-receptor relationships in chronic, active antibody mediated rejection.",
    "journal": "Kidney international",
    "year": 2026,
    "DOI": "10.1016/j.kint.2025.08.042",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Proximity of NK cells and macrophages with GEC revealed several potential ligand receptor interactions previously unappreciated, including GEC IL33→NK cell IL1RL1 and GEC HLA-DQA1→Macrophage FCGR3A, implicating NK cell and macrophage activation in endothelial injury.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:23890736",
    "gene": "IFITM3",
    "title": "Immune system disturbances in schizophrenia.",
    "journal": "Biological psychiatry",
    "year": 2014,
    "DOI": "10.1016/j.biopsych.2013.06.010",
    "evidence_grade": "C",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Recent data suggest that IFITM3 expression is a critical mediator of maternal immune activation.",
    "evidence_categories": "Review; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:40611157",
    "gene": "IFITM3",
    "title": "IFITM3 enhances immunosensitivity via MHC-I regulation and is associated with the efficacy of anti-PD-1/-L1 therapy in SCLC.",
    "journal": "Molecular cancer",
    "year": 2025,
    "DOI": "10.1186/s12943-025-02383-x",
    "evidence_grade": "C",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Clinical data from SCLC patients treated with PD-1/PD-L1 inhibitors were used to investigate the associations between treatment efficacy and IFITM3 expression.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40684176",
    "gene": "IFITM3",
    "title": "Periodontitis-induced neuroinflammation triggers IFITM3-Aβ axis to cause alzheimer's disease-like pathology and cognitive decline.",
    "journal": "Alzheimer's research & therapy",
    "year": 2025,
    "DOI": "10.1186/s13195-025-01818-3",
    "evidence_grade": "C",
    "study_type": "Laboratory/animal study",
    "summary": "PubMed abstract evidence: Recently, interferon-induced transmembrane protein 3 (IFITM3), an inflammation-induced innate immunity protein, was identified as a novel γ-secretase modulatory protein for Aβ production in AD.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:16362817",
    "gene": "LST1",
    "title": "LST1 and NCR3 expression in autoimmune inflammation and in response to IFN-gamma, LPS and microbial infection.",
    "journal": "Immunogenetics",
    "year": 2006,
    "DOI": "10.1007/s00251-005-0057-2",
    "evidence_grade": "A",
    "study_type": "Human laboratory study",
    "summary": "PubMed abstract evidence: The specific function of LST1 is not known, although expression analysis and functional data suggest an immunomodulatory role.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:24816991",
    "gene": "LST1",
    "title": "An upstream open reading frame regulates LST1 expression during monocyte differentiation.",
    "journal": "PloS one",
    "year": 2014,
    "DOI": "10.1371/journal.pone.0096245",
    "evidence_grade": "A",
    "study_type": "Human laboratory study",
    "summary": "PubMed abstract evidence: The main objective of the present study was to assess whether uORFs regulate the expression of the MHC class III gene LST1.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41488617",
    "gene": "LST1",
    "title": "LST1: a novel biomarker for efferocytosis in the co-occurrence of type 2 diabetes mellitus and clear cell renal cell carcinoma.",
    "journal": "Frontiers in immunology",
    "year": 2025,
    "DOI": "10.3389/fimmu.2025.1737749",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Integrating machine learning and transcriptome analysis, we identified LST1 as a pivotal regulatory gene in both T2DM and ccRCC (AUC> 0.745).",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:36944954",
    "gene": "MS4A7",
    "title": "The short isoform of MS4A7 is a novel player in glioblastoma microenvironment, M2 macrophage polarization, and tumor progression.",
    "journal": "Journal of neuroinflammation",
    "year": 2023,
    "DOI": "10.1186/s12974-023-02766-1",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: The short isoform of MS4A7 (MS4A7-s) was selected for evaluation by RT-PCR and western blotting in clinical specimens.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:38478630",
    "gene": "MS4A7",
    "title": "Hepatic danger signaling triggers TREM2+ macrophage induction and drives steatohepatitis via MS4A7-dependent inflammasome activation.",
    "journal": "Science translational medicine",
    "year": 2024,
    "DOI": "10.1126/scitranslmed.adk1866",
    "evidence_grade": "A",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: Here, we identify membrane-spanning 4-domains a7 (MS4A7) as a NAM-specific pathogenic factor that exacerbates MASH progression in mice.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:39954254",
    "gene": "MS4A7",
    "title": "Lipid droplet efferocytosis attenuates proinflammatory signaling in macrophages via TREM2- and MS4A7-dependent mechanisms.",
    "journal": "Cell reports",
    "year": 2025,
    "DOI": "10.1016/j.celrep.2025.115310",
    "evidence_grade": "A",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: Additionally, MS4A7 downregulation contributes to LD efferocytosis-mediated dampening of inflammatory response.",
    "evidence_categories": "Association; Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:39737188",
    "gene": "SERPINA1",
    "title": "Regulation of epidermal barrier function and pathogenesis of psoriasis by serine protease inhibitors.",
    "journal": "Frontiers in immunology",
    "year": 2024,
    "DOI": "10.3389/fimmu.2024.1498067",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Only a small number, such as the mutation of SerpinA1/A3/B3, are involved in the pathogenesis of GPP.",
    "evidence_categories": "Review; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:41270966",
    "gene": "SERPINA1",
    "title": "Air pollution exacerbates cardiovascular-kidney-metabolic syndrome and sarcopenia comorbidity via shared genetic-epigenetic mechanisms: A multi-omics and Mendelian Randomization study.",
    "journal": "Metabolism: clinical and experimental",
    "year": 2026,
    "DOI": "10.1016/j.metabol.2025.156452",
    "evidence_grade": "B",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: Proteomics (F-statistics > 10) revealed potential targets linking CKM/sarcopenia (HP, FCGR3B, GALNT2) and CKM-events/sarcopenia (SERPINA1, FER).",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41558114",
    "gene": "SERPINA1",
    "title": "SERPINA1 as a Shared Biomarker in Periodontitis and Oral Squamous Cell Carcinoma.",
    "journal": "International dental journal",
    "year": 2026,
    "DOI": "10.1016/j.identj.2025.109378",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: At the cellular level, we evaluated SERPINA1 expression in an LPS-induced periodontal inflammation model and conducted siRNA-mediated knockdown in CAL27 oral cancer cells to examine its effects on proliferation, migration and invasion.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  }
]

==================================================
REASONING INSTRUCTIONS
==================================================

1. Begin with the dataset evidence. Identify the strongest observations based
   on marker specificity, expression prevalence, fold change, statistical
   significance, and marker score.

2. Group the representative genes into functional biological modules. A module
   should contain genes that contribute to the same biological process, cell
   identity, pathway, regulatory function, or communication mechanism.

3. For each functional module:
   - list the relevant genes
   - describe the shared biological function
   - identify which statements are directly supported by the supplied literature
   - explain how the dataset observations support the module
   - assign a confidence level of High, Moderate, or Low
   - explain the reason for that confidence level

4. Evaluate the proposed cell-type annotation:
   - state whether it is strongly supported, partially supported, or weakly supported
   - identify the genes and literature evidence that support it
   - identify plausible alternative cell types or cell states
   - explain what additional evidence would help distinguish the alternatives

5. Produce an overall biological interpretation of the cluster. Explain how the
   functional modules work together as a coordinated biological program. Do not
   merely summarize each gene separately.

6. Clearly distinguish among:
   - DATASET OBSERVATION: directly measured in this analysis
   - LITERATURE-SUPPORTED FACT: reported in the supplied references
   - BIOLOGICAL INFERENCE: a reasoned connection between the dataset and literature
   - UNKNOWN OR UNCERTAIN: not sufficiently supported by the supplied evidence

7. Treat disease-related papers only as research contexts in which a gene or
   pathway was studied. Gene expression in this dataset must not be interpreted
   as evidence that the donor had any disease.

8. Do not:
   - diagnose a disease
   - infer the donor's identity, health status, age, sex, ethnicity, or medical history
   - claim that a marker gene is unique to one cell type unless the supplied evidence
     explicitly establishes uniqueness
   - invent biological mechanisms
   - invent citations, PMIDs, DOIs, numerical values, or experimental results
   - treat correlation as causation
   - claim pathway activation solely because one associated gene is expressed
   - hide contradictory or weak evidence

9. If the evidence is incomplete, explicitly say:
   "The supplied evidence is insufficient to determine this."

10. Cite supplied sources using their PMID or reference identifier. Only cite
    references included in the verified reference list.

==================================================
REQUIRED OUTPUT
==================================================

Return valid JSON using exactly this structure:

{
  "cluster_id": "",
  "proposed_cell_type": "",
  "annotation_assessment": {
    "support_level": "strongly supported | partially supported | weakly supported",
    "supporting_genes": [],
    "supporting_evidence": "",
    "alternative_interpretations": [],
    "additional_evidence_needed": []
  },
  "strongest_dataset_observations": [
    {
      "gene": "",
      "observation": "",
      "importance": ""
    }
  ],
  "functional_modules": [
    {
      "module_name": "",
      "genes": [],
      "dataset_support": "",
      "literature_support": "",
      "biological_inference": "",
      "confidence": "High | Moderate | Low",
      "confidence_reason": "",
      "reference_ids": []
    }
  ],
  "coordinated_biological_program": "",
  "supported_conclusions": [],
  "reasonable_inferences": [],
  "weak_or_uncertain_interpretations": [],
  "contradictory_evidence": [],
  "limitations": [],
  "overall_confidence": "High | Moderate | Low",
  "overall_confidence_reason": "",
  "plain_language_explanation": ""
}

Before returning the JSON, silently verify that:
- every citation exists in the supplied references
- every gene mentioned appears in the supplied data
- observations and inferences are clearly separated
- no diagnosis or donor inference appears
- the output contains valid JSON
