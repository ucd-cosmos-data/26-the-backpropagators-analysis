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
1

Current cell-type annotation:
B cells

Classification-model prediction:
Not available: Notebook 05 did not export a cluster-level prediction. The selected cell-level model was XGBoost.

Classification confidence, if available:
Not available as a cluster-level probability. Held-out B cells metrics for XGBoost: precision=1.000, recall=1.000, F1=1.000, support=35. These are evaluation metrics against expression-derived labels, not a cluster-level probability.

==================================================
DATASET OBSERVATIONS
==================================================

Representative marker genes:
CD79A, MS4A1, CD79B, TCL1A, HLA-DQA1, LINC00926, VPREB3, HLA-DQB1, HLA-DRA, FCER2

Marker-gene statistics:
representative_rank,gene,avg_log2FC,adjusted_p_value,pct_in,pct_out,specificity_delta,marker_score,selection_tier
1,CD79A,7.704485,1.223091e-164,0.925287,0.041485,0.883803,136.184875,primary: pct_in >= 0.20
2,MS4A1,6.358171,2.358891e-133,0.841954,0.053275,0.788679,100.291108,primary: pct_in >= 0.20
3,CD79B,5.473424,1.834737e-149,0.905172,0.141921,0.763251,83.551929,primary: pct_in >= 0.20
4,TCL1A,6.973357,9.948571e-72,0.617816,0.021397,0.596419,83.180812,primary: pct_in >= 0.20
5,HLA-DQA1,5.323151,1.841307e-136,0.885057,0.117031,0.768027,81.766464,primary: pct_in >= 0.20
6,LINC00926,7.396564,1.581289e-58,0.554598,0.009607,0.544991,80.621168,primary: pct_in >= 0.20
7,VPREB3,7.447546,2.560128e-44,0.482759,0.00655,0.476208,70.931684,primary: pct_in >= 0.20
8,HLA-DQB1,4.928785,2.692386e-125,0.856322,0.147162,0.70916,69.905974,primary: pct_in >= 0.20
9,HLA-DRA,4.864488,2.495813e-164,1.0,0.49345,0.50655,49.282145,primary: pct_in >= 0.20
10,FCER2,6.480006,2.326877e-26,0.376437,0.008734,0.367703,47.654371,primary: pct_in >= 0.20


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
    "gene": "CD79A",
    "official_gene_name": "CD79A",
    "immune_function": "The selected PubMed collection discusses CD79A in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Selected evidence is computational and lacks stronger primary experimental support in this collection.",
    "plain_language_note": "Selected PubMed records provide context for CD79A, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "MS4A1",
    "official_gene_name": "MS4A1",
    "immune_function": "The selected PubMed collection discusses MS4A1 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for MS4A1, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "CD79B",
    "official_gene_name": "CD79B",
    "immune_function": "The selected PubMed collection discusses CD79B in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Selected evidence is limited and does not meet the thresholds for grades A–D.",
    "plain_language_note": "Selected PubMed records provide context for CD79B, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "TCL1A",
    "official_gene_name": "TCL1A",
    "immune_function": "The selected PubMed collection discusses TCL1A in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for TCL1A, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "HLA-DQA1",
    "official_gene_name": "HLA-DQA1",
    "immune_function": "The selected PubMed collection discusses HLA-DQA1 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for HLA-DQA1, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "LINC00926",
    "official_gene_name": "LINC00926",
    "immune_function": "The selected PubMed collection discusses LINC00926 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for LINC00926, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "VPREB3",
    "official_gene_name": "VPREB3",
    "immune_function": "The selected PubMed collection discusses VPREB3 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for VPREB3, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "HLA-DQB1",
    "official_gene_name": "HLA-DQB1",
    "immune_function": "The selected PubMed collection discusses HLA-DQB1 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for HLA-DQB1, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "HLA-DRA",
    "official_gene_name": "HLA-DRA",
    "immune_function": "The selected PubMed collection discusses HLA-DRA in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for HLA-DRA, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "FCER2",
    "official_gene_name": "FCER2",
    "immune_function": "The selected PubMed collection discusses FCER2 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for FCER2, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  }
]

