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
7

Current cell-type annotation:
Naive/resting T cells

Classification-model prediction:
Not available: Notebook 05 did not export a cluster-level prediction. The selected cell-level model was XGBoost.

Classification confidence, if available:
Not available as a cluster-level probability. Held-out Naive/resting T cells metrics for XGBoost: precision=0.881, recall=0.822, F1=0.851, support=45. These are evaluation metrics against expression-derived labels, not a cluster-level probability.

==================================================
DATASET OBSERVATIONS
==================================================

Representative marker genes:
CCR7, CD3D, LDHB, PRKCQ-AS1, NOSIP, CD7, CD3E, PIK3IP1, LEF1, C6orf48

Marker-gene statistics:
representative_rank,gene,avg_log2FC,adjusted_p_value,pct_in,pct_out,specificity_delta,marker_score,selection_tier
1,CCR7,2.896683,1.762786e-44,0.54,0.125686,0.414314,24.002754,primary: pct_in >= 0.20
2,CD3D,1.829257,1.505187e-39,0.86,0.450183,0.409817,14.993219,primary: pct_in >= 0.20
3,LDHB,1.895979,1.378755e-73,0.953333,0.617916,0.335417,12.718891,primary: pct_in >= 0.20
4,PRKCQ-AS1,2.213363,1.508665e-19,0.397778,0.121572,0.276206,11.506337,primary: pct_in >= 0.20
5,NOSIP,1.706754,2.413143e-35,0.691111,0.375229,0.315883,10.782675,primary: pct_in >= 0.20
6,CD7,1.604004,1.423542e-26,0.642222,0.311243,0.330979,10.617835,primary: pct_in >= 0.20
7,CD3E,1.550029,3.138899e-30,0.764444,0.428245,0.336199,10.422377,primary: pct_in >= 0.20
8,PIK3IP1,1.766211,8.355855e-21,0.486667,0.203382,0.283285,10.006806,primary: pct_in >= 0.20
9,LEF1,2.001486,7.654412e-15,0.364444,0.124314,0.24013,6.784429,primary: pct_in >= 0.20
10,C6orf48,1.339001,9.591402e-30,0.755556,0.502285,0.25327,6.782583,primary: pct_in >= 0.20


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
    "gene": "CCR7",
    "official_gene_name": "CCR7",
    "immune_function": "The selected PubMed collection discusses CCR7 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for CCR7, but they do not by themselves establish what the gene does in this PBMC3k cluster."
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
    "gene": "LDHB",
    "official_gene_name": "LDHB",
    "immune_function": "The selected PubMed collection discusses LDHB in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for LDHB, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "PRKCQ-AS1",
    "official_gene_name": "PRKCQ-AS1",
    "immune_function": "The selected PubMed collection discusses PRKCQ-AS1 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient.",
    "plain_language_note": "Selected PubMed records provide context for PRKCQ-AS1, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "NOSIP",
    "official_gene_name": "NOSIP",
    "immune_function": "The selected PubMed collection discusses NOSIP in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for NOSIP, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "CD7",
    "official_gene_name": "CD7",
    "immune_function": "The selected PubMed collection discusses CD7 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for CD7, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "CD3E",
    "official_gene_name": "CD3E",
    "immune_function": "The selected PubMed collection discusses CD3E in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for CD3E, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "PIK3IP1",
    "official_gene_name": "PIK3IP1",
    "immune_function": "The selected PubMed collection discusses PIK3IP1 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for PIK3IP1, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "LEF1",
    "official_gene_name": "LEF1",
    "immune_function": "The selected PubMed collection discusses LEF1 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for LEF1, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "C6orf48",
    "official_gene_name": "C6orf48",
    "immune_function": "The selected PubMed collection discusses C6orf48 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for C6orf48, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  }
]

Cluster-level literature summary:
# Literature Reference Report — Cluster 7: Naive/resting T cells

> This document organizes evidence for later analysis. It does not interpret the genes as a combined program and does not make a biological or clinical conclusion.

