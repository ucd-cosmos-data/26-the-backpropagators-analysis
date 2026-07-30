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
6

Current cell-type annotation:
Activated/transitional T cells

Classification-model prediction:
Not available: Notebook 05 did not export a cluster-level prediction. The selected cell-level model was XGBoost.

Classification confidence, if available:
Not available as a cluster-level probability. Held-out Activated/transitional T cells metrics for XGBoost: precision=0.636, recall=0.538, F1=0.583, support=13. These are evaluation metrics against expression-derived labels, not a cluster-level probability.

==================================================
DATASET OBSERVATIONS
==================================================

Representative marker genes:
CCL5, IL32, CD3D, RPL23A, RPS3, RPS12, MALAT1, RPS25, RPS14, RPL13

Marker-gene statistics:
representative_rank,gene,avg_log2FC,adjusted_p_value,pct_in,pct_out,specificity_delta,marker_score,selection_tier
1,CCL5,2.067858,3.022016e-05,0.523438,0.305976,0.217461,2.032417,primary: pct_in >= 0.20
2,IL32,1.377941,2.033227e-06,0.765625,0.541434,0.224191,1.758324,primary: pct_in >= 0.20
3,CD3D,1.333352,6.311240e-07,0.71875,0.50996,0.20879,1.725988,primary: pct_in >= 0.20
4,RPL23A,0.424583,1.431692e-04,1.0,0.990837,0.009163,0.014956,primary: pct_in >= 0.20
5,RPS3,0.475426,2.874728e-07,1.0,0.995618,0.004382,0.013629,primary: pct_in >= 0.20
6,RPS12,0.389514,1.129513e-03,1.0,0.993227,0.006773,0.007775,primary: pct_in >= 0.20
7,MALAT1,0.902251,3.301258e-19,1.0,0.999602,0.000398,0.006643,primary: pct_in >= 0.20
8,RPS25,0.439362,1.170849e-04,0.984375,0.980876,0.003499,0.006043,primary: pct_in >= 0.20
9,RPS14,0.326824,5.302522e-04,1.0,0.995618,0.004382,0.004692,primary: pct_in >= 0.20
10,RPL13,0.35512,2.124474e-04,1.0,0.997211,0.002789,0.003637,primary: pct_in >= 0.20


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
    "gene": "CCL5",
    "official_gene_name": "CCL5",
    "immune_function": "The selected PubMed collection discusses CCL5 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for CCL5, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "IL32",
    "official_gene_name": "IL32",
    "immune_function": "The selected PubMed collection discusses IL32 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for IL32, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "CD3D",
    "official_gene_name": "CD3D",
    "immune_function": "The selected PubMed collection discusses CD3D in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for CD3D, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "RPL23A",
    "official_gene_name": "RPL23A",
    "immune_function": "The selected PubMed collection discusses RPL23A in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for RPL23A, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "RPS3",
    "official_gene_name": "RPS3",
    "immune_function": "The selected PubMed collection discusses RPS3 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient.",
    "plain_language_note": "Selected PubMed records provide context for RPS3, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "RPS12",
    "official_gene_name": "RPS12",
    "immune_function": "The selected PubMed collection discusses RPS12 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for RPS12, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "MALAT1",
    "official_gene_name": "MALAT1",
    "immune_function": "The selected PubMed collection discusses MALAT1 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient.",
    "plain_language_note": "Selected PubMed records provide context for MALAT1, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "RPS25",
    "official_gene_name": "RPS25",
    "immune_function": "The selected PubMed collection discusses RPS25 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for RPS25, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "RPS14",
    "official_gene_name": "RPS14",
    "immune_function": "The selected PubMed collection discusses RPS14 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for RPS14, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "RPL13",
    "official_gene_name": "RPL13",
    "immune_function": "The selected PubMed collection discusses RPL13 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for RPL13, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  }
]

Cluster-level literature summary:
# Literature Reference Report — Cluster 6: Activated/transitional T cells

> This document organizes evidence for later analysis. It does not interpret the genes as a combined program and does not make a biological or clinical conclusion.

## Selected Genes

CCL5, IL32, CD3D, RPL23A, RPS3, RPS12, MALAT1, RPS25, RPS14, RPL13

## Dataset Boundary