Cluster-level literature summary:
# Literature Reference Report — Cluster 1: B cells

> This document organizes evidence for later analysis. It does not interpret the genes as a combined program and does not make a biological or clinical conclusion.

## Selected Genes

CD79A, MS4A1, CD79B, TCL1A, HLA-DQA1, LINC00926, VPREB3, HLA-DQB1, HLA-DRA, FCER2

## Dataset Boundary

The genes were selected from the Phase 6 marker ranking for cluster 1. Marker statistics are dataset observations. All publication claims come from the verified references table. Publication contexts do not describe or diagnose the PBMC3k source.

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
| CD79A | D | 3 | Selected evidence is computational and lacks stronger primary experimental support in this collection. |
| MS4A1 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| CD79B | E | 3 | Selected evidence is limited and does not meet the thresholds for grades A–D. |
| TCL1A | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| HLA-DQA1 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| LINC00926 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| VPREB3 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| HLA-DQB1 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| HLA-DRA | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| FCER2 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |

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
    "gene": "CD79A",
    "evidence_grade": "D",
    "publication_count": 3,
    "grade_explanation": "Selected evidence is computational and lacks stronger primary experimental support in this collection."
  },
  {
    "gene": "MS4A1",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "CD79B",
    "evidence_grade": "E",
    "publication_count": 3,
    "grade_explanation": "Selected evidence is limited and does not meet the thresholds for grades A–D."
  },
  {
    "gene": "TCL1A",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "HLA-DQA1",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "LINC00926",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "VPREB3",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "HLA-DQB1",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "HLA-DRA",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "FCER2",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  }
]

