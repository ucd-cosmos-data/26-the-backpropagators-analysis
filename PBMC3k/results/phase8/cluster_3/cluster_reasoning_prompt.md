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
3

Current cell-type annotation:
Classical monocytes

Classification-model prediction:
Not available: Notebook 05 did not export a cluster-level prediction. The selected cell-level model was XGBoost.

Classification confidence, if available:
Not available as a cluster-level probability. Held-out Classical monocytes metrics for XGBoost: precision=1.000, recall=0.980, F1=0.990, support=50. These are evaluation metrics against expression-derived labels, not a cluster-level probability.

==================================================
DATASET OBSERVATIONS
==================================================

Representative marker genes:
S100A8, LGALS2, S100A9, FCN1, CST3, TYROBP, CD14, MS4A6A, LST1, AIF1

Marker-gene statistics:
representative_rank,gene,avg_log2FC,adjusted_p_value,pct_in,pct_out,specificity_delta,marker_score,selection_tier
1,S100A8,7.360887,7.621623e-225,0.942231,0.120318,0.821913,121.000134,primary: pct_in >= 0.20
2,LGALS2,7.016551,2.403732e-211,0.908367,0.050562,0.857805,120.376605,primary: pct_in >= 0.20
3,S100A9,7.183323,2.211534e-238,0.976096,0.212079,0.764017,109.763619,primary: pct_in >= 0.20
4,FCN1,5.470355,1.143427e-201,0.936255,0.146067,0.790188,86.452124,primary: pct_in >= 0.20
5,CST3,5.857136,2.283287e-223,0.992032,0.258427,0.733605,85.936477,primary: pct_in >= 0.20
6,TYROBP,5.471521,7.936130e-222,0.994024,0.257491,0.736533,80.599145,primary: pct_in >= 0.20
7,CD14,6.178094,2.153154e-103,0.641434,0.027154,0.614281,75.901679,primary: pct_in >= 0.20
8,MS4A6A,5.854212,1.466062e-114,0.681275,0.035581,0.645694,75.600639,primary: pct_in >= 0.20
9,LST1,4.502578,8.208264e-171,0.958167,0.215356,0.742812,66.891337,primary: pct_in >= 0.20
10,AIF1,4.549419,6.385215e-173,0.958167,0.23736,0.720808,65.585132,primary: pct_in >= 0.20


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
    "gene": "S100A8",
    "official_gene_name": "S100A8",
    "immune_function": "The selected PubMed collection discusses S100A8 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for S100A8, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "LGALS2",
    "official_gene_name": "LGALS2",
    "immune_function": "The selected PubMed collection discusses LGALS2 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for LGALS2, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "S100A9",
    "official_gene_name": "S100A9",
    "immune_function": "The selected PubMed collection discusses S100A9 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for S100A9, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "FCN1",
    "official_gene_name": "FCN1",
    "immune_function": "The selected PubMed collection discusses FCN1 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient.",
    "plain_language_note": "Selected PubMed records provide context for FCN1, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "CST3",
    "official_gene_name": "CST3",
    "immune_function": "The selected PubMed collection discusses CST3 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for CST3, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "TYROBP",
    "official_gene_name": "TYROBP",
    "immune_function": "The selected PubMed collection discusses TYROBP in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for TYROBP, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "CD14",
    "official_gene_name": "CD14",
    "immune_function": "The selected PubMed collection discusses CD14 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for CD14, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "MS4A6A",
    "official_gene_name": "MS4A6A",
    "immune_function": "The selected PubMed collection discusses MS4A6A in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for MS4A6A, but they do not by themselves establish what the gene does in this PBMC3k cluster."
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
    "gene": "AIF1",
    "official_gene_name": "AIF1",
    "immune_function": "The selected PubMed collection discusses AIF1 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for AIF1, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  }
]

Cluster-level literature summary:
# Literature Reference Report — Cluster 3: Classical monocytes

> This document organizes evidence for later analysis. It does not interpret the genes as a combined program and does not make a biological or clinical conclusion.

## Selected Genes

S100A8, LGALS2, S100A9, FCN1, CST3, TYROBP, CD14, MS4A6A, LST1, AIF1

## Dataset Boundary

The genes were selected from the Phase 6 marker ranking for cluster 3. Marker statistics are dataset observations. All publication claims come from the verified references table. Publication contexts do not describe or diagnose the PBMC3k source.

## Recurring Biological Functions

- gene-specific literature evidence: tagged for 10 gene(s)

## Recurring Immune Pathways

- publication-specific; no combined pathway inference: tagged for 10 gene(s)

## Recurring Disease Themes in the Selected Publications

- publication contexts only: tagged for 10 gene(s)

These are indexing tags, not evidence of disease in this dataset and not formal enrichment results.

