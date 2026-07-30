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
2

Current cell-type annotation:
IL7R+ memory/helper T cells

Classification-model prediction:
Not available: Notebook 05 did not export a cluster-level prediction. The selected cell-level model was XGBoost.

Classification confidence, if available:
Not available as a cluster-level probability. Held-out IL7R+ memory/helper T cells metrics for XGBoost: precision=0.833, recall=0.917, F1=0.873, support=60. These are evaluation metrics against expression-derived labels, not a cluster-level probability.

==================================================
DATASET OBSERVATIONS
==================================================

Representative marker genes:
IL32, IL7R, CD3D, LTB, CD3E, CD2, AQP3, LDHB, TRAT1, SPOCK2

Marker-gene statistics:
representative_rank,gene,avg_log2FC,adjusted_p_value,pct_in,pct_out,specificity_delta,marker_score,selection_tier
1,IL32,2.521231,7.213826e-91,0.933555,0.439587,0.493967,24.90812,primary: pct_in >= 0.20
2,IL7R,2.425345,1.521022e-74,0.76412,0.295678,0.468442,22.722657,primary: pct_in >= 0.20
3,CD3D,2.239499,1.647630e-73,0.906977,0.405697,0.501279,22.452293,primary: pct_in >= 0.20
4,LTB,2.441446,3.179300e-104,0.980066,0.622299,0.357768,17.469413,primary: pct_in >= 0.20
5,CD3E,1.974084,8.421711e-60,0.82392,0.38556,0.43836,17.307204,primary: pct_in >= 0.20
6,CD2,2.075754,5.706686e-45,0.624585,0.227898,0.396687,16.468491,primary: pct_in >= 0.20
7,AQP3,2.529479,2.432166e-28,0.406977,0.096267,0.31071,15.718668,primary: pct_in >= 0.20
8,LDHB,1.99006,6.116035e-93,0.958472,0.591356,0.367116,14.611665,primary: pct_in >= 0.20
9,TRAT1,2.327359,3.042077e-26,0.408638,0.103635,0.305003,14.197043,primary: pct_in >= 0.20
10,SPOCK2,2.015473,5.018826e-25,0.438538,0.141454,0.297084,11.975311,primary: pct_in >= 0.20


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
    "gene": "IL7R",
    "official_gene_name": "IL7R",
    "immune_function": "The selected PubMed collection discusses IL7R in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for IL7R, but they do not by themselves establish what the gene does in this PBMC3k cluster."
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
    "gene": "LTB",
    "official_gene_name": "LTB",
    "immune_function": "The selected PubMed collection discusses LTB in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for LTB, but they do not by themselves establish what the gene does in this PBMC3k cluster."
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
    "gene": "CD2",
    "official_gene_name": "CD2",
    "immune_function": "The selected PubMed collection discusses CD2 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Selected evidence is limited and does not meet the thresholds for grades A–D.",
    "plain_language_note": "Selected PubMed records provide context for CD2, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "AQP3",
    "official_gene_name": "AQP3",
    "immune_function": "The selected PubMed collection discusses AQP3 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for AQP3, but they do not by themselves establish what the gene does in this PBMC3k cluster."
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
    "gene": "TRAT1",
    "official_gene_name": "TRAT1",
    "immune_function": "The selected PubMed collection discusses TRAT1 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for TRAT1, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "SPOCK2",
    "official_gene_name": "SPOCK2",
    "immune_function": "The selected PubMed collection discusses SPOCK2 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for SPOCK2, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  }
]

Cluster-level literature summary:
# Literature Reference Report — Cluster 2: IL7R+ memory/helper T cells

> This document organizes evidence for later analysis. It does not interpret the genes as a combined program and does not make a biological or clinical conclusion.

## Selected Genes

IL32, IL7R, CD3D, LTB, CD3E, CD2, AQP3, LDHB, TRAT1, SPOCK2

## Dataset Boundary

The genes were selected from the Phase 6 marker ranking for cluster 2. Marker statistics are dataset observations. All publication claims come from the verified references table. Publication contexts do not describe or diagnose the PBMC3k source.

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
| IL32 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| IL7R | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| CD3D | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| LTB | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| CD3E | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| CD2 | E | 3 | Selected evidence is limited and does not meet the thresholds for grades A–D. |
| AQP3 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| LDHB | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| TRAT1 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| SPOCK2 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |

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
    "gene": "IL32",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "IL7R",
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
    "gene": "LTB",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "CD3E",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "CD2",
    "evidence_grade": "E",
    "publication_count": 3,
    "grade_explanation": "Selected evidence is limited and does not meet the thresholds for grades A–D."
  },
  {
    "gene": "AQP3",
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
    "gene": "TRAT1",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "SPOCK2",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  }
]