## Selected Genes

CCR7, CD3D, LDHB, PRKCQ-AS1, NOSIP, CD7, CD3E, PIK3IP1, LEF1, C6orf48

## Dataset Boundary

The genes were selected from the Phase 6 marker ranking for cluster 7. Marker statistics are dataset observations. All publication claims come from the verified references table. Publication contexts do not describe or diagnose the PBMC3k source.

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
| CCR7 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| CD3D | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| LDHB | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| PRKCQ-AS1 | C | 3 | Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient. |
| NOSIP | B | 3 | Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade. |
| CD7 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| CD3E | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| PIK3IP1 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| LEF1 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| C6orf48 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |

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
    "gene": "CCR7",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "CD3D",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "LDHB",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "PRKCQ-AS1",
    "evidence_grade": "C",
    "publication_count": 3,
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient."
  },
  {
    "gene": "NOSIP",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "CD7",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "CD3E",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "PIK3IP1",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "LEF1",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "C6orf48",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  }
]

Verified references:
[
  {
    "reference_id": "PMID:15962222",
    "gene": "C6orf48",
    "title": "Single-nucleotide polymorphisms associated with symptomatic infection and differential human gene expression in healthy seropositive persons each implicate the cytoskeleton, integrin signaling, and oncosuppression in the pathogenesis of human parvovirus B19 infection.",
    "journal": "The Journal of infectious diseases",
    "year": 2005,
    "DOI": "10.1086/430950",
    "evidence_grade": "A",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: Differential expression was confirmed in 6 of 38 genes (SKIP, MACF1, SPAG7, FLOT1, c6orf48, and RASSF5) tested using real-time quantitative polymerase chain reaction in a different group of healthy subjects.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:38246423",
    "gene": "C6orf48",
    "title": "Association of GAL-8 promoter methylation levels with coronary plaque inflammation.",
    "journal": "International journal of cardiology",
    "year": 2024,
    "DOI": "10.1016/j.ijcard.2024.131782",
    "evidence_grade": "A",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: Among the differentially hypomethylated genes were GAL-8, LTF, and RFPL3, while the highly methylated genes were TMEM9B, ANK3, and C6orF48.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41455820",
    "gene": "C6orf48",
    "title": "Advancing leprosy risk prediction through identification of a whole blood host transcriptomic biomarker signature including non-coding genes.",
    "journal": "Scientific reports",
    "year": 2025,
    "DOI": "10.1038/s41598-025-33878-8",
    "evidence_grade": "A",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: Furthermore, the optimal 3-gene signature consisted of two non-coding genes and one coding gene (SNHG5, SNHG8, C6orf48; sensitivity: 88%; specificity: 88%; AUC: 0.96).",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:35281921",
    "gene": "CCR7",
    "title": "New Insights of CCR7 Signaling in Dendritic Cell Migration and Inflammatory Diseases.",
    "journal": "Frontiers in pharmacology",
    "year": 2022,
    "DOI": "10.3389/fphar.2022.841687",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: CCR7, collaborated with its ligands CCL19 and CCL21, controls extensive migratory events in the immune system.",
    "evidence_categories": "Review; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:40513067",
    "gene": "CCR7",
    "title": "Anti-angiogenic therapy combined with immune checkpoint blockade mediates CCR7 + CD8 + T-cell entry into HCC through high endothelial venules.",
    "journal": "Hepatology (Baltimore, Md.)",
    "year": 2026,
    "DOI": "10.1097/HEP.0000000000001426",
    "evidence_grade": "B",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: Multiplex immunohistochemistry and spatial analysis demonstrated that CCR7 + CD8 + T cells were spatially associated with HEVs.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41321019",
    "gene": "CCR7",
    "title": "CCL19+ fibroblast-CCR7+ T-cell crosstalk coordinates immunofibrotic signalling networks in systemic sclerosis.",
    "journal": "The British journal of dermatology",
    "year": 2026,
    "DOI": "10.1093/bjd/ljaf444",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: The functional role of the CCL19-CCR7 axis was further validated using a bleomycin-induced SSc mouse model.",
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
    "reference_id": "PMID:16264327",
    "gene": "CD3E",
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
    "reference_id": "PMID:35570001",
    "gene": "CD3E",
    "title": "The establishment and application of CD3E humanized mice in immunotherapy.",
    "journal": "Experimental animals",
    "year": 2022,
    "DOI": "10.1538/expanim.22-0012",
    "evidence_grade": "B",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: In this study, CD3E humanized mice were established by replacing the second to the seventh exon of the Cd3e mouse gene with the same exon of the human gene.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:35710869",
    "gene": "CD3E",
    "title": "Low transcriptomic of PTPRCv1 and CD3E is an independent predictor of mortality in HIV and tuberculosis co-infected patient.",
    "journal": "Scientific reports",
    "year": 2022,
    "DOI": "10.1038/s41598-022-14305-8",
    "evidence_grade": "B",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: At baseline, IL4δ2 was significantly more highly expressed in the deceased group than survivor matched controls, whereas CD3E, IL7R, PTPRCv1, CCL4, GNLY, BCL2, CCL5, NOD1, TLR3, and NLRP13 had significantly lower expression levels in the deceased group compared to survivor matched controls.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:28539325",
    "gene": "CD7",
    "title": "CD7-edited T cells expressing a CD7-specific CAR for the therapy of T-cell malignancies.",
    "journal": "Blood",
    "year": 2017,
    "DOI": "10.1182/blood-2017-01-761320",
    "evidence_grade": "B",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: CD7 is a transmembrane protein highly expressed in acute T-cell leukemia (T-ALL) and in a subset of peripheral T-cell lymphomas.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40771729",
    "gene": "CD7",
    "title": "CD7 CAR-T therapy: current developments, improvements, and dilemmas.",
    "journal": "Blood science (Baltimore, Md.)",
    "year": 2025,
    "DOI": "10.1097/BS9.0000000000000247",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Among the various potential target antigens, CD7 has garnered attention as a promising candidate.",
    "evidence_categories": "Review"
  },
  {
    "reference_id": "PMID:41290542",
    "gene": "CD7",
    "title": "Single-Cell Dissection Reveals Immune Dysregulation After CD5 or CD7-Directed Chimeric Antigen Receptor T-Cell Therapy.",
    "journal": "Advanced science (Weinheim, Baden-Wurttemberg, Germany)",
    "year": 2026,
    "DOI": "10.1002/advs.202509259",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: CD5- and CD7-directed chimeric antigen receptor T-cell (5CAR and 7CAR) therapies for T-cell malignancies carry the risk of life-threatening infection.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:36090994",
    "gene": "LDHB",
    "title": "Identify metabolism-related genes IDO1, ALDH2, NCOA2, SLC7A5, SLC3A2, LDHB, and HPRT1 as potential prognostic markers and correlate with immune infiltrates in head and neck squamous cell carcinoma.",
    "journal": "Frontiers in immunology",
    "year": 2022,
    "DOI": "10.3389/fimmu.2022.955614",
    "evidence_grade": "A",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: Overall survival analysis showed that upregulated genes CD276, LDHB, SLC3A2, EGFR, SLC7A5, and HPRT1 are potential unfavorable prognostic markers in HNSCC, while downregulated genes EEA1, IDO1, NCOA2, REST, CCL19, and ALDH2 are potential favorable prognostic markers in HNSCC.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:38326896",
    "gene": "LDHB",
    "title": "1-Pyrroline-5-carboxylate inhibit T cell glycolysis in prostate cancer microenvironment by SHP1/PKM2/LDHB axis.",
    "journal": "Cell communication and signaling : CCS",
    "year": 2024,
    "DOI": "10.1186/s12964-024-01493-1",
    "evidence_grade": "A",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: RESULT: PKM2 and LDHB bind SHP1 in T cells, and P5C could increase the levels of p-PKM2 while having no effect on the levels of PKM2 and LDHB.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:39731912",
    "gene": "LDHB",
    "title": "HMOX1-LDHB interaction promotes ferroptosis by inducing mitochondrial dysfunction in foamy macrophages during advanced atherosclerosis.",
    "journal": "Developmental cell",
    "year": 2025,
    "DOI": "10.1016/j.devcel.2024.12.011",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Mechanically, upregulated heme oxygenase 1 (HMOX1)-lactate dehydrogenase B (LDHB) interaction enables Lon peptidase 1 (LONP1) to degrade mitochondrial transcription factor A (TFAM), leading to mitochondrial dysfunction and ferroptosis.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:34127847",
    "gene": "LEF1",
    "title": "TCF1 in T cell immunity: a broadened frontier.",
    "journal": "Nature reviews. Immunology",
    "year": 2022,
    "DOI": "10.1038/s41577-021-00563-6",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: TCF1 and its homologue LEF1 are historically known as effector transcription factors downstream of the WNT signalling pathway and are essential for early T cell development.",
    "evidence_categories": "Review; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:38589618",
    "gene": "LEF1",
    "title": "TCF1-LEF1 co-expression identifies a multipotent progenitor cell (TH2-MPP) across human allergic diseases.",
    "journal": "Nature immunology",
    "year": 2024,
    "DOI": "10.1038/s41590-024-01803-2",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: To understand these divergent outcomes, we employed bioinformatic, immunophenotyping and functional approaches with human diseased tissues, identifying an abundant population of type 2 helper T (TH2) cells with co-expression of TCF7 and LEF1, and features of chronic activation.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:42385703",
    "gene": "LEF1",
    "title": "LEF1 and niche factors determine T cell stemness across chronic diseases.",
    "journal": "Cell",
    "year": 2026,
    "DOI": "10.1016/j.cell.2026.06.022",
    "evidence_grade": "B",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: Using preclinical models of autoimmune type 1 diabetes and chronic infection, we discover that a small subset of TCF1hi T cells express the TF LEF1.",
    "evidence_categories": "Association; Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:33782480",
    "gene": "NOSIP",
    "title": "Modular genome-wide gene expression architecture shared by early traits of osteoporosis and atherosclerosis in the Young Finns Study.",
    "journal": "Scientific reports",
    "year": 2021,
    "DOI": "10.1038/s41598-021-86536-0",
    "evidence_grade": "B",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: The three most significant member genes from the significant modules were NOSIP, GXYLT2, and TRIM63 (p.adj ≤ 0.18).",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:35660746",
    "gene": "NOSIP",
    "title": "Peptide vaccine-treated, long-term surviving cancer patients harbor self-renewing tumor-specific CD8+ T cells.",
    "journal": "Nature communications",
    "year": 2022,
    "DOI": "10.1038/s41467-022-30861-z",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Tracking TCR clonotypes at the single cell level reveals in two patients that peptide-specific long-lasting CD8+ T cells acquire an effector memory phenotype that associates with cell cycle-related genes (CCNA2 and CDK1), and are characterized by high expression of IL7R, SELL, and NOSIP along with a later stage promotion of the AP-1 transcription factor network (5 years or more past vaccination).",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:42440569",
    "gene": "NOSIP",
    "title": "NOSIP overexpression promotes long-term persistence of CD8+ T cells during chronic infection.",
    "journal": "Frontiers in immunology",
    "year": 2026,
    "DOI": "10.3389/fimmu.2026.1755657",
    "evidence_grade": "B",
    "study_type": "Laboratory/animal study",
    "summary": "PubMed abstract evidence: In this study, we demonstrate that overexpression of nitric oxide synthase-interacting protein (NOSIP) enhances the persistence of antigen-specific CD8+ T cells under chronic antigen stimulation.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:22706993",
    "gene": "PIK3IP1",
    "title": "Inhibition of T-cell activation by PIK3IP1.",
    "journal": "European journal of immunology",
    "year": 2012,
    "DOI": "10.1002/eji.201141653",
    "evidence_grade": "B",
    "study_type": "Human laboratory study",
    "summary": "PubMed abstract evidence: PIK3IP1 (PI3K interacting protein 1) is a recently described transmembrane protein that has the ability to bind the catalytic protein p110 and prevent its activation by the p85 family adaptor proteins.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:33024547",
    "gene": "PIK3IP1",
    "title": "Control of T lymphocyte fate decisions by PI3K signaling.",
    "journal": "F1000Research",
    "year": 2020,
    "DOI": "10.12688/f1000research.26928.1",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Here we review recent key findings regarding both the triggering/enhancement of PI3K signals (via BCAP and ICOS) as well as their regulation (via PIK3IP1 and PHLPP) and how these signals integrate and determine cellular processes.",
    "evidence_categories": "Review; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:41571844",
    "gene": "PIK3IP1",
    "title": "GANT61 suppresses proliferation and induces apoptosis in ALK-Positive anaplastic large cell lymphoma via modulating the Hh-PIK3IP1-Akt signaling axis.",
    "journal": "Annals of hematology",
    "year": 2026,
    "DOI": "10.1007/s00277-026-06827-2",
    "evidence_grade": "B",
    "study_type": "Human laboratory study",
    "summary": "PubMed abstract evidence: Protein expression levels of apoptosis-related markers (Bcl-2, Bax, caspase-3, cleaved caspase-3) and signaling molecules (Gli1, PIK3IP1, Akt, phosphorylated Akt) were quantitatively examined by western blotting.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:38229689",
    "gene": "PRKCQ-AS1",
    "title": "Analysis of Immune and Prognostic-Related lncRNA PRKCQ-AS1 for Predicting Prognosis and Regulating Effect in Sepsis.",
    "journal": "Journal of inflammation research",
    "year": 2024,
    "DOI": "10.2147/JIR.S433057",
    "evidence_grade": "C",
    "study_type": "Other PubMed-indexed study",
    "summary": "PubMed abstract evidence: Subsequently, Subsequently, lncRNA PRKCQ-AS1 was identified as the regulator for further investigation in sepsis.",
    "evidence_categories": "Association; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:38243290",
    "gene": "PRKCQ-AS1",
    "title": "Expression profile analysis of LncRNAs and mRNAs in pre-receptive endometrium of women with polycystic ovary syndrome undergoing in vitro fertilization-embryo transfer.",
    "journal": "BMC medical genomics",
    "year": 2024,
    "DOI": "10.1186/s12920-024-01806-w",
    "evidence_grade": "C",
    "study_type": "Human laboratory study",
    "summary": "PubMed abstract evidence: qRT-PCR was performed to detect the expression of 9 lncRNAs, and validated that the expression of these 7 lncRNAs IDH1-AS1, PCAT14, FTX, DANCR, PRKCQ-AS1, SNHG8, TPT1-AS1 were significantly enhanced among PCOS patients.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40433053",
    "gene": "PRKCQ-AS1",
    "title": "Identification of PRKCQ-AS1 as a Keratinocyte-Derived Exosomal lncRNA That Promotes Th17 Differentiation and IL-17 secretion in Psoriasis Through Bioinformatics, Machine Learning Algorithms, and Cell Experiments.",
    "journal": "Journal of inflammation research",
    "year": 2025,
    "DOI": "10.2147/JIR.S521553",
    "evidence_grade": "C",
    "study_type": "Computational study",
    "summary": "PubMed abstract evidence: RESULTS: We identified 10 exosome-related ncRNAs, including PRKCQ-AS1, and constructed five machine learning models with excellent diagnostic performance, emphasizing PRKCQ-AS1's significance.",
    "evidence_categories": "Association; Mechanism; Biomarker"
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
