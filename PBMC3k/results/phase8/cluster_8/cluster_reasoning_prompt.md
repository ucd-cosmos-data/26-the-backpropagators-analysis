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
8

Current cell-type annotation:
Platelets

Classification-model prediction:
Not available: Notebook 05 did not export a cluster-level prediction. The selected cell-level model was XGBoost.

Classification confidence, if available:
Not available as a cluster-level probability. Held-out Platelets metrics for XGBoost: precision=1.000, recall=1.000, F1=1.000, support=1. These are evaluation metrics against expression-derived labels, not a cluster-level probability.

==================================================
DATASET OBSERVATIONS
==================================================

Representative marker genes:
PPBP, PF4, GNG11, SDPR, SPARC, CD9, GP9, ITGA2B, HIST1H2AC, NRGN

Marker-gene statistics:
representative_rank,gene,avg_log2FC,adjusted_p_value,pct_in,pct_out,specificity_delta,marker_score,selection_tier
1,PPBP,13.376807,5.940330e-06,1.0,0.024743,0.975257,68.179947,primary: pct_in >= 0.20
2,PF4,12.977622,5.940330e-06,1.0,0.01142,0.98858,67.048975,primary: pct_in >= 0.20
3,GNG11,12.698402,5.940330e-06,1.0,0.010278,0.989722,65.68217,primary: pct_in >= 0.20
4,SDPR,12.011179,5.940330e-06,1.0,0.011801,0.988199,62.031946,primary: pct_in >= 0.20
5,SPARC,11.213252,5.940330e-06,1.0,0.009136,0.990864,58.067192,primary: pct_in >= 0.20
6,CD9,10.211339,5.940330e-06,1.0,0.025504,0.974496,52.005315,primary: pct_in >= 0.20
7,GP9,12.469261,3.095606e-05,0.909091,0.002284,0.906807,50.987097,primary: pct_in >= 0.20
8,ITGA2B,12.441929,3.095606e-05,0.909091,0.001903,0.907188,50.896692,primary: pct_in >= 0.20
9,HIST1H2AC,9.829602,5.940330e-06,1.0,0.031976,0.968024,49.72873,primary: pct_in >= 0.20
10,NRGN,9.031865,5.940330e-06,1.0,0.027788,0.972212,45.890565,primary: pct_in >= 0.20


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
    "gene": "PPBP",
    "official_gene_name": "PPBP",
    "immune_function": "The selected PubMed collection discusses PPBP in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for PPBP, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "PF4",
    "official_gene_name": "PF4",
    "immune_function": "The selected PubMed collection discusses PF4 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient.",
    "plain_language_note": "Selected PubMed records provide context for PF4, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "GNG11",
    "official_gene_name": "GNG11",
    "immune_function": "The selected PubMed collection discusses GNG11 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for GNG11, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "SDPR",
    "official_gene_name": "SDPR",
    "immune_function": "The selected PubMed collection discusses SDPR in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for SDPR, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "SPARC",
    "official_gene_name": "SPARC",
    "immune_function": "The selected PubMed collection discusses SPARC in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Selected evidence is limited and does not meet the thresholds for grades A–D.",
    "plain_language_note": "Selected PubMed records provide context for SPARC, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "CD9",
    "official_gene_name": "CD9",
    "immune_function": "The selected PubMed collection discusses CD9 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for CD9, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "GP9",
    "official_gene_name": "GP9",
    "immune_function": "The selected PubMed collection discusses GP9 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for GP9, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "ITGA2B",
    "official_gene_name": "ITGA2B",
    "immune_function": "The selected PubMed collection discusses ITGA2B in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for ITGA2B, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "HIST1H2AC",
    "official_gene_name": "HIST1H2AC",
    "immune_function": "The selected PubMed collection discusses HIST1H2AC in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient.",
    "plain_language_note": "Selected PubMed records provide context for HIST1H2AC, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "NRGN",
    "official_gene_name": "NRGN",
    "immune_function": "The selected PubMed collection discusses NRGN in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for NRGN, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  }
]

Cluster-level literature summary:
# Literature Reference Report — Cluster 8: Platelets

> This document organizes evidence for later analysis. It does not interpret the genes as a combined program and does not make a biological or clinical conclusion.

## Selected Genes

PPBP, PF4, GNG11, SDPR, SPARC, CD9, GP9, ITGA2B, HIST1H2AC, NRGN

## Dataset Boundary

