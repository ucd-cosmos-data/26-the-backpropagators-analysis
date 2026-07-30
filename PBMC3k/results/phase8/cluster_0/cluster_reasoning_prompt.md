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
0

Current cell-type annotation:
Cytotoxic CD8 T cells

Classification-model prediction:
Not available: Notebook 05 did not export a cluster-level prediction. The selected cell-level model was XGBoost.

Classification confidence, if available:
Not available as a cluster-level probability. Held-out Cytotoxic CD8 T cells metrics for XGBoost: precision=0.852, recall=0.821, F1=0.836, support=28. These are evaluation metrics against expression-derived labels, not a cluster-level probability.

==================================================
DATASET OBSERVATIONS
==================================================

Representative marker genes:
NKG7, CCL5, GZMA, CST7, GZMK, CTSW, CD8A, LYAR, GZMH, KLRG1

Marker-gene statistics:
representative_rank,gene,avg_log2FC,adjusted_p_value,pct_in,pct_out,specificity_delta,marker_score,selection_tier
1,NKG7,5.149965,2.524331e-104,0.959707,0.22241,0.737297,75.941055,primary: pct_in >= 0.20
2,CCL5,5.365429,2.447579e-111,0.945055,0.243975,0.70108,75.231933,primary: pct_in >= 0.20
3,GZMA,4.028471,5.997373e-68,0.787546,0.129387,0.658159,53.02748,primary: pct_in >= 0.20
4,CST7,4.054892,1.801775e-67,0.776557,0.129387,0.64717,52.484075,primary: pct_in >= 0.20
5,GZMK,4.834554,1.209201e-45,0.586081,0.058351,0.52773,51.026748,primary: pct_in >= 0.20
6,CTSW,3.365193,5.045760e-66,0.820513,0.239323,0.581189,39.116288,primary: pct_in >= 0.20
7,CD8A,3.730852,6.730724e-31,0.509158,0.072727,0.43643,32.565132,primary: pct_in >= 0.20
8,LYAR,3.081434,1.366361e-35,0.589744,0.135307,0.454437,28.006359,primary: pct_in >= 0.20
9,GZMH,3.894171,2.653517e-20,0.417582,0.063425,0.354157,26.998483,primary: pct_in >= 0.20
10,KLRG1,3.330793,1.103393e-22,0.450549,0.07611,0.37444,24.943613,primary: pct_in >= 0.20


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
    "gene": "NKG7",
    "official_gene_name": "natural killer cell granule protein 7",
    "immune_function": "Granule-associated protein studied as a regulator of cytotoxic granule release in NK and T cells.",
    "immune_cell_contexts": "NK cells; cytotoxic CD8 T cells; selected activated CD4 T-cell states",
    "biological_role": "Experimental studies report effects on granule exocytosis, target-cell killing, and downstream inflammation.",
    "function_tags": "cytotoxic granules; granule exocytosis; target-cell killing",
    "pathway_tags": "lymphocyte degranulation; inflammatory signaling",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "NKG7 helps organize how killer immune cells release packages containing cell-killing proteins."
  },
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
    "gene": "GZMA",
    "official_gene_name": "granzyme A",
    "immune_function": "Cytotoxic-lymphocyte serine protease with reported inflammatory and target-cell death activities that differ from granzyme B.",
    "immune_cell_contexts": "NK cells; cytotoxic CD8 T cells",
    "biological_role": "Granule-released protease; selected studies report context-dependent substrate cleavage and inflammatory or cell-death outcomes.",
    "function_tags": "cytotoxic granules; serine protease; target-cell response",
    "pathway_tags": "gasdermin-mediated pyroptosis; lymphocyte cytotoxicity",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "GZMA makes granzyme A, another enzyme carried by killer immune cells; it does not always act in the same way as granzyme B."
  },
  {
    "gene": "CST7",
    "official_gene_name": "cystatin F",
    "immune_function": "Immune-enriched cysteine-protease inhibitor that can regulate cathepsins involved in cytotoxic-cell effector pathways.",
    "immune_cell_contexts": "NK cells; cytotoxic T cells; myeloid cells and microglia in context-dependent states",
    "biological_role": "Reported to inhibit cathepsin C and other proteases; direction and consequence depend on cell type, processing, and tissue context.",
    "function_tags": "protease inhibition; cytotoxic-cell regulation",
    "pathway_tags": "cathepsin regulation; immune effector protease processing",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "CST7 makes cystatin F, a protein that can act like a brake on enzymes used by several immune cells."
  },
  {
    "gene": "GZMK",
    "official_gene_name": "GZMK",
    "immune_function": "The selected PubMed collection discusses GZMK in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for GZMK, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "CTSW",
    "official_gene_name": "cathepsin W",
    "immune_function": "Lysosomal cysteine protease enriched in NK cells and cytotoxic T cells; its indispensable substrates and mechanism remain uncertain.",
    "immune_cell_contexts": "NK cells; cytotoxic CD8 T cells",
    "biological_role": "Human cell studies report cytotoxic-lymphocyte expression and secretion during target contact, while knockout evidence questions whether it is essential for killing.",
    "function_tags": "lysosomal protease; cytotoxic lymphocyte marker",
    "pathway_tags": "cysteine-protease regulation; lymphocyte cytotoxicity",
    "grade_explanation": "Laboratory or animal evidence predominates (2 selected experimental study/studies); repeated human evidence is insufficient.",
    "plain_language_note": "CTSW makes cathepsin W, an enzyme common in killer immune cells, but scientists have not fully settled exactly what it must do."
  },
  {
    "gene": "CD8A",
    "official_gene_name": "CD8A",
    "immune_function": "The selected PubMed collection discusses CD8A in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for CD8A, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "LYAR",
    "official_gene_name": "LYAR",
    "immune_function": "The selected PubMed collection discusses LYAR in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for LYAR, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "GZMH",
    "official_gene_name": "GZMH",
    "immune_function": "The selected PubMed collection discusses GZMH in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for GZMH, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  },
  {
    "gene": "KLRG1",
    "official_gene_name": "KLRG1",
    "immune_function": "The selected PubMed collection discusses KLRG1 in publication-specific biological or immune contexts; claims are limited to the verified article summaries below.",
    "immune_cell_contexts": "Cell contexts vary across the selected publications; no cell type is treated as unique.",
    "biological_role": "No single cross-publication mechanism is asserted; publication-specific evidence is listed below.",
    "function_tags": "gene-specific literature evidence",
    "pathway_tags": "publication-specific; no combined pathway inference",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "Selected PubMed records provide context for KLRG1, but they do not by themselves establish what the gene does in this PBMC3k cluster."
  }
]