Verified references:
[
  {
    "reference_id": "PMID:38203179",
    "gene": "CD79A",
    "title": "B-Cell Receptor Signaling and Beyond: The Role of Igα (CD79a)/Igβ (CD79b) in Normal and Malignant B Cells.",
    "journal": "International journal of molecular sciences",
    "year": 2023,
    "DOI": "10.3390/ijms25010010",
    "evidence_grade": "D",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Igα (CD79a)/Igβ (CD79b) are essential components of BCR that are indispensable for its functionality, signal initiation, and signal transduction.",
    "evidence_categories": "Review; Mechanism"
  },
  {
    "reference_id": "PMID:40734705",
    "gene": "CD79A",
    "title": "Single-Cell Sequence and Machine Learning Identify a CD79A+B Cells-Related Transcriptional Signature for Predicting Clinical Outcomes and Immune Microenvironment in Breast Cancer.",
    "journal": "Cancer informatics",
    "year": 2025,
    "DOI": "10.1177/11769351251360675",
    "evidence_grade": "D",
    "study_type": "Computational study",
    "summary": "PubMed abstract evidence: OBJECTIVE: The aim of this study was to investigate the role and mechanism of CD79A+ B cells in mediating the microenvironment of breast cancer and the relationship with the prognosis of breast cancer.",
    "evidence_categories": "Association; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:41348872",
    "gene": "CD79A",
    "title": "Integrating single-cell biophysical and transcriptomic features to resolve functional heterogeneity in mantle cell lymphoma.",
    "journal": "Science advances",
    "year": 2025,
    "DOI": "10.1126/sciadv.ady2963",
    "evidence_grade": "D",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Linked measurements reveal that buoyant mass and stiffness characterize B cell development states from naïve to plasma cell and correlate with expression of oncogenic B cell receptor signaling genes such as BLK and CD79A.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:11396639",
    "gene": "CD79B",
    "title": "CD79: a review.",
    "journal": "Applied immunohistochemistry & molecular morphology : AIMM",
    "year": 2001,
    "DOI": "10.1097/00129039-200106000-00001",
    "evidence_grade": "E",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: CD79 is composed of CD79a and CD79b components expressed almost exclusively on B cells and B-cell neoplasms.",
    "evidence_categories": "Review; Biomarker"
  },
  {
    "reference_id": "PMID:25925619",
    "gene": "CD79B",
    "title": "Safety and activity of the anti-CD79B antibody-drug conjugate polatuzumab vedotin in relapsed or refractory B-cell non-Hodgkin lymphoma and chronic lymphocytic leukaemia: a phase 1 study.",
    "journal": "The Lancet. Oncology",
    "year": 2015,
    "DOI": "10.1016/S1470-2045(15)70128-2",
    "evidence_grade": "E",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: Polatuzumab vedotin is an antibody-drug conjugate containing an anti-CD79B monoclonal antibody conjugated to the microtubule-disrupting agent monomethyl auristatin E.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:38203179",
    "gene": "CD79B",
    "title": "B-Cell Receptor Signaling and Beyond: The Role of Igα (CD79a)/Igβ (CD79b) in Normal and Malignant B Cells.",
    "journal": "International journal of molecular sciences",
    "year": 2023,
    "DOI": "10.3390/ijms25010010",
    "evidence_grade": "E",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Igα (CD79a)/Igβ (CD79b) are essential components of BCR that are indispensable for its functionality, signal initiation, and signal transduction.",
    "evidence_categories": "Review; Mechanism"
  },
  {
    "reference_id": "PMID:24010859",
    "gene": "FCER2",
    "title": "FCER2 (CD23) asthma-related single nucleotide polymorphisms yields increased IgE binding and Egr-1 expression in human B cells.",
    "journal": "American journal of respiratory cell and molecular biology",
    "year": 2014,
    "DOI": "10.1165/rcmb.2013-0112OC",
    "evidence_grade": "A",
    "study_type": "Human laboratory study",
    "summary": "PubMed abstract evidence: Polymorphisms within FCER2, the gene encoding CD23, have been associated with atopy, increased risk of exacerbations in patients with asthma, and high serum IgE levels.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:33108776",
    "gene": "FCER2",
    "title": "Correlations between exhaled nitric oxide, rs28364072 polymorphism of FCER2 gene, asthma control, and inhaled corticosteroid responsiveness in children with asthma.",
    "journal": "Journal of breath research",
    "year": 2020,
    "DOI": "10.1088/1752-7163/abc4ec",
    "evidence_grade": "A",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: This study aimed to describe the clinical and biological characteristics, and its correlation with polymorphism of rs28364072 in FCER2 of asthmatic children.",
    "evidence_categories": "Association; Experimental evidence"
  },
  {
    "reference_id": "PMID:36445014",
    "gene": "FCER2",
    "title": "IgG memory B cells expressing IL4R and FCER2 are associated with atopic diseases.",
    "journal": "Allergy",
    "year": 2023,
    "DOI": "10.1111/all.15601",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: RESULTS: We identified a novel population of IgG memory B cells characterized by the expression of IL-4/IL-13 regulated genes FCER2/CD23, IL4R, IL13RA1, and IGHE, denoting a history of differentiation during type 2 immune responses.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40428403",
    "gene": "HLA-DQA1",
    "title": "Genetic Determinants of Colonic Diverticulosis-A Systematic Review.",
    "journal": "Genes",
    "year": 2025,
    "DOI": "10.3390/genes16050581",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Identified in GWAS studies, gene candidates may be grouped into blood group and immune system-related genes (ABO, HLA-DQA1, HLA-H, OAS1, TNFSF13, FADD), extracellular matrix and connective tissue genes (COL6A1, COLQ, EFEMP1, ELN, HAS2, TIMP2), signaling and cell communication (BMPR1B, WNT4, RHOU, PHGR1, PCSK5), nervous system and neurodevelopment (BDNF, CACNB2, GPR158, SIRT1, SCAPER, TRPS1), metabolism and...",
    "evidence_categories": "Review; Mechanism"
  },
  {
    "reference_id": "PMID:41173191",
    "gene": "HLA-DQA1",
    "title": "Single-cell spatial transcriptomics reveal intraglomerular cell activation and ligand-receptor relationships in chronic, active antibody mediated rejection.",
    "journal": "Kidney international",
    "year": 2026,
    "DOI": "10.1016/j.kint.2025.08.042",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Proximity of NK cells and macrophages with GEC revealed several potential ligand receptor interactions previously unappreciated, including GEC IL33→NK cell IL1RL1 and GEC HLA-DQA1→Macrophage FCGR3A, implicating NK cell and macrophage activation in endothelial injury.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41866337",
    "gene": "HLA-DQA1",
    "title": "Population and single-cell analyses reveal immune cell-specific expression profiles associated with Alzheimer's disease risk.",
    "journal": "Alzheimer's & dementia : the journal of the Alzheimer's Association",
    "year": 2026,
    "DOI": "10.1002/alz.71282",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Expression of BIN1, CTSW, CTSH, HLA-DRB1, TSTD1, PLEKHA1, and SCIMP increased AD risk, while EPHA1-AS1, FCER1G, FIBP, KAT8, STX4, and HLA-DQA1 reduced it.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:28052334",
    "gene": "HLA-DQB1",
    "title": "Association of HLA-DRB1 and HLA-DQB1 with red-blood-cell alloimmunization in the Czech population.",
    "journal": "Vox sanguinis",
    "year": 2017,
    "DOI": "10.1111/vox.12478",
    "evidence_grade": "B",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: HLA-DRB1 and HLA-DQB1 variants were determined by PCR-SSO and their frequencies compared between the patients (patient subgroups) and 375 ethnically and regionally matched controls.",
    "evidence_categories": "Association; Experimental evidence"
  },
  {
    "reference_id": "PMID:40373365",
    "gene": "HLA-DQB1",
    "title": "Unraveling the pathophysiology of narcolepsy type 1 through hypothesis-driven and hypothesis-generating approaches.",
    "journal": "Seminars in immunology",
    "year": 2025,
    "DOI": "10.1016/j.smim.2025.101962",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Given the genetic association with the HLA-DQB1 * 06:02 allele and environmental links with the 2009 influenza pandemic, many lines of evidence point towards an immune mechanism, notably autoimmunity, underlying the disease pathophysiology.",
    "evidence_categories": "Review; Mechanism"
  },
  {
    "reference_id": "PMID:41364757",
    "gene": "HLA-DQB1",
    "title": "HLA-DQB1*03:01 strongly affects age of onset of type 1 narcolepsy independently of DQA1 and ethnicity.",
    "journal": "Proceedings of the National Academy of Sciences of the United States of America",
    "year": 2025,
    "DOI": "10.1073/pnas.2513989122",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: In contrast, HLA-DQB1*06:02-positive heterodimer (DQ0602) dosage did not strongly affect onset, and other known narcolepsy-associated genetic loci had minor effects.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:36801619",
    "gene": "HLA-DRA",
    "title": "Early peripheral blood MCEMP1 and HLA-DRA expression predicts COVID-19 prognosis.",
    "journal": "EBioMedicine",
    "year": 2023,
    "DOI": "10.1016/j.ebiom.2023.104472",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: FINDINGS: The most consistent differentially regulated genes in peripheral blood of severe COVID-19 patients were MCEMP1, HLA-DRA and ETS1 across the 7 transcriptomics datasets.",
    "evidence_categories": "Review; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:39694280",
    "gene": "HLA-DRA",
    "title": "Single-cell RNA sequencing of chronic idiopathic erythroderma defines disease-specific markers.",
    "journal": "The Journal of allergy and clinical immunology",
    "year": 2025,
    "DOI": "10.1016/j.jaci.2024.11.037",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: While patients with CIE and eCTCL lacked the strong type 2 or type 17 immune skewing typically found in atopic dermatitis or psoriasis, respectively, they were characterized by upregulation of MHC II genes (HLA-DRB1, HLA-DRA, and CD74) in keratinocytes and fibroblasts, most likely in an IFN-γ-dependent fashion.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40157360",
    "gene": "HLA-DRA",
    "title": "A spatially resolved transcriptome landscape during thyroid cancer progression.",
    "journal": "Cell reports. Medicine",
    "year": 2025,
    "DOI": "10.1016/j.xcrm.2025.102043",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Our integrative analysis reveals extensive molecular and cellular heterogeneity during thyroid cancer progression, enabling the identification of three distinct thyrocyte meta-clusters, including TG+IYG+ subpopulation in PT, HLA-DRB1+HLA-DRA+ subpopulation in early cancerous stages, and APOE+APOC1+ subpopulation in late-stage progression.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:35551428",
    "gene": "LINC00926",
    "title": "Long non-coding RNA LINC00926 regulates WNT10B signaling pathway thereby altering inflammatory gene expression in PTSD.",
    "journal": "Translational psychiatry",
    "year": 2022,
    "DOI": "10.1038/s41398-022-01971-5",
    "evidence_grade": "A",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: Increased H3K4me3 resulted from LINC00926, which we found to be upregulated in the PTSD sample, bringing in histone methyltransferase, MLL1, onto WNT10B promotor leading to the introduction of H3K4 trimethylation.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:37728413",
    "gene": "LINC00926",
    "title": "Ferroptosis and WDFY4 as novel targets for immunotherapy of lung adenocarcinoma.",
    "journal": "Aging",
    "year": 2023,
    "DOI": "10.18632/aging.205042",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: During the later phases of B cell differentiation in LUAD, there was a decrease in the expression levels of ACAP1, LINC00926, TLR10, MS4A1, WDFY4, and TRIM22 genes, whereas the expression levels of TMEM59, TP53INP1, and METTL7A genes were elevated.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:42274770",
    "gene": "LINC00926",
    "title": "YY1-activated LINC00926 promotes the survival of mycobacteria and regulates inflammatory response in Mycobacterium tuberculosis-infected macrophages.",
    "journal": "Archives of microbiology",
    "year": 2026,
    "DOI": "10.1007/s00203-026-04953-z",
    "evidence_grade": "A",
    "study_type": "Human laboratory study",
    "summary": "PubMed abstract evidence: Notably, lncRNA LINC00926 is upregulated in peripheral blood mononuclear cells from tuberculosis patients.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:32482755",
    "gene": "MS4A1",
    "title": "The regulation and function of CD20: an \"enigma\" of B-cell biology and targeted therapy.",
    "journal": "Haematologica",
    "year": 2020,
    "DOI": "10.3324/haematol.2019.243543",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Several epigenetic (EZH2, HDAC1/2, HDAC1/4, HDAC6, complex Sin3A-HDAC1) and transcription factors (USF, OCT1/2, PU.1, PiP, ELK1, ETS1, SP1, NFκB, FOXO1, CREM, SMAD2/3) regulating CD20 expression (encoded by MS4A1) have been characterized.",
    "evidence_categories": "Review; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:37433400",
    "gene": "MS4A1",
    "title": "Novel cell subtypes of SPP1 + S100P+, MS4A1-SPP1 + S100P+ were key subpopulations in intrahepatic cholangiocarcinoma.",
    "journal": "Biochimica et biophysica acta. General subjects",
    "year": 2023,
    "DOI": "10.1016/j.bbagen.2023.130420",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: RESULTS: iCCA presented a unique immune ecosystem, with increased proportions of Epi (epithelial)-SPP1-2, Epi-S100P-1, Epi-DN (double negative for SPP1 and S100P expression)-1, Epi-DN-2, Epi-DP (double positive for SPP1 and S100P expression)-1, Plasma B-3, Plasma B-2, B-HSPA1A-1, B-HSPA1A-2 cells, and decreased proportions of B-MS4A1.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:39239552",
    "gene": "MS4A1",
    "title": "MS4A1-PTGS2 axis induces taurine metabolic reprogramming to exacerbate abdominal aortic aneurysm progression.",
    "journal": "International journal of medical sciences",
    "year": 2024,
    "DOI": "10.7150/ijms.99659",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: The publication title identifies MS4A1 as its subject: MS4A1-PTGS2 axis induces taurine metabolic reprogramming to exacerbate abdominal aortic aneurysm progression.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:34206047",
    "gene": "TCL1A",
    "title": "TCL1A, B Cell Regulation and Tolerance in Renal Transplantation.",
    "journal": "Cells",
    "year": 2021,
    "DOI": "10.3390/cells10061367",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Among proposed biomarkers, T-cell Leukemia/Lymphoma protein 1A (TCL1A) has been observed as overexpressed in the peripheral blood of operational tolerant patients in several studies.",
    "evidence_categories": "Review; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:38764038",
    "gene": "TCL1A",
    "title": "TCL1A-expressing B cells are critical for tertiary lymphoid structure formation and the prognosis of oral squamous cell carcinoma.",
    "journal": "Journal of translational medicine",
    "year": 2024,
    "DOI": "10.1186/s12967-024-05292-7",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: We utilized tissue microarray data for 146 OSCC clinical samples and RNA sequencing data of 359 OSCC samples from The Cancer Genome Atlas (TCGA) to investigate the role of T-cell leukemia 1 A (TCL1A) in OSCC prognosis.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:39946833",
    "gene": "TCL1A",
    "title": "TCL1A in naïve B cells as a therapeutic target for type 1 diabetes.",
    "journal": "EBioMedicine",
    "year": 2025,
    "DOI": "10.1016/j.ebiom.2025.105593",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Specifically, the population of naïve B cells increased in patients with newly diagnosed T1D who expressed elevated levels of the AKT kinase coactivator TCL1A.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:20823132",
    "gene": "VPREB3",
    "title": "The pre-B-cell receptor associated protein VpreB3 is a useful diagnostic marker for identifying c-MYC translocated lymphomas.",
    "journal": "Haematologica",
    "year": 2010,
    "DOI": "10.3324/haematol.2010.025767",
    "evidence_grade": "A",
    "study_type": "Human laboratory study",
    "summary": "PubMed abstract evidence: Recent profiling studies unexpectedly revealed abundant transcripts of one member of the VpreB family, VpreB3, in a subset of mature B cells and Burkitt lymphoma.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:24493312",
    "gene": "VPREB3",
    "title": "The combined expression of VPREB3 and ID3 represents a new helpful tool for the routine diagnosis of mature aggressive B-cell lymphomas.",
    "journal": "Hematological oncology",
    "year": 2014,
    "DOI": "10.1002/hon.2094",
    "evidence_grade": "A",
    "study_type": "Human laboratory study",
    "summary": "PubMed abstract evidence: In particular, mutations in the transcription factors ID3 and TCF3, leading to overexpression of B-cell receptor components such as VPREB3, have been shown to be specific for Burkitt lymphoma (BL) and play an important tumourigenic role by mediating the activation of the pro-survival phosphatidylinositol-3-OH kinase pathway.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:25861052",
    "gene": "VPREB3",
    "title": "Pre-B Lymphocyte Protein 3 (VPREB3) Expression in the Adrenal Cortex: Precedent for non-Immunological Roles in Normal and Neoplastic Human Tissues.",
    "journal": "Endocrine pathology",
    "year": 2015,
    "DOI": "10.1007/s12022-015-9366-7",
    "evidence_grade": "A",
    "study_type": "Human laboratory study",
    "summary": "PubMed abstract evidence: The pre-B lymphocyte protein 3 (VPREB3) is expressed during B cell differentiation and in subsets of mature B lymphocytes and is mainly found in bone marrow and lymphoid tissue germinative centers.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
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