The genes were selected from the Phase 6 marker ranking for cluster 8. Marker statistics are dataset observations. All publication claims come from the verified references table. Publication contexts do not describe or diagnose the PBMC3k source.

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
| PPBP | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| PF4 | C | 3 | Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient. |
| GNG11 | B | 3 | Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade. |
| SDPR | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| SPARC | E | 3 | Selected evidence is limited and does not meet the thresholds for grades A–D. |
| CD9 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| GP9 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| ITGA2B | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| HIST1H2AC | C | 2 | Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient. |
| NRGN | B | 3 | Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade. |

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
    "gene": "PPBP",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "PF4",
    "evidence_grade": "C",
    "publication_count": 3,
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient."
  },
  {
    "gene": "GNG11",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "SDPR",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "SPARC",
    "evidence_grade": "E",
    "publication_count": 3,
    "grade_explanation": "Selected evidence is limited and does not meet the thresholds for grades A–D."
  },
  {
    "gene": "CD9",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "GP9",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "ITGA2B",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "HIST1H2AC",
    "evidence_grade": "C",
    "publication_count": 2,
    "grade_explanation": "Laboratory or animal evidence predominates (1 selected experimental study/studies); repeated human evidence is insufficient."
  },
  {
    "gene": "NRGN",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade."
  }
]