Cluster-level literature summary:
# Literature Reference Report — Cluster 0: Cytotoxic CD8 T cells

> This document organizes evidence for later analysis. It does not interpret the genes as a combined program and does not make a biological or clinical conclusion.

## Selected Genes

NKG7, CCL5, GZMA, CST7, GZMK, CTSW, CD8A, LYAR, GZMH, KLRG1

## Dataset Boundary

The genes were selected from the Phase 6 marker ranking for cluster 0. Marker statistics are dataset observations. All publication claims come from the verified references table. Publication contexts do not describe or diagnose the PBMC3k source.

## Recurring Biological Functions

- gene-specific literature evidence: tagged for 6 gene(s)
- cytotoxic granules: tagged for 2 gene(s)
- granule exocytosis: tagged for 1 gene(s)
- target-cell killing: tagged for 1 gene(s)
- serine protease: tagged for 1 gene(s)
- target-cell response: tagged for 1 gene(s)
- protease inhibition: tagged for 1 gene(s)
- cytotoxic-cell regulation: tagged for 1 gene(s)
- lysosomal protease: tagged for 1 gene(s)
- cytotoxic lymphocyte marker: tagged for 1 gene(s)

## Recurring Immune Pathways

- publication-specific; no combined pathway inference: tagged for 6 gene(s)
- lymphocyte cytotoxicity: tagged for 2 gene(s)
- lymphocyte degranulation: tagged for 1 gene(s)
- inflammatory signaling: tagged for 1 gene(s)
- gasdermin-mediated pyroptosis: tagged for 1 gene(s)
- cathepsin regulation: tagged for 1 gene(s)
- immune effector protease processing: tagged for 1 gene(s)
- cysteine-protease regulation: tagged for 1 gene(s)