## Confidence of Literature

| Gene | Grade | References | Reason |
| --- | --- | --- | --- |
| S100A8 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| LGALS2 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| S100A9 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| FCN1 | C | 3 | Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient. |
| CST3 | B | 3 | Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade. |
| TYROBP | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| CD14 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| MS4A6A | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| LST1 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| AIF1 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |

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
    "gene": "S100A8",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "LGALS2",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "S100A9",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "FCN1",
    "evidence_grade": "C",
    "publication_count": 3,
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient."
  },
  {
    "gene": "CST3",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "TYROBP",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "CD14",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "MS4A6A",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "LST1",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "AIF1",
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
    "reference_id": "PMID:30105020",
    "gene": "CD14",
    "title": "Monocyte Subsets: Phenotypes and Function in Tuberculosis Infection.",
    "journal": "Frontiers in immunology",
    "year": 2018,
    "DOI": "10.3389/fimmu.2018.01726",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: In humans, three circulating monocyte subsets are classified based on relative expression levels of CD14 and CD16 surface proteins, namely classical, intermediate and non-classical subsets.",
    "evidence_categories": "Review; Biomarker"
  },
  {
    "reference_id": "PMID:34279540",
    "gene": "CD14",
    "title": "Single-cell analysis of human skin identifies CD14+ type 3 dendritic cells co-producing IL1B and IL23A in psoriasis.",
    "journal": "The Journal of experimental medicine",
    "year": 2021,
    "DOI": "10.1084/jem.20202345",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Here, we performed index-sorted single-cell flow cytometry and RNA sequencing of lesional and nonlesional AD and PSO skin to identify macrophages and all DC subsets, including the newly described mature LAMP3+BIRC3+ DCs enriched in immunoregulatory molecules (mregDC) and CD14+ DC3.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40023733",
    "gene": "CD14",
    "title": "Integrative analysis reveals the multilateral inflammatory mechanisms of CD14 monocytes in gout.",
    "journal": "Annals of the rheumatic diseases",
    "year": 2025,
    "DOI": "10.1016/j.ard.2025.01.046",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: OBJECTIVES: Gout, prevalent inflammatory arthritis caused by urate crystal deposition, involves immune cell activation, yet the precise role of CD14 monocytes in initiating the inflammatory response is poorly understood.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:37854583",
    "gene": "CST3",
    "title": "CST3 alleviates bilirubin-induced neurocytes' damage by promoting autophagy.",
    "journal": "Translational neuroscience",
    "year": 2023,
    "DOI": "10.1515/tnsci-2022-0314",
    "evidence_grade": "B",
    "study_type": "Other PubMed-indexed study",
    "summary": "PubMed abstract evidence: It has been reported that cystatin C (CST3) concentrations have a significant positive correlation with total bilirubin (TB) levels and a negative correlation with albumin levels.",
    "evidence_categories": "Association; Mechanism"
  },
  {
    "reference_id": "PMID:40925202",
    "gene": "CST3",
    "title": "The ferroptosis-associated gene TIMP1 facilitates skin scar formation through the interaction with CST3 in fibroblasts.",
    "journal": "International immunopharmacology",
    "year": 2025,
    "DOI": "10.1016/j.intimp.2025.115496",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Further mechanistic studies demonstrated that in human dermal fibroblast cells, the ferroptosis regulator TIMP metallopeptidase inhibitor 1 (TIMP1) significantly promotes fibroblast differentiation toward a mature phenotype through interactions with cystatin C (CST3), characterized by upregulated expression of myofibroblast differentiation markers such as α-smooth muscle actin (α-SMA) and connective tissue growth...",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41167578",
    "gene": "CST3",
    "title": "Multi-Omics discovery and clinical validation of IGFBP2, B2M, and CST3 as a serum biomarker panel for diabetic kidney disease progression.",
    "journal": "Gene",
    "year": 2026,
    "DOI": "10.1016/j.gene.2025.149858",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Integration with proteomics prioritized three candidate biomarkers-IGFBP2, B2M, and CST3- which were further assessed in murine DKD models (STZ/HFD-induced) and clinical serum samples (n = 139).",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:38262391",
    "gene": "FCN1",
    "title": "Sputum Transcriptomics Reveals FCN1+ Macrophage Activation in Mild Eosinophilic Asthma Compared to Non-Asthmatic Eosinophilic Bronchitis.",
    "journal": "Allergy, asthma & immunology research",
    "year": 2024,
    "DOI": "10.4168/aair.2024.16.1.55",
    "evidence_grade": "C",
    "study_type": "Other PubMed-indexed study",
    "summary": "PubMed abstract evidence: FABP4+ macrophages, SPP1+ macrophages, FCN1+ macrophages, dendritic cells, T cells, B cells, mast cells, and epithelial cells were identified based on gene expression profiling.",
    "evidence_categories": "Association; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:39139822",
    "gene": "FCN1",
    "title": "Multi-omics evaluation of the prognostic value and immune signature of FCN1 in pan-cancer and its relationship with proliferation and apoptosis in acute myeloid leukemia.",
    "journal": "Frontiers in genetics",
    "year": 2024,
    "DOI": "10.3389/fgene.2024.1425075",
    "evidence_grade": "C",
    "study_type": "Laboratory or other primary study",
    "summary": "PubMed abstract evidence: BACKGROUND: The FCN1 gene encodes the ficolin-1 protein, implicated in the pathogenesis of various diseases, though its precise role in tumorigenesis remains elusive.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:39171604",
    "gene": "FCN1",
    "title": "Cross-tissue organization of myeloid cells in scleroderma and related fibrotic diseases.",
    "journal": "Current opinion in rheumatology",
    "year": 2024,
    "DOI": "10.1097/BOR.0000000000001047",
    "evidence_grade": "C",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: DC3 express similar inflammatory genes to monocytes, including FCN1 , IL1B, VCAN, S100A8, S100A9 , and S100A12 .",
    "evidence_categories": "Review; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:19330599",
    "gene": "LGALS2",
    "title": "Galectin-2 (LGALS2) 3279C/T polymorphism may be independently associated with diastolic blood pressure in patients with rheumatoid arthritis.",
    "journal": "Clinical and experimental hypertension (New York, N.Y. : 1993)",
    "year": 2009,
    "DOI": "10.1080/10641960802621267",
    "evidence_grade": "B",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: The galectin-2 (LGALS2) 3279 C/T single nucleotide polymorphism (SNP) has recently been associated with myocardial infarction (MI).",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:36499335",
    "gene": "LGALS2",
    "title": "Identification of Risk Genes Associated with Myocardial Infarction-Big Data Analysis and Literature Review.",
    "journal": "International journal of molecular sciences",
    "year": 2022,
    "DOI": "10.3390/ijms232315008",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: The most important genes increasing the risk for AMI are lymphotoxin-a gene (LTA), LGALS2, LDLR, and APOA5.",
    "evidence_categories": "Review"
  },
  {
    "reference_id": "PMID:39350165",
    "gene": "LGALS2",
    "title": "Deciphering the role of LGALS2: insights into tertiary lymphoid structure-associated dendritic cell activation and immunotherapeutic potential in breast cancer patients.",
    "journal": "Molecular cancer",
    "year": 2024,
    "DOI": "10.1186/s12943-024-02126-4",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Here, we performed an integrated analysis of bulk transcriptome data from over 6000 BRCA samples using biological network-based computational strategies and machine learning (ML) methods, and identified LGALS2 as a key marker within TLSs.",
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
    "reference_id": "PMID:30906402",
    "gene": "MS4A6A",
    "title": "Genetics of Alzheimer's Disease.",
    "journal": "Dementia and neurocognitive disorders",
    "year": 2018,
    "DOI": "10.12779/dnd.2018.17.4.131",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Genome-wide association studies have found risk genes such as ABCA7, BIN1, CASS4, CD33, CD2AP, CELF1, CLU, CR1, DSG2, EPHA1, FERMT2, HLA-DRB5-HLA-DRB1, INPP5D, MEF2C, MS4A6A/MS4A4E, NME8, PICALM, PTK2B, SLC24A4, SORL1, and ZCWPW1.",
    "evidence_categories": "Review; Biomarker"
  },
  {
    "reference_id": "PMID:40090082",
    "gene": "MS4A6A",
    "title": "MS4A6A regulates ox-LDL-induced endothelial dysfunction and monocyte adhesion in atherosclerosis via the IKK/NF-kappaB pathway.",
    "journal": "International immunopharmacology",
    "year": 2025,
    "DOI": "10.1016/j.intimp.2025.114404",
    "evidence_grade": "B",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: Membrane Spanning 4-Domains A6A (MS4A6A) is associated with inflammation and primarily regulates immunity and cell signaling.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41515934",
    "gene": "MS4A6A",
    "title": "The Myeloid Biomarker MS4A6A Drives an Immunosuppressive Microenvironment in Glioblastoma via Activation of the PGE2 Signaling Axis.",
    "journal": "International journal of molecular sciences",
    "year": 2025,
    "DOI": "10.3390/ijms27010058",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: We integrated bulk- and single-cell transcriptomic datasets (TCGA, CGGA, Ivy GAP, and Brain Immune Atlas) to systematically characterize the expression, prognostic relevance, and immune contexture of the myeloid biomarker membrane-spanning 4-domain A6A, MS4A6A, in GBM.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:27492899",
    "gene": "S100A8",
    "title": "S100A8/A9: From basic science to clinical application.",
    "journal": "Pharmacology & therapeutics",
    "year": 2016,
    "DOI": "10.1016/j.pharmthera.2016.07.015",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Both cells contain huge amounts of the heterodimeric protein S100A8/A9 in their cytoplasm.",
    "evidence_categories": "Review; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:38776909",
    "gene": "S100A8",
    "title": "Alarmin S100A8 imparts chemoresistance of esophageal cancer by reprogramming cancer-associated fibroblasts.",
    "journal": "Cell reports. Medicine",
    "year": 2024,
    "DOI": "10.1016/j.xcrm.2024.101576",
    "evidence_grade": "B",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: Mechanistically, we reveal that cancer-cell-derived S100A8 triggers the intracellular RhoA-ROCK-MLC2-MRTF-A pathway by binding to the CD147 receptor of CAFs, inducing CAF polarization and leading to chemoresistance.",
    "evidence_categories": "Association; Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:39929053",
    "gene": "S100A8",
    "title": "Inhibition of S100A8/A9 ameliorates neuroinflammation by blocking NET formation following traumatic brain injury.",
    "journal": "Redox biology",
    "year": 2025,
    "DOI": "10.1016/j.redox.2025.103532",
    "evidence_grade": "B",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: S100A8/A9, also known as calprotectin or myeloid-related protein-8/14 (MRP8/14), is an alarmin primarily secreted by activated neutrophils with potent pro-inflammatory property.",
    "evidence_categories": "Association; Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:32434457",
    "gene": "S100A9",
    "title": "S100A9 Links Inflammation and Repair in Myocardial Infarction.",
    "journal": "Circulation research",
    "year": 2020,
    "DOI": "10.1161/CIRCRESAHA.120.315865",
    "evidence_grade": "B",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: RATIONALE: The alarmin S100A9 has been identified as a potential therapeutic target in myocardial infarction.",
    "evidence_categories": "Association; Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:38013255",
    "gene": "S100A9",
    "title": "Roles of S100A8, S100A9 and S100A12 in infection, inflammation and immunity.",
    "journal": "Immunology",
    "year": 2024,
    "DOI": "10.1111/imm.13722",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: As members of the S100 protein subfamily of myeloid-related proteins, S100A8, S100A9 and S100A12 play a crucial role in resisting microbial infection and maintaining immune homeostasis.",
    "evidence_categories": "Review; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:39266214",
    "gene": "S100A9",
    "title": "S100A9 and HMGB1 orchestrate MDSC-mediated immunosuppression in melanoma through TLR4 signaling.",
    "journal": "Journal for immunotherapy of cancer",
    "year": 2024,
    "DOI": "10.1136/jitc-2024-009552",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Damage-associated molecular patterns S100A8, S100A9, and HMGB1, acting as toll like receptor 4 (TLR4) and receptor for advanced glycation endproducts (RAGE) ligands, are highly expressed in the tumor microenvironment and drive MDSC activation.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:36002854",
    "gene": "TYROBP",
    "title": "Microglial TYROBP/DAP12 in Alzheimer's disease: Transduction of physiological and pathological signals across TREM2.",
    "journal": "Molecular neurodegeneration",
    "year": 2022,
    "DOI": "10.1186/s13024-022-00552-w",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: TYROBP (also known as DAP12 or KARAP) is a transmembrane adaptor protein initially described as a receptor-activating subunit component of natural killer (NK) cells.",
    "evidence_categories": "Review; Biomarker"
  },
  {
    "reference_id": "PMID:39508103",
    "gene": "TYROBP",
    "title": "Trem2/Tyrobp Signaling Protects Against Aortic Dissection and Rupture by Inhibiting Macrophage Activation in Mice.",
    "journal": "Arteriosclerosis, thrombosis, and vascular biology",
    "year": 2025,
    "DOI": "10.1161/ATVBAHA.124.321429",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: The Trem2 (triggering receptor expressed on myeloid cells 2)/Tyrobp (TYRO protein tyrosine kinase-binding protein) signaling pathway critically regulates innate immunity and has emerged as an important target in cardiovascular diseases; however, its role in AD remains unclear.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40301889",
    "gene": "TYROBP",
    "title": "Monoallelic TYROBP deletion is a novel risk factor for Alzheimer's disease.",
    "journal": "Molecular neurodegeneration",
    "year": 2025,
    "DOI": "10.1186/s13024-025-00830-3",
    "evidence_grade": "B",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: Biallelic loss-of-function variants in TYROBP and TREM2 cause autosomal recessive presenile dementia with bone cysts known as Nasu-Hakola disease (NHD, alternatively polycystic lipomembranous osteodysplasia with sclerosing leukoencephalopathy, PLOSL).",
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