The genes were selected from the Phase 6 marker ranking for cluster 6. Marker statistics are dataset observations. All publication claims come from the verified references table. Publication contexts do not describe or diagnose the PBMC3k source.

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
| CCL5 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| IL32 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| CD3D | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| RPL23A | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| RPS3 | C | 3 | Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient. |
| RPS12 | B | 3 | Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade. |
| MALAT1 | C | 3 | Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient. |
| RPS25 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| RPS14 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| RPL13 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |

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
    "gene": "CCL5",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "IL32",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "CD3D",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "RPL23A",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "RPS3",
    "evidence_grade": "C",
    "publication_count": 3,
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient."
  },
  {
    "gene": "RPS12",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "MALAT1",
    "evidence_grade": "C",
    "publication_count": 3,
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient."
  },
  {
    "gene": "RPS25",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "RPS14",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "RPL13",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  }
]

Verified references:
[
  {
    "reference_id": "PMID:34514075",
    "gene": "CCL5",
    "title": "CCL5/CCR5 axis in human diseases and related treatments.",
    "journal": "Genes & diseases",
    "year": 2022,
    "DOI": "10.1016/j.gendis.2021.08.004",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: CCL5/CCR5 combination is known for facilitating inflammatory responses, as well as inducing the adhesion and migration of different T cell subsets in immune responses.",
    "evidence_categories": "Review; Mechanism"
  },
  {
    "reference_id": "PMID:38797830",
    "gene": "CCL5",
    "title": "A new integrative analysis of histopathology and single cell RNA-seq reveals the CCL5 mediated T and NK cell interaction with vascular cells in idiopathic pulmonary arterial hypertension.",
    "journal": "Journal of translational medicine",
    "year": 2024,
    "DOI": "10.1186/s12967-024-05304-6",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: RESULTS: Through an extensive bioinformatics analysis, CXCL9, CCL5, GZMA and GZMK were identified as hub genes that distinguished IPAH patients from controls.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40397747",
    "gene": "CCL5",
    "title": "Astrocyte-derived CCL5-mediated CCR5+ neutrophil infiltration drives depression pathogenesis.",
    "journal": "Science advances",
    "year": 2025,
    "DOI": "10.1126/sciadv.adt6632",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Furthermore, by genetic or pharmacologic disruption, we identified a chemotactic effect of the astrocyte-derived chemokine CCL5 on mediating the infiltration of CCR5+ neutrophils and behavioral disorders in male depressed mice.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:16264327",
    "gene": "CD3D",
    "title": "CD3 deficiencies.",
    "journal": "Current opinion in allergy and clinical immunology",
    "year": 2005,
    "DOI": "10.1097/01.all.0000191886.12645.79",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: RECENT FINDINGS: Homozygous mutations in CD3D and CD3E genes lead to a complete block in T-cell development and thus to an early-onset severe combined immunodeficiency phenotype.",
    "evidence_categories": "Review"
  },
  {
    "reference_id": "PMID:33283362",
    "gene": "CD3D",
    "title": "Concomitant overexpression of mir-182-5p and mir-182-3p raises the possibility of IL-17-producing Treg formation in breast cancer by targeting CD3d, ITK, FOXO1, and NFATs: A meta-analysis and experimental study.",
    "journal": "Cancer science",
    "year": 2021,
    "DOI": "10.1111/cas.14764",
    "evidence_grade": "B",
    "study_type": "Human laboratory study",
    "summary": "PubMed abstract evidence: FOXO1, CD3d, ITK, NFATc3, NFATc4, and IL-2RA were targeted by miR-182, due to which their expression decreased in PBMCs of patients.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:35712757",
    "gene": "CD3D",
    "title": "CD3D: a prognostic biomarker associated with immune infiltration and immunotherapeutic response in head and neck squamous cell carcinoma.",
    "journal": "Bioengineered",
    "year": 2022,
    "DOI": "10.1080/21655979.2022.2084254",
    "evidence_grade": "B",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: Recent studies have demonstrated that CD3D activates T-cell-related signal transduction and is associated with the antitumor immune response in several cancers.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:39435643",
    "gene": "IL32",
    "title": "Pericytes Modulate Third-Generation Tyrosine Kinase Inhibitor Sensitivity in EGFR-Mutated Lung Cancer Cells Through IL32-β5-Integrin Paracrine Signaling.",
    "journal": "Advanced science (Weinheim, Baden-Wurttemberg, Germany)",
    "year": 2024,
    "DOI": "10.1002/advs.202405130",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: The study shows that PCs isolated from EGFR-mutated patients have a unique secretome profile, notably secreting IL32 and affecting signaling pathways and biological processes linked to TKI sensitivity.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40330458",
    "gene": "IL32",
    "title": "Advancing personalized, predictive, and preventive medicine in bladder cancer: a multi-omics and machine learning approach for novel prognostic modeling, immune profiling, and therapeutic target discovery.",
    "journal": "Frontiers in immunology",
    "year": 2025,
    "DOI": "10.3389/fimmu.2025.1572034",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: RESULTS: The ICDRS, based on eight key genes (IL32, AHNAK, ANXA5, FN1, GSN, CNN3, FXYD3, CTSS), effectively stratified BLCA patients into high- and low-risk groups with significant differences in overall survival (OS, P < 0.001).",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40997225",
    "gene": "IL32",
    "title": "Acute Respiratory Distress Syndrome Molecular Phenotypes Have Distinct Lower Respiratory Tract Transcriptomes.",
    "journal": "American journal of respiratory and critical care medicine",
    "year": 2025,
    "DOI": "10.1164/rccm.202407-1454OC",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Eighteen genes were reproducibly differentially expressed between phenotypes in both cohorts, including greater expression of IL32, HSPA8, and PPP3CC in hyperinflammatory ARDS.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:35473929",
    "gene": "MALAT1",
    "title": "An intersegmental single-cell profile reveals aortic heterogeneity and identifies a novel Malat1+ vascular smooth muscle subtype involved in abdominal aortic aneurysm formation.",
    "journal": "Signal transduction and targeted therapy",
    "year": 2022,
    "DOI": "10.1038/s41392-022-00943-x",
    "evidence_grade": "C",
    "study_type": "Laboratory/animal study",
    "summary": "PubMed abstract evidence: More importantly, vascular smooth muscle cells (VSMCs) demonstrated a novel composition in which VSMC 4 marked with the gene Malat1 were mainly distributed in the abdominal segment.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:38087169",
    "gene": "MALAT1",
    "title": "LncRNA MALAT1 and Ischemic Stroke: Pathogenesis and Opportunities.",
    "journal": "Molecular neurobiology",
    "year": 2024,
    "DOI": "10.1007/s12035-023-03853-3",
    "evidence_grade": "C",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Among these lncRNAs, MALAT1 (metastasis-associated lung adenocarcinoma transcript 1) has been extensively studied due to its involvement in the pathophysiological processes of IS.",
    "evidence_categories": "Review; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:38493144",
    "gene": "MALAT1",
    "title": "Long noncoding RNA Malat1 protects against osteoporosis and bone metastasis.",
    "journal": "Nature communications",
    "year": 2024,
    "DOI": "10.1038/s41467-024-46602-3",
    "evidence_grade": "C",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: MALAT1, one of the few highly conserved nuclear long noncoding RNAs (lncRNAs), is abundantly expressed in normal tissues.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40565588",
    "gene": "RPL13",
    "title": "Identifying CDCA4 as a Radiotherapy Resistance-Associated Gene in Colorectal Cancer by an Integrated Bioinformatics Analysis Approach.",
    "journal": "Genes",
    "year": 2025,
    "DOI": "10.3390/genes16060696",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: A gene signature, including CDCA4, FANCA, PBRM1, RPL13, and C12orf43, was developed to predict radiotherapy response.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40764361",
    "gene": "RPL13",
    "title": "Integrated single-cell and transcriptomic analysis of bone marrow-derived metastatic neuroblastoma reveals molecular mechanisms of metabolic reprogramming.",
    "journal": "Scientific reports",
    "year": 2025,
    "DOI": "10.1038/s41598-025-13626-8",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Through integrated analyses, five core metabolic reprogramming genes (MRPL21, NHP2, RPL13, RPL18A, and RPL27A) were identified and shown to be significantly associated with poor prognosis.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41779063",
    "gene": "RPL13",
    "title": "Single-cell transcriptomic profiling combined with Mendelian randomization illuminates molecular drivers of bladder cancer.",
    "journal": "Molecular genetics and genomics : MGG",
    "year": 2026,
    "DOI": "10.1007/s00438-026-02371-w",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Mendelian randomization highlighted six bladder-cancer-related genes-ARHGEF18, HLA-DRB5, ISG20, NCF1, RPL13, and YPEL5.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:37400220",
    "gene": "RPL23A",
    "title": "[Identification of core pathogenic genes and pathways in elderly osteoporosis based on bioinformatics analysis].",
    "journal": "Zhonghua yu fang yi xue za zhi [Chinese journal of preventive medicine]",
    "year": 2023,
    "DOI": "10.3760/cma.j.cn112150-20230221-00140",
    "evidence_grade": "A",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: Gene UBA52, UBB, RPS27A, RPS15, RPS12, RPL13A, RPL23A, RPL10A, RPS25 and RPS6 were selected and seven of them could encode ribosome proteins.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:37864923",
    "gene": "RPL23A",
    "title": "Comparative analysis of peripheral blood immunoinflammatory landscapes in patients with acute cholangitis and its secondary septic shock using single-cell RNA sequencing.",
    "journal": "Biochemical and biophysical research communications",
    "year": 2023,
    "DOI": "10.1016/j.bbrc.2023.149121",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Neutrophils-7 (CCL5, RPL23A, RPL13, RPS19 and RPS18) were mainly involved in the regulation of cellular functions.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:42311670",
    "gene": "RPL23A",
    "title": "Swimming ameliorates intervertebral disc degeneration accompanied by Rpl23a downregulation and changes in its immune-inflammatory pathway.",
    "journal": "Frontiers in immunology",
    "year": 2026,
    "DOI": "10.3389/fimmu.2026.1819987",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Ribosomal protein L23a (Rpl23a) participates in various inflammatory diseases, but its role in the intervertebral disc immune microenvironment has not been studied.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:37272618",
    "gene": "RPS12",
    "title": "Haploinsufficiency of the essential gene Rps12 causes defects in erythropoiesis and hematopoietic stem cell maintenance.",
    "journal": "eLife",
    "year": 2023,
    "DOI": "10.7554/eLife.69322",
    "evidence_grade": "B",
    "study_type": "Laboratory/animal study",
    "summary": "PubMed abstract evidence: We generated a conditional knockout mouse to partially delete Rps12.",
    "evidence_categories": "Association; Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:37400220",
    "gene": "RPS12",
    "title": "[Identification of core pathogenic genes and pathways in elderly osteoporosis based on bioinformatics analysis].",
    "journal": "Zhonghua yu fang yi xue za zhi [Chinese journal of preventive medicine]",
    "year": 2023,
    "DOI": "10.3760/cma.j.cn112150-20230221-00140",
    "evidence_grade": "B",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: Gene UBA52, UBB, RPS27A, RPS15, RPS12, RPL13A, RPL23A, RPL10A, RPS25 and RPS6 were selected and seven of them could encode ribosome proteins.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41261408",
    "gene": "RPS12",
    "title": "Unveiling the role of gastric cancer-associated mesenchymal stem cells and neutrophil extracellular traps through multi-omics analysis.",
    "journal": "Stem cell research & therapy",
    "year": 2025,
    "DOI": "10.1186/s13287-025-04768-7",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: MR analysis confirmed EIF1 and RPS12 as key genes with causal links to GC progression, demonstrating robust associations with immune cell infiltration and critical signaling pathways.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:20980806",
    "gene": "RPS14",
    "title": "New insights into 5q- syndrome as a ribosomopathy.",
    "journal": "Cell cycle (Georgetown, Tex.)",
    "year": 2010,
    "DOI": "10.4161/cc.9.21.13742",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Recently, two novel mouse models have provided evidence for the involvement of both RPS14 and the p53 pathway, and specific miRNAs in 5q- syndrome.",
    "evidence_categories": "Review; Mechanism"
  },
  {
    "reference_id": "PMID:32571542",
    "gene": "RPS14",
    "title": "The effect of miR-223 on cellular behaviour in non-5q myelodysplastic syndromes through targeting RPS14.",
    "journal": "Pathology",
    "year": 2020,
    "DOI": "10.1016/j.pathol.2020.03.010",
    "evidence_grade": "B",
    "study_type": "Human laboratory study",
    "summary": "PubMed abstract evidence: A decrease in RPS14 expression in non-5q MDS patients was confirmed by immunohistochemical analyses of MDS bone marrow biopsies.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:34432872",
    "gene": "RPS14",
    "title": "TLR7 ligation augments hematopoiesis in Rps14 (uS11) deficiency via paradoxical suppression of inflammatory signaling.",
    "journal": "Blood advances",
    "year": 2021,
    "DOI": "10.1182/bloodadvances.2020003055",
    "evidence_grade": "B",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: We developed a model of MDS in zebrafish with knockout of Rps14, the primary mediator of the anemia associated with del(5q) MDS.",
    "evidence_categories": "Association; Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:28260789",
    "gene": "RPS25",
    "title": "HBZ-mediated shift of JunD from growth suppressor to tumor promoter in leukemic cells by inhibition of ribosomal protein S25 expression.",
    "journal": "Leukemia",
    "year": 2017,
    "DOI": "10.1038/leu.2017.74",
    "evidence_grade": "A",
    "study_type": "Human laboratory study",
    "summary": "PubMed abstract evidence: To decipher the mechanisms for Δ JunD production, we looked into the translational machinery and observed that HBZ induces nuclear retention of RPS25 mRNA and loss of RPS25 protein expression, a component of the small ribosomal subunit.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:35766008",
    "gene": "RPS25",
    "title": "Upregulation of ribosome complexes at the blood-brain barrier in Alzheimer's disease patients.",
    "journal": "Journal of cerebral blood flow and metabolism : official journal of the International Society of Cerebral Blood Flow and Metabolism",
    "year": 2022,
    "DOI": "10.1177/0271678X221111602",
    "evidence_grade": "A",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: Of the 29 ribosomal proteins that were quantified, 28 (RPLP0, RPL4, RPL6, RPL7A, RPL8, RPL10A, RPL11, RPL12, RPL14, RPL15, RPL18, RPL23, RPL27, RPL27A, RPL31, RPL35A, RPS2, RPS3, RPS3A, RPS4X, RPS7, RPS8, RPS14, RPS16, RPS20, RPS24, RPS25, and RPSA) were significantly upregulated in AD patients.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:37400220",
    "gene": "RPS25",
    "title": "[Identification of core pathogenic genes and pathways in elderly osteoporosis based on bioinformatics analysis].",
    "journal": "Zhonghua yu fang yi xue za zhi [Chinese journal of preventive medicine]",
    "year": 2023,
    "DOI": "10.3760/cma.j.cn112150-20230221-00140",
    "evidence_grade": "A",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: Gene UBA52, UBB, RPS27A, RPS15, RPS12, RPL13A, RPL23A, RPL10A, RPS25 and RPS6 were selected and seven of them could encode ribosome proteins.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:29608488",
    "gene": "RPS3",
    "title": "Latexin and hematopoiesis.",
    "journal": "Current opinion in hematology",
    "year": 2018,
    "DOI": "10.1097/MOH.0000000000000428",
    "evidence_grade": "C",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: It inhibits nuclear translocation of ribosomal protein subunit 3 (Rps3), a novel latexin-binding protein, and sensitizes hematopoietic cells to radiation-induced cell death.",
    "evidence_categories": "Review; Mechanism"
  },
  {
    "reference_id": "PMID:37087770",
    "gene": "RPS3",
    "title": "RNA binding protein RPS3 mediates microglial polarization by activating NLRP3 inflammasome via SIRT1 in ischemic stroke.",
    "journal": "Journal of stroke and cerebrovascular diseases : the official journal of National Stroke Association",
    "year": 2023,
    "DOI": "10.1016/j.jstrokecerebrovasdis.2023.107132",
    "evidence_grade": "C",
    "study_type": "Laboratory/animal study",
    "summary": "PubMed abstract evidence: Here, we focused on function and mechanism of RNA binding protein RPS3 in microglial polarization after ischemic stroke.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40023134",
    "gene": "RPS3",
    "title": "Centromere protein U mediates the ubiquitination and degradation of RPS3 to facilitate temozolomide resistance in glioblastoma.",
    "journal": "Drug resistance updates : reviews and commentaries in antimicrobial and anticancer chemotherapy",
    "year": 2025,
    "DOI": "10.1016/j.drup.2025.101214",
    "evidence_grade": "C",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Mechanistically, CENPU cooperates with TRIM5α to promote the ubiquitination and degradation of RPS3 by inducing its polyubiquitination at the K214 residue.",
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