Verified references:
[
  {
    "reference_id": "PMID:39366998",
    "gene": "CD9",
    "title": "Distinctive CD39+CD9+ lung interstitial macrophages suppress IL-23/Th17-mediated neutrophilic asthma by inhibiting NETosis.",
    "journal": "Nature communications",
    "year": 2024,
    "DOI": "10.1038/s41467-024-53038-2",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: In our neutrophil-dominant asthma (NDA) model, single-cell RNA-seq analysis identifies a subpopulation of CD39+CD9+ interstitial macrophages (IMs) suppressed by IL-23 in NDA conditions but increased by an IL-23 inhibitor αIL-23p19.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:39873228",
    "gene": "CD9",
    "title": "CCN5 suppresses injury-induced vascular restenosis by inhibiting smooth muscle cell proliferation and facilitating endothelial repair via thymosin β4 and Cd9 pathway.",
    "journal": "European heart journal",
    "year": 2025,
    "DOI": "10.1093/eurheartj/ehae911",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Also, CCN5rp promoted EC repair to suppress neointimal hyperplasia via interaction with Cd9 extracellular domain.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41566006",
    "gene": "CD9",
    "title": "Diversity and immune dynamics of choroid plexus macrophages are shaped by distinct developmental origins.",
    "journal": "Nature neuroscience",
    "year": 2026,
    "DOI": "10.1038/s41593-025-02158-z",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Using single-cell transcriptomics combined with lineage and spatial tracing methods, we identified three biologically distinct populations of choroid plexus macrophages, defined by differential expression of CD163, MHCII or CD9.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:34113163",
    "gene": "GNG11",
    "title": "Assessment of Significant Pathway Signaling and Prognostic Value of GNG11 in Ovarian Serous Cystadenocarcinoma.",
    "journal": "International journal of general medicine",
    "year": 2021,
    "DOI": "10.2147/IJGM.S314911",
    "evidence_grade": "B",
    "study_type": "Computational study",
    "summary": "PubMed abstract evidence: BACKGROUND: GNG11 (G protein subunit gamma 11) is a member of guanine nucleotide-binding protein (G protein) gamma family.",
    "evidence_categories": "Association; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:40383719",
    "gene": "GNG11",
    "title": "Identification of hub biomarkers in coronary artery disease patients using machine learning and bioinformatic analyses.",
    "journal": "Scientific reports",
    "year": 2025,
    "DOI": "10.1038/s41598-025-02123-7",
    "evidence_grade": "B",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: Eleven hub biomarkers (ITM2B, GNA15, PLAU, GNG11, HIST1H2BH, SLC11A1, RPS7, DDIT4, CD83, GNLY, and S100A12) were identified and associated with CD8 + T cells and NK cells.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:42135635",
    "gene": "GNG11",
    "title": "Identification of key genes related to macrophages and metabolic reprogramming in myocardial infarct based on single-cell and bulk transcriptomics data and experimental validation.",
    "journal": "BMC cardiovascular disorders",
    "year": 2026,
    "DOI": "10.1186/s12872-026-05822-9",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: The key genes (ABCG1, GNG11, and RPL24) were successfully identified.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:24934643",
    "gene": "GP9",
    "title": "Spectrum of the mutations in Bernard-Soulier syndrome.",
    "journal": "Human mutation",
    "year": 2014,
    "DOI": "10.1002/humu.22607",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Most of the mutations identified in the genes encoding for the GP1BA (GPIbα), GP1BB (GPIbβ), and GP9 (GPIX) subunits prevent expression of the complex at the platelet membrane or more rarely its interaction with VWF.",
    "evidence_categories": "Review; Biomarker"
  },
  {
    "reference_id": "PMID:29119855",
    "gene": "GP9",
    "title": "Two novel variants of uncertain significance in GP9 associated with Bernard-Soulier syndrome: Are they true mutations?",
    "journal": "Platelets",
    "year": 2018,
    "DOI": "10.1080/09537104.2017.1371288",
    "evidence_grade": "B",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: A large number of mutations, sometimes involving the GP9 gene, have been described as possibly responsible for the disease.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:32030720",
    "gene": "GP9",
    "title": "Bernard-Soulier syndrome: first human case due to a homozygous deletion of GP9 gene.",
    "journal": "British journal of haematology",
    "year": 2020,
    "DOI": "10.1111/bjh.16374",
    "evidence_grade": "B",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: The publication title identifies GP9 as its subject: Bernard-Soulier syndrome: first human case due to a homozygous deletion of GP9 gene.",
    "evidence_categories": "Association; Experimental evidence"
  },
  {
    "reference_id": "PMID:28178938",
    "gene": "HIST1H2AC",
    "title": "Messenger RNA and MicroRNA transcriptomic signatures of cardiometabolic risk factors.",
    "journal": "BMC genomics",
    "year": 2017,
    "DOI": "10.1186/s12864-017-3533-9",
    "evidence_grade": "C",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: Four mRNAs (FAM13A, CSF2RB, HIST1H2AC, WNK1) were associated with all 6 CM traits (FDR < 0.001) and four miRNAs (miR-197-3p, miR-328, miR-505-5p, miR-145-5p) were associated with four CM traits (FDR < 0.05).",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:30782612",
    "gene": "HIST1H2AC",
    "title": "The global clonal complexity of the murine blood system declines throughout life and after serial transplantation.",
    "journal": "Blood",
    "year": 2019,
    "DOI": "10.1182/blood-2018-09-873059",
    "evidence_grade": "C",
    "study_type": "Laboratory/animal study",
    "summary": "PubMed abstract evidence: Whole-exome sequencing of serially transplanted aged and young hematopoietic clones confirmed oligoclonal hematopoiesis and revealed mutations in at least 27 genes, including nonsense, missense, and deletion mutations in Bcl11b, Hist1h2ac, Npy2r, Notch3, Ptprr, and Top2b.",
    "evidence_categories": "Association; Experimental evidence"
  },
  {
    "reference_id": "PMID:27965976",
    "gene": "ITGA2B",
    "title": "Identification of ITGA2B and ITGB3 Single-Nucleotide Polymorphisms and Their Influences on the Platelet Function.",
    "journal": "BioMed research international",
    "year": 2016,
    "DOI": "10.1155/2016/5675084",
    "evidence_grade": "B",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: The aim of the study was to investigate ITGA2B and ITGB3 genetic polymorphisms and to evaluate the variability in the platelet function in healthy Chinese subjects.",
    "evidence_categories": "Association; Experimental evidence"
  },
  {
    "reference_id": "PMID:41503871",
    "gene": "ITGA2B",
    "title": "ITGA2B/ITGB3-Related Macrothrombocytopenia Associated With Gain-of-Function Mutations in ITGA2B or ITGB3 Genes.",
    "journal": "Journal of cellular and molecular medicine",
    "year": 2026,
    "DOI": "10.1111/jcmm.70988",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: While classical GT typically exhibits normal platelet counts and morphology, very rare mutations in ITGA2B (encoding αIIb) and/or ITGB3 (encoding β3) cause macrothrombocytopenia or increased platelet anisotropy (heterogeneity of platelet size and morphology).",
    "evidence_categories": "Review"
  },
  {
    "reference_id": "PMID:41944931",
    "gene": "ITGA2B",
    "title": "A CREM-ITGA2B-MAPK axis drives proliferation and invasiveness in gastric cancer: insights from single-cell analysis.",
    "journal": "Cellular oncology (Dordrecht, Netherlands)",
    "year": 2026,
    "DOI": "10.1007/s13402-026-01189-3",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: CREM activation promotes aggressive tumor phenotypes and correlates with poorer patient outcomes by regulating the ITGA2B promoter and MAPK signaling pathway.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:31234132",
    "gene": "NRGN",
    "title": "NRGN, S100B and GFAP levels are significantly increased in patients with structural lesions resulting from mild traumatic brain injuries.",
    "journal": "Clinical neurology and neurosurgery",
    "year": 2019,
    "DOI": "10.1016/j.clineuro.2019.105380",
    "evidence_grade": "B",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: OBJECTIVE: To determine whether serum neurogranin (NRGN), glial fibrillary acidic protein (GFAP), and calcium-binding protein S100 beta (S100B) levels are associated with traumatic intracranial lesions compared to computed tomography (CT) findings of patients with mild traumatic brain injury (mTBI).",
    "evidence_categories": "Association; Experimental evidence"
  },
  {
    "reference_id": "PMID:41554902",
    "gene": "NRGN",
    "title": "Single-cell characterization of the adult male hippocampus suggests a prominent, and cell-type specific, role for Nrgn and Sgk1 in response to a social stressor.",
    "journal": "Molecular psychiatry",
    "year": 2026,
    "DOI": "10.1038/s41380-025-03417-y",
    "evidence_grade": "B",
    "study_type": "Laboratory/animal study",
    "summary": "PubMed abstract evidence: We found previously unknown, cell-type specific, molecular signatures of a single prolonged social defeat stress response and identified Nrgn and SgK1 as key regulators in stress-responsive glutamatergic neurons, oligodendrocytes, astrocytes, and endothelial cells.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41637423",
    "gene": "NRGN",
    "title": "Identification of common genes and biomarkers between Dermatomyositis and rheumatoid arthritis through integrated bioinformatics.",
    "journal": "PloS one",
    "year": 2026,
    "DOI": "10.1371/journal.pone.0340617",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Four core genes (JUNB, NRGN, HCP5, RARRES3) were prioritised; HCP5 and RARRES3 showed significant differential expression and diagnostic performance in external datasets (AUC 0.634-0.846).",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:38008700",
    "gene": "PF4",
    "title": "Platelet factor 4(PF4) and its multiple roles in diseases.",
    "journal": "Blood reviews",
    "year": 2024,
    "DOI": "10.1016/j.blre.2023.101155",
    "evidence_grade": "C",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Platelet factor 4 (PF4) combines with heparin to form an antigen that could produce IgG antibodies and participate in heparin-induced thrombocytopenia (HIT).",
    "evidence_categories": "Review; Mechanism"
  },
  {
    "reference_id": "PMID:39025985",
    "gene": "PF4",
    "title": "Proteomic screening identifies PF4/Cxcl4 as a critical driver of myelofibrosis.",
    "journal": "Leukemia",
    "year": 2024,
    "DOI": "10.1038/s41375-024-02354-z",
    "evidence_grade": "C",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: The chemokine Platelet Factor 4 (PF4)/Cxcl4 was up-regulated in all proteomes and increased in plasma and BM fluids of fibrotic mice.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40589323",
    "gene": "PF4",
    "title": "Anti-PF4 disorders: Pathogenesis, diagnosis and treatment.",
    "journal": "British journal of haematology",
    "year": 2025,
    "DOI": "10.1111/bjh.20216",
    "evidence_grade": "C",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Platelet factor 4 (PF4) is a cationic protein, able to form complexes with negatively charged molecules upon its self-assembly into PF4 tetramers.",
    "evidence_categories": "Review; Mechanism"
  },
  {
    "reference_id": "PMID:28420383",
    "gene": "PPBP",
    "title": "PPBP and DEFA1/DEFA3 genes in hyperlipidaemia as feasible synergistic inflammatory biomarkers for coronary heart disease.",
    "journal": "Lipids in health and disease",
    "year": 2017,
    "DOI": "10.1186/s12944-017-0471-0",
    "evidence_grade": "A",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: RESULTS: α-defensin (DEFA1/DEFA3), pro-platelet basic protein (PPBP), and beta and alpha2 hemoglobin mRNA expression was significantly increased in H and CHD groups compared with controls, but only plasma PPBP and α-defensin proteins were correspondingly increased.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:35734636",
    "gene": "PPBP",
    "title": "PPBP gene as a biomarker for coronary heart disease risk in postmenopausal Thai women.",
    "journal": "PeerJ",
    "year": 2022,
    "DOI": "10.7717/peerj.13615",
    "evidence_grade": "A",
    "study_type": "Human study",
    "summary": "PubMed abstract evidence: We recently reported that the PPBP and DEFA1/DEFA3 genes may be feasible synergistic biomarkers for CHD risk in Thai men with hyperlipidemia.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41258106",
    "gene": "PPBP",
    "title": "Migration of CD8 + TSCM cells into intestine via PPBP-CXCR2 axis increases host stress susceptibility by inhibiting gut microbiome-derived homovanillic acid.",
    "journal": "Nature communications",
    "year": 2025,
    "DOI": "10.1038/s41467-025-65112-4",
    "evidence_grade": "A",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: The publication title identifies PPBP as its subject: Migration of CD8 + TSCM cells into intestine via PPBP-CXCR2 axis increases host stress susceptibility by inhibiting gut microbiome-derived homovanillic acid.",
    "evidence_categories": "Association; Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:19852682",
    "gene": "SDPR",
    "title": "The platelet protein kinase C substrate pleckstrin binds directly to SDPR protein.",
    "journal": "Platelets",
    "year": 2009,
    "DOI": "10.3109/09537100903137314",
    "evidence_grade": "A",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: Our recent studies have led to the identification of a novel pleckstrin-binding protein, serum deprivation response protein (SDPR), by co-immunoprecipitation, GST-pulldowns and nanospray quadruple time of flight mass spectrometry.",
    "evidence_categories": "Association; Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:30522007",
    "gene": "SDPR",
    "title": "Temporal dynamics of cortisol-associated changes in mRNA expression of glucocorticoid responsive genes FKBP5, GILZ, SDPR, PER1, PER2 and PER3 in healthy humans.",
    "journal": "Psychoneuroendocrinology",
    "year": 2019,
    "DOI": "10.1016/j.psyneuen.2018.11.033",
    "evidence_grade": "A",
    "study_type": "Human laboratory study",
    "summary": "PubMed abstract evidence: The current study aims to investigate the temporal association between unstimulated, diurnal cortisol secretion and the expression of selected GR-target genes (PER1, PER2, PER3, FKBP5, GILZ and SDPR) in vivo to determine the timing of the most pronounced coupling between cortisol and mRNA expression.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:37291580",
    "gene": "SDPR",
    "title": "Exploring the molecular mechanism of comorbidity of autism spectrum disorder and inflammatory bowel disease by combining multiple data sets.",
    "journal": "Journal of translational medicine",
    "year": 2023,
    "DOI": "10.1186/s12967-023-04218-z",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: A total of 98 common genes related to ASD and IBD were identified by weighted gene coexpression network analysis (WGCNA), and 4 hub genes were obtained by intersection with the 7 intersecting DEGs, which were PDGFC, CA2, GUCY1B3 and SDPR.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:37220502",
    "gene": "SPARC",
    "title": "Sparcl1 and Atherosclerosis.",
    "journal": "Journal of inflammation research",
    "year": 2023,
    "DOI": "10.2147/JIR.S406907",
    "evidence_grade": "E",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Sparcl-1 is a cysteine-rich secretory stromal cell protein present in the extracellular matrix and belongs to the Sparc family of proteins.",
    "evidence_categories": "Review; Mechanism"
  },
  {
    "reference_id": "PMID:39904988",
    "gene": "SPARC",
    "title": "Single-cell transcriptomics reveals novel chondrocyte and osteoblast subtypes and their role in knee osteoarthritis pathogenesis.",
    "journal": "Signal transduction and targeted therapy",
    "year": 2025,
    "DOI": "10.1038/s41392-025-02136-8",
    "evidence_grade": "E",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Sparc+ osteoblasts have negatively regulated bone mineralization and osteoblastic differentiation, aggravated the pathological remodeling of subchondral bone, and promoted the progression of KOA.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40104024",
    "gene": "SPARC",
    "title": "Single-cell RNA sequencing-guided engineering of mitochondrial therapies for intervertebral disc degeneration by regulating mtDNA/SPARC-STING signaling.",
    "journal": "Bioactive materials",
    "year": 2025,
    "DOI": "10.1016/j.bioactmat.2025.02.036",
    "evidence_grade": "E",
    "study_type": "Other PubMed-indexed study",
    "summary": "PubMed abstract evidence: The obtained multi-bioactive biotherapy exhibited significantly enhanced benefits in IVDD treatment, in terms of reversing IVDD progression and restoring structural integrity through the mtDNA/SPARC-STING signaling pathways.",
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