## Recurring Disease Themes in the Selected Publications

- publication contexts only: tagged for 6 gene(s)
- cancer: tagged for 2 gene(s)
- inflammation: tagged for 2 gene(s)
- parasitic infection: tagged for 1 gene(s)
- glioblastoma: tagged for 1 gene(s)
- viral neuroinflammation: tagged for 1 gene(s)
- immune pathology (limited evidence): tagged for 1 gene(s)

These are indexing tags, not evidence of disease in this dataset and not formal enrichment results.

## Confidence of Literature

| Gene | Grade | References | Reason |
| --- | --- | --- | --- |
| NKG7 | B | 3 | Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade. |
| CCL5 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| GZMA | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| CST7 | B | 3 | Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade. |
| GZMK | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| CTSW | C | 3 | Laboratory or animal evidence predominates (2 selected experimental study/studies); repeated human evidence is insufficient. |
| CD8A | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| LYAR | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| GZMH | B | 3 | Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade. |
| KLRG1 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |

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
    "gene": "NKG7",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "CCL5",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "GZMA",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "CST7",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "GZMK",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "CTSW",
    "evidence_grade": "C",
    "publication_count": 3,
    "grade_explanation": "Laboratory or animal evidence predominates (2 selected experimental study/studies); repeated human evidence is insufficient."
  },
  {
    "gene": "CD8A",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "LYAR",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "GZMH",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "KLRG1",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
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
    "reference_id": "PMID:38348045",
    "gene": "CD8A",
    "title": "Lung single-cell RNA profiling reveals response of pulmonary capillary to sepsis-induced acute lung injury.",
    "journal": "Frontiers in immunology",
    "year": 2024,
    "DOI": "10.3389/fimmu.2024.1308915",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Cd74+ Capillary cells expressing high levels of major histocompatibility complex (MHC) and mainly interacted with Cd8a+ T cells in the sham group.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:39694280",
    "gene": "CD8A",
    "title": "Single-cell RNA sequencing of chronic idiopathic erythroderma defines disease-specific markers.",
    "journal": "The Journal of allergy and clinical immunology",
    "year": 2025,
    "DOI": "10.1016/j.jaci.2024.11.037",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: In contrast, CIE exhibited a pattern of low-level, but consistent, expansion of CD8A+KLRK1+ T-cell clones, both in blood and in skin.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40769312",
    "gene": "CD8A",
    "title": "BCAP31 promotes colorectal cancer metastasis via oxidative phosphorylation-dependent macrophage immunosuppression: A single-cell transcriptomic study.",
    "journal": "Free radical biology & medicine",
    "year": 2025,
    "DOI": "10.1016/j.freeradbiomed.2025.08.002",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Through single-cell RNA sequencing (scRNA-seq) analysis of CRC tissues, we identified macrophages as a dominant immune subset (16 % of TME) that interacts with NK cells and fibroblasts via HLA-CD8A and COL1A1/2-CD44 signaling, promoting immunosuppression.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:18256700",
    "gene": "CST7",
    "title": "Cystatin F is a cathepsin C-directed protease inhibitor regulated by proteolysis.",
    "journal": "The EMBO journal",
    "year": 2008,
    "DOI": "10.1038/sj.emboj.7601979",
    "evidence_grade": "B",
    "study_type": "Human laboratory study",
    "summary": "Biochemical and human immune-cell experiments identify cystatin F as a cathepsin C-directed inhibitor enriched in cytotoxic lymphocytes.",
    "evidence_categories": "Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:34189679",
    "gene": "CST7",
    "title": "Cystatin F acts as a mediator of immune suppression in glioblastoma.",
    "journal": "Cellular oncology (Dordrecht, Netherlands)",
    "year": 2021,
    "DOI": "10.1007/s13402-021-00618-9",
    "evidence_grade": "B",
    "study_type": "Human and laboratory study",
    "summary": "Glioblastoma study reports cystatin F expression and transfer in tumor and immune cells alongside reduced NK-cell cytotoxic susceptibility.",
    "evidence_categories": "Association; Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:38879499",
    "gene": "CST7",
    "title": "Cystatin F attenuates neuroinflammation and demyelination following murine coronavirus infection of the central nervous system.",
    "journal": "Journal of neuroinflammation",
    "year": 2024,
    "DOI": "10.1186/s12974-024-03153-0",
    "evidence_grade": "B",
    "study_type": "Laboratory/animal study",
    "summary": "Mouse coronavirus study reports altered neuroinflammation and immune-cell transcription after Cst7 deletion.",
    "evidence_categories": "Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:15087452",
    "gene": "CTSW",
    "title": "Characterization of murine cathepsin W and its role in cell-mediated cytotoxicity.",
    "journal": "The Journal of biological chemistry",
    "year": 2004,
    "DOI": "10.1074/jbc.M400304200",
    "evidence_grade": "C",
    "study_type": "Laboratory/animal study",
    "summary": "Mouse knockout study characterizes cathepsin W expression and tests its contribution to cell-mediated cytotoxicity.",
    "evidence_categories": "Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:19100676",
    "gene": "CTSW",
    "title": "Cathepsin W expressed exclusively in CD8+ T cells and NK cells, is secreted during target cell killing but is not essential for cytotoxicity in human CTLs.",
    "journal": "Experimental hematology",
    "year": 2009,
    "DOI": "10.1016/j.exphem.2008.10.011",
    "evidence_grade": "C",
    "study_type": "Human laboratory study",
    "summary": "Human cytotoxic-lymphocyte study reports cathepsin W secretion during target-cell contact but finds it nonessential in tested CTL killing assays.",
    "evidence_categories": "Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:38891048",
    "gene": "CTSW",
    "title": "Unveiling the Roles of Cysteine Proteinases F and W: From Structure to Pathological Implications and Therapeutic Targets.",
    "journal": "Cells",
    "year": 2024,
    "DOI": "10.3390/cells13110917",
    "evidence_grade": "C",
    "study_type": "Review",
    "summary": "Review summarizes cysteine proteases F and W, including immune expression, proposed roles, pathology, and unresolved therapeutic questions.",
    "evidence_categories": "Association; Review"
  },
  {
    "reference_id": "PMID:32093590",
    "gene": "GZMA",
    "title": "Granzymes and Mitochondria.",
    "journal": "Biochemistry. Biokhimiia",
    "year": 2020,
    "DOI": "10.1134/S0006297920020017",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "Review compares granzyme effects involving mitochondria and emphasizes distinct mechanisms among granzyme family members.",
    "evidence_categories": "Mechanism; Review"
  },
  {
    "reference_id": "PMID:32299851",
    "gene": "GZMA",
    "title": "Granzyme A from cytotoxic lymphocytes cleaves GSDMB to trigger pyroptosis in target cells.",
    "journal": "Science (New York, N.Y.)",
    "year": 2020,
    "DOI": "10.1126/science.aaz7548",
    "evidence_grade": "B",
    "study_type": "Human and laboratory/animal study",
    "summary": "Human-cell and mouse experiments report granzyme A cleavage of GSDMB and target-cell pyroptosis under specified conditions.",
    "evidence_categories": "Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:36792800",
    "gene": "GZMA",
    "title": "Butyrate limits human natural killer cell effector function.",
    "journal": "Scientific reports",
    "year": 2023,
    "DOI": "10.1038/s41598-023-29731-5",
    "evidence_grade": "B",
    "study_type": "Human ex vivo study",
    "summary": "Ex vivo human blood NK-cell study reports reduced granzyme A and other effector outputs after butyrate exposure.",
    "evidence_categories": "Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:40970118",
    "gene": "GZMH",
    "title": "Intrathecally expanded GZMK+/GZMH+ CD8 T cells targeting EBV antigens may reduce severity of Multiple Sclerosis.",
    "journal": "medRxiv : the preprint server for health sciences",
    "year": 2025,
    "DOI": "10.1101/2025.08.05.25333071",
    "evidence_grade": "B",
    "study_type": "Laboratory or other primary study",
    "summary": "PubMed abstract evidence: Combining cerebrospinal fluid B cell receptor and T cell receptor repertoire analysis with transcriptional/ flow cytometry cellular profiles in hundreds of deeply-phenotyped people with Multiple Sclerosis (pwMS) and controls, we identified intrathecal expansion of anti-viral, cytotoxic, granzymes H/K (GZMH+/GZMK+) double positive (DP) CD8+ T cells that recognize EBV epitopes in pwMS.",
    "evidence_categories": "Association; Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:40974256",
    "gene": "GZMH",
    "title": "Single-cell profiling of peripheral and local immune compartments reveal unique genotype-independent prognostic immune signatures across isocitrate dehydrogenase-stratified glioma.",
    "journal": "Neuro-oncology",
    "year": 2026,
    "DOI": "10.1093/neuonc/noaf206",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: RESULTS: Our analyses revealed unique intratumoral and peripheral immune cellular ontogenies, including naïve CD4+ T cell enrichment in the IDH-Mut peripheral immune compartment, monocyte enrichment in IDH-WT glioma PBMCs, and emergence of a unique population of GZMH+ CD8+ T cells preferentially in the IDH-Mut microenvironment.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41740930",
    "gene": "GZMH",
    "title": "Comprehensive single-cell transcriptomic profiling of the scalp from patients with moderate-to-severe alopecia areata.",
    "journal": "The Journal of allergy and clinical immunology",
    "year": 2026,
    "DOI": "10.1016/j.jaci.2026.02.014",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: LS AA samples demonstrated robust TH1 activation and cytotoxicity, with upregulated IFNG, GZMH/K, and XCL1/2.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:33271118",
    "gene": "GZMK",
    "title": "Comprehensive Profiling of an Aging Immune System Reveals Clonal GZMK+ CD8+ T Cells as Conserved Hallmark of Inflammaging.",
    "journal": "Immunity",
    "year": 2021,
    "DOI": "10.1016/j.immuni.2020.11.005",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: We defined organ-specific and common immune alterations and identified a subpopulation of age-associated granzyme K (GZMK)-expressing CD8+ T (Taa) cells that are distinct from T effector memory (Tem) cells.",
    "evidence_categories": "Association; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:39814882",
    "gene": "GZMK",
    "title": "GZMK-expressing CD8+ T cells promote recurrent airway inflammatory diseases.",
    "journal": "Nature",
    "year": 2025,
    "DOI": "10.1038/s41586-024-08395-9",
    "evidence_grade": "B",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: By comparing T cell repertoires in nasal polyp tissues obtained from consecutive surgeries, here we report that persistent CD8+ T cell clones carrying effector memory-like features colonize the mucosal tissue during disease recurrence, and these cells characteristically express the tryptase Granzyme K (GZMK).",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:40651883",
    "gene": "GZMK",
    "title": "GZMK+CD8+ T cells: multifaceted roles beyond cytotoxicity.",
    "journal": "Trends in immunology",
    "year": 2025,
    "DOI": "10.1016/j.it.2025.06.003",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Among these, granzyme-K-expressing (GZMK+) CD8+ T cells represent a distinct subset characterized by low cytotoxicity but heightened proinflammatory activity, by contrast with their granzyme-B-expressing (GZMB+) counterparts with high cytotoxicity.",
    "evidence_categories": "Review; Mechanism; Biomarker"
  },
  {
    "reference_id": "PMID:38252421",
    "gene": "KLRG1",
    "title": "KLRG1 Cell Depletion as a Novel Therapeutic Strategy in Patients with Mature T-Cell Lymphoma Subtypes.",
    "journal": "Clinical cancer research : an official journal of the American Association for Cancer Research",
    "year": 2024,
    "DOI": "10.1158/1078-0432.CCR-23-3504",
    "evidence_grade": "B",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: EXPERIMENTAL DESIGN: Primary specimens, cell lines, patient-derived xenograft models, commercially available, and proprietary anti-KLRG1 antibodies were used for screening, target, and functional validation.",
    "evidence_categories": "Association; Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:39658611",
    "gene": "KLRG1",
    "title": "T cell dynamics with neoadjuvant immunotherapy in head and neck cancer.",
    "journal": "Nature reviews. Clinical oncology",
    "year": 2025,
    "DOI": "10.1038/s41571-024-00969-w",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "PubMed abstract evidence: Analyses of systemic responses have defined a PD-1+KLRG1- circulating CD8+ T cell subpopulation that is highly predictive of response, and revealed the interrelationships between intratumoural clones and circulating CD8+ T cells.",
    "evidence_categories": "Review; Mechanism"
  },
  {
    "reference_id": "PMID:40307497",
    "gene": "KLRG1",
    "title": "KLRG1 identifies regulatory T cells with mitochondrial alterations that accumulate with aging.",
    "journal": "Nature aging",
    "year": 2025,
    "DOI": "10.1038/s43587-025-00855-9",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Our analysis identifies a subpopulation of regulatory T (Treg) cells that is characterized by the extracellular expression of the co-inhibitory molecule killer cell lectin-like receptor subfamily G member 1 (KLRG1) and accumulates with aging in humans and mice.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:8491376",
    "gene": "LYAR",
    "title": "LYAR, a novel nucleolar protein with zinc finger DNA-binding motifs, is involved in cell growth regulation.",
    "journal": "Genes & development",
    "year": 1993,
    "DOI": "10.1101/gad.7.5.735",
    "evidence_grade": "A",
    "study_type": "Human and laboratory/animal study",
    "summary": "PubMed abstract evidence: The cDNA is therefore named Ly-1 antibody reactive clone (LYAR).",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:39159060",
    "gene": "LYAR",
    "title": "A Comprehensive Analysis of LYAR in Colorectal Cancer: Prognostic Marker and Therapeutic Target.",
    "journal": "Cancer biotherapy & radiopharmaceuticals",
    "year": 2024,
    "DOI": "10.1089/cbr.2023.0181",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: This work investigated the biological mechanisms and clinical value of Ly1 antibody reactive (LYAR) in CRC.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:41352636",
    "gene": "LYAR",
    "title": "Spatiotemporal profiling of endocytic regulators in the immunosuppressive TAM microenvironment of glioma.",
    "journal": "Brain research",
    "year": 2026,
    "DOI": "10.1016/j.brainres.2025.150086",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "PubMed abstract evidence: Among them, FCGR2B, CLEC7A, and LYAR emerged as key modulators associated with the spatiotemporal heterogeneity of tumor-associated macrophages (TAMs) and malignant cells.",
    "evidence_categories": "Association; Mechanism; Biomarker; Experimental evidence"
  },
  {
    "reference_id": "PMID:32839608",
    "gene": "NKG7",
    "title": "The NK cell granule protein NKG7 regulates cytotoxic granule exocytosis and inflammation.",
    "journal": "Nature immunology",
    "year": 2020,
    "DOI": "10.1038/s41590-020-0758-6",
    "evidence_grade": "B",
    "study_type": "Human and laboratory/animal study",
    "summary": "Human and experimental models report that NKG7 regulates cytotoxic-granule exocytosis, target killing, and inflammatory responses.",
    "evidence_categories": "Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:34911739",
    "gene": "NKG7",
    "title": "NKG7 Is a T-cell-Intrinsic Therapeutic Target for Improving Antitumor Cytotoxicity and Cancer Immunotherapy.",
    "journal": "Cancer immunology research",
    "year": 2022,
    "DOI": "10.1158/2326-6066.CIR-21-0539",
    "evidence_grade": "B",
    "study_type": "Human and laboratory study",
    "summary": "Human-tumor analyses and laboratory experiments examine NKG7 as a target for improving T-cell cytotoxic function.",
    "evidence_categories": "Association; Experimental evidence"
  },
  {
    "reference_id": "PMID:35013002",
    "gene": "NKG7",
    "title": "NKG7 Is Required for Optimal Antitumor T-cell Immunity.",
    "journal": "Cancer immunology research",
    "year": 2022,
    "DOI": "10.1158/2326-6066.CIR-20-0649",
    "evidence_grade": "B",
    "study_type": "Laboratory/animal study",
    "summary": "Experimental cancer models report that NKG7 is required for optimal antitumor T-cell activity.",
    "evidence_categories": "Mechanism; Experimental evidence"
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