Verified references:
[
  {
    "reference_id": "PMID:36010640",
    "gene": "AQP3",
    "title": "The Water Transport System in Astrocytes-Aquaporins.",
    "journal": "Cells",
    "year": 2022,
    "DOI": "10.3390/cells11162564",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Various subtypes of AQPs (AQP1, AQP3, AQP4, AQP5, AQP8 and AQP9) have been reported to be expressed in astrocytes, and the expressions and subcellular localizations of AQPs in astrocytes are highly correlated with both their physiological and pathophysiological functions.",
    "evidence_categories": "Review; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:38279209",
    "gene": "AQP3",
    "title": "AQP3 and AQP9-Contrary Players in Sepsis?",
    "journal": "International journal of molecular sciences",
    "year": 2024,
    "DOI": "10.3390/ijms25021209",
    "evidence_grade": "B",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: In immune cells, AQP3 and AQP9 are of special interest.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:38726865",
    "gene": "AQP3",
    "title": "SCFFBXW5-mediated degradation of AQP3 suppresses autophagic cell death through the PDPK1-AKT-MTOR axis in hepatocellular carcinoma cells.",
    "journal": "Autophagy",
    "year": 2024,
    "DOI": "10.1080/15548627.2024.2353497",
    "evidence_grade": "B",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: AQP3 (aquaporin 3 (Gill blood group)), a member of the AQP family, is an aquaglyceroporin which transports water, glycerol and small solutes across the plasma membrane.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:2482743",
    "gene": "CD2",
    "title": "The CD2-LFA-3 and LFA-1-ICAM pathways: relevance to T-cell recognition.",
    "journal": "Immunology today",
    "year": 1989,
    "DOI": "10.1016/0167-5699(89)90039-X",
    "evidence_grade": "E",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: In this review Malegapuru Makgoba, Martin Sanders and Stephen Shaw focus primarily on the two molecular pathways of lymphocyte adhesion that have been shown to play a critical role in facilitation of antigen-specific recognition, namely CD2 and its ligand, lymphocyte function associated antigen-3 (LFA-3), and LFA-1 and its ligand, intercellular adhesion molecule-1 (ICAM-1).",
    "evidence_categories": "Review; Mechanism"
  },
  {
    "reference_id": "PMID:7693022",
    "gene": "CD2",
    "title": "T cell adhesion, avidity regulation and signaling: a molecular analysis of CD2.",
    "journal": "Seminars in immunology",
    "year": 1993,
    "DOI": "10.1006/smim.1993.1029",
    "evidence_grade": "E",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: One such co-receptor molecule is CD2, a T cell glycoprotein that not only participates in T cell activation but also provides the T cell with a major adhesion pathway whose avidity is regulated by TcR triggering.",
    "evidence_categories": "Review; Mechanism"
  },
  {
    "reference_id": "PMID:37798328",
    "gene": "CD2",
    "title": "An \"off-the-shelf\" CD2 universal CAR-T therapy for T-cell malignancies.",
    "journal": "Leukemia",
    "year": 2023,
    "DOI": "10.1038/s41375-023-02039-z",
    "evidence_grade": "E",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: To broaden the use of CAR-T cells in pan T-cell malignancies, we developed an allogeneic \"universal\" CD2-targeting CAR-T cell (UCART2), in which the CD2 antigen is deleted to prevent fratricide, and the T-cell receptor is removed to prevent GvHD.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
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
    "reference_id": "PMID:38956225",
    "gene": "IL7R",
    "title": "Lrp10 suppresses IL7R limiting CD8 T cell homeostatic expansion and anti-tumor immunity.",
    "journal": "EMBO reports",
    "year": 2024,
    "DOI": "10.1038/s44319-024-00191-w",
    "evidence_grade": "A",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: T-cell activation induces Lrp10 expression, which post-translationally suppresses IL7 receptor (IL7R) levels.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:39982469",
    "gene": "IL7R",
    "title": "Single-Cell Transcriptomic Profile of Innate Cell Populations in Mesenteric Lymph Nodes of Inflammatory Bowel Disease Patients.",
    "journal": "Inflammatory bowel diseases",
    "year": 2025,
    "DOI": "10.1093/ibd/izaf017",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Among NK/ILC clusters, we identified a cytotoxic ILC subset (IL7R, KLRD1, GNLY), previously not reported in MLNs, reminiscent of cytotoxic ILC1-like cells found in inflamed gut mucosa.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40993240",
    "gene": "IL7R",
    "title": "A single-cell and spatial genomics atlas of human skin fibroblasts reveals shared disease-related fibroblast subtypes across tissues.",
    "journal": "Nature immunology",
    "year": 2025,
    "DOI": "10.1038/s41590-025-02267-8",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: The second, F6: inflammatory myofibroblasts (IL11+MMP1+CXCL8+IL7R+), characterizes early human skin wounds, inflammatory diseases with scarring risk and cancer.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
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
    "reference_id": "PMID:33748804",
    "gene": "LTB",
    "title": "Identifying CNS-colonizing T cells as potential therapeutic targets to prevent progression of multiple sclerosis.",
    "journal": "Med (New York, N.Y.)",
    "year": 2021,
    "DOI": "10.1016/j.medj.2021.01.006",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: FINDINGS: We identify a specific pathogenic CD161+/lymphotoxin beta (LTB)+ T cell population that resides in brains of progressive MS patients.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:39982469",
    "gene": "LTB",
    "title": "Single-Cell Transcriptomic Profile of Innate Cell Populations in Mesenteric Lymph Nodes of Inflammatory Bowel Disease Patients.",
    "journal": "Inflammatory bowel diseases",
    "year": 2025,
    "DOI": "10.1093/ibd/izaf017",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: DC clusters included 3 newly characterized DC clusters such as CD1c/CD163/VCAN/CD64-expressing DC3; AXL-expressing DCs; and a CD103+ DC subset, expressing LTB, S100B, and IL22RA2 (encoding IL22BP).",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41241792",
    "gene": "LTB",
    "title": "Single-cell transcriptomic analysis reveals T cell heterogeneity and metabolic reprogramming in human immune-mediated glomerulonephritis.",
    "journal": "Autoimmunity",
    "year": 2025,
    "DOI": "10.1080/08916934.2025.2582720",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Notably, LTB⁺ memory T cells (LTB⁺ Tm) were selectively elevated in IgAN and LN patients.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:37165378",
    "gene": "SPOCK2",
    "title": "Integrated bulk and single-cell RNA-sequencing reveals SPOCK2 as a novel biomarker gene in the development of congenital pulmonary airway malformation.",
    "journal": "Respiratory research",
    "year": 2023,
    "DOI": "10.1186/s12931-023-02436-z",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: By combining the analysis of the expression dataset from RNA-seq and scRNA-seq, SPOCK2, STX11, and ZNF331 were highlighted in CPAM.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:39115722",
    "gene": "SPOCK2",
    "title": "Spock2 Functions as a Key Time-Series Gene of Endothelial Cells in Sepsis-Induced Cardiomyopathy.",
    "journal": "Journal of cardiovascular pharmacology",
    "year": 2024,
    "DOI": "10.1097/FJC.0000000000001577",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: The study highlighted Spock2, S100a9, S100a8, and Xdh as differential genes specific to endothelial cells in a time-dependent manner.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:39741186",
    "gene": "SPOCK2",
    "title": "SPOCK2 controls the proliferation and function of immature pancreatic β-cells through MMP2.",
    "journal": "Experimental & molecular medicine",
    "year": 2025,
    "DOI": "10.1038/s12276-024-01380-2",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Through bidirectional expression modulation and single-cell RNA-seq, we identified SPOCK2, an ECM protein, as an inhibitor of immature β-cell proliferation.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:36184729",
    "gene": "TRAT1",
    "title": "The Roles and Mechanisms of TRAT1 in the Progression of Non-Small Cell Lung Cancer.",
    "journal": "Current medical science",
    "year": 2022,
    "DOI": "10.1007/s11596-022-2625-1",
    "evidence_grade": "A",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: OBJECTIVE: T cell receptor-associated transmembrane adaptor 1 (TRAT1) is one of the hub genes regulating T cell receptors (TCRs).",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41074026",
    "gene": "TRAT1",
    "title": "T cell receptor associated transmembrane adaptor 1 (TRAT1) modulates human Th17 and Treg responses via PI3-kinase and STAT dependent mechanisms.",
    "journal": "Cell communication and signaling : CCS",
    "year": 2025,
    "DOI": "10.1186/s12964-025-02429-z",
    "evidence_grade": "A",
    "study_type": "Human laboratory study",
    "summary": "PubMed abstract evidence: T cell Receptor Associated Transmembrane Adaptor 1 (TRAT1) has been implicated in modulating TCR complex stability, but its functional role in human effector and regulatory CD4⁺ T cell subsets remains poorly understood.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41076046",
    "gene": "TRAT1",
    "title": "The BET degrader BETd-246 demonstrated significant anti-tumor efficacy in T-cell acute lymphoblastic leukemia by inhibiting TRAT1.",
    "journal": "Experimental cell research",
    "year": 2025,
    "DOI": "10.1016/j.yexcr.2025.114791",
    "evidence_grade": "A",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: RNA sequencing analysis indicated significant downregulation of T-cell receptor (TCR)-associated transmembrane adaptor 1 (TRAT1) expression in T-ALL cells treated with BETd-246.",
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
