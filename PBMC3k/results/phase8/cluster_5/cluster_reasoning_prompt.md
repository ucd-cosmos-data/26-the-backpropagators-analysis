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
5

Current cell-type annotation:
NK cells

Classification-model prediction:
Not available: Notebook 05 did not export a cluster-level prediction. The selected cell-level model was XGBoost.

Classification confidence, if available:
Not available as a cluster-level probability. Held-out NK cells metrics for XGBoost: precision=0.933, recall=0.933, F1=0.933, support=15. These are evaluation metrics against expression-derived labels, not a cluster-level probability.

==================================================
DATASET OBSERVATIONS
==================================================

Representative marker genes:
GZMB, FGFBP2, GNLY, PRF1, NKG7, CST7, SPON2, GZMA, CCL4, CTSW

Marker-gene statistics:
representative_rank,gene,avg_log2FC,adjusted_p_value,pct_in,pct_out,specificity_delta,marker_score,selection_tier
1,GZMB,7.890887,4.623276e-85,0.973856,0.068008,0.905848,142.95891,primary: pct_in >= 0.20
2,FGFBP2,6.923403,1.184735e-70,0.895425,0.061569,0.833855,115.462342,primary: pct_in >= 0.20
3,GNLY,7.358587,2.051503e-72,0.915033,0.134809,0.780224,114.826898,primary: pct_in >= 0.20
4,PRF1,6.527348,9.805125e-83,0.96732,0.106237,0.861083,112.411747,primary: pct_in >= 0.20
5,NKG7,6.985301,4.393452e-88,1.0,0.255533,0.744467,104.006494,primary: pct_in >= 0.20
6,CST7,5.519955,6.498606e-76,0.96732,0.148893,0.818427,90.353588,primary: pct_in >= 0.20
7,SPON2,6.330124,5.106432e-48,0.738562,0.039437,0.699125,88.511024,primary: pct_in >= 0.20
8,GZMA,5.479171,2.617524e-74,0.954248,0.150905,0.803343,88.033071,primary: pct_in >= 0.20
9,CCL4,5.431434,4.898287e-45,0.745098,0.074849,0.670249,72.808254,primary: pct_in >= 0.20
10,CTSW,4.689354,1.005510e-75,0.986928,0.257143,0.729785,68.444433,primary: pct_in >= 0.20


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
    "gene": "GZMB",
    "official_gene_name": "granzyme B",
    "immune_function": "Cytotoxic-granule serine protease discussed in perforin-dependent target-cell killing and in perforin-independent extracellular activity.",
    "immune_cell_contexts": "NK cells; cytotoxic CD8 T cells; context-dependent expression in additional immune cells",
    "biological_role": "Effector protease released from cytotoxic granules; reported substrates and effects vary by cellular and disease context.",
    "function_tags": "cytotoxic granules; target-cell killing; serine protease",
    "pathway_tags": "perforin–granzyme pathway; programmed cell death",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 2 review(s) provide context but do not determine the grade.",
    "plain_language_note": "GZMB makes granzyme B, one of the protein tools killer immune cells can release when they attack a target cell."
  },
  {
    "gene": "FGFBP2",
    "official_gene_name": "fibroblast growth factor binding protein 2",
    "immune_function": "Frequently used in single-cell studies as an expression marker of mature cytotoxic NK-cell states; a direct immune mechanism is less well established.",
    "immune_cell_contexts": "Cytotoxic NK cells; some cytotoxic T/NKT-cell states",
    "biological_role": "Literature in this collection primarily treats FGFBP2 as a cell-state marker rather than demonstrating a causal NK-cell mechanism.",
    "function_tags": "cytotoxic cell-state marker; NK-cell heterogeneity",
    "pathway_tags": "cytotoxic lymphocyte program",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "FGFBP2 is often used as a label for a strongly cytotoxic group of NK cells, but its exact immune job is still less clear."
  },
  {
    "gene": "GNLY",
    "official_gene_name": "granulysin",
    "immune_function": "Cytotoxic and antimicrobial granule protein reported in human NK cells and cytotoxic T cells.",
    "immune_cell_contexts": "NK cells; cytotoxic CD8 T cells; gamma-delta T cells",
    "biological_role": "Reported to damage microbial or target-cell membranes, with precursor and mature forms stored in distinct effector-vesicle contexts.",
    "function_tags": "cytotoxic granules; antimicrobial defense; target-cell killing",
    "pathway_tags": "cytotoxic lymphocyte degranulation; host defense",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "GNLY makes granulysin, a protein that some killer immune cells use against microbes and other target cells."
  },
  {
    "gene": "PRF1",
    "official_gene_name": "perforin 1",
    "immune_function": "Pore-forming cytotoxic-granule protein required for normal killing by NK cells and cytotoxic T cells.",
    "immune_cell_contexts": "NK cells; cytotoxic CD8 T cells",
    "biological_role": "Enables cytotoxic granule contents to act on target cells; pathogenic variants can impair lymphocyte cytotoxicity.",
    "function_tags": "cytotoxic granules; pore formation; target-cell killing",
    "pathway_tags": "perforin–granzyme pathway; lymphocyte cytotoxicity",
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade.",
    "plain_language_note": "PRF1 makes perforin, which helps killer immune cells deliver their attack proteins into a target cell."
  },
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
    "gene": "SPON2",
    "official_gene_name": "spondin 2",
    "immune_function": "Extracellular-matrix protein, also called mindin, studied in innate pattern recognition, leukocyte adhesion, and phagocytosis.",
    "immune_cell_contexts": "Macrophages and dendritic-cell interactions are best represented in the selected literature; direct NK-cell evidence is limited.",
    "biological_role": "Reported as an extracellular ligand and pattern-recognition molecule in experimental innate-immune models.",
    "function_tags": "pattern recognition; cell adhesion; phagocytosis",
    "pathway_tags": "innate pathogen recognition; integrin signaling",
    "grade_explanation": "Laboratory or animal evidence predominates (3 selected experimental study/studies); repeated human evidence is insufficient.",
    "plain_language_note": "SPON2 makes an outside-the-cell protein that can help innate immune cells recognize and interact with microbes; its NK-cell role is uncertain."
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
    "gene": "CCL4",
    "official_gene_name": "C-C motif chemokine ligand 4",
    "immune_function": "Secreted chemokine associated with immune-cell communication and recruitment through chemokine receptors including CCR5.",
    "immune_cell_contexts": "Activated NK cells; T cells; additional leukocytes depending on context",
    "biological_role": "Acts as a signaling ligand that can help coordinate leukocyte trafficking rather than directly executing target-cell killing.",
    "function_tags": "chemokine signaling; immune-cell recruitment; cell communication",
    "pathway_tags": "CCR5 chemokine axis; leukocyte trafficking",
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade.",
    "plain_language_note": "CCL4 is a chemical message that can help immune cells call or guide other immune cells to an area."
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
  }
]

Cluster-level literature summary:
# Literature Reference Report — Cluster 5: NK cells

> This document organizes evidence for later analysis. It does not interpret the genes as a combined program and does not make a biological or clinical conclusion.

## Selected Genes

GZMB, FGFBP2, GNLY, PRF1, NKG7, CST7, SPON2, GZMA, CCL4, CTSW

## Dataset Boundary

The genes were selected from the Phase 6 marker ranking for cluster 5. Marker statistics are dataset observations. All publication claims come from the verified references table. Disease contexts in those papers do not describe or diagnose the PBMC3k donor.

## Recurring Biological Functions

- cytotoxic granules: tagged for 5 gene(s)
- target-cell killing: tagged for 4 gene(s)
- serine protease: tagged for 2 gene(s)
- cytotoxic cell-state marker: tagged for 1 gene(s)
- NK-cell heterogeneity: tagged for 1 gene(s)
- antimicrobial defense: tagged for 1 gene(s)
- pore formation: tagged for 1 gene(s)
- granule exocytosis: tagged for 1 gene(s)
- protease inhibition: tagged for 1 gene(s)
- cytotoxic-cell regulation: tagged for 1 gene(s)
- pattern recognition: tagged for 1 gene(s)
- cell adhesion: tagged for 1 gene(s)
- phagocytosis: tagged for 1 gene(s)
- target-cell response: tagged for 1 gene(s)
- chemokine signaling: tagged for 1 gene(s)
- immune-cell recruitment: tagged for 1 gene(s)
- cell communication: tagged for 1 gene(s)
- lysosomal protease: tagged for 1 gene(s)
- cytotoxic lymphocyte marker: tagged for 1 gene(s)

## Recurring Immune Pathways

- lymphocyte cytotoxicity: tagged for 3 gene(s)
- perforin–granzyme pathway: tagged for 2 gene(s)
- programmed cell death: tagged for 1 gene(s)
- cytotoxic lymphocyte program: tagged for 1 gene(s)
- cytotoxic lymphocyte degranulation: tagged for 1 gene(s)
- host defense: tagged for 1 gene(s)
- lymphocyte degranulation: tagged for 1 gene(s)
- inflammatory signaling: tagged for 1 gene(s)
- cathepsin regulation: tagged for 1 gene(s)
- immune effector protease processing: tagged for 1 gene(s)
- innate pathogen recognition: tagged for 1 gene(s)
- integrin signaling: tagged for 1 gene(s)
- gasdermin-mediated pyroptosis: tagged for 1 gene(s)
- CCR5 chemokine axis: tagged for 1 gene(s)
- leukocyte trafficking: tagged for 1 gene(s)
- cysteine-protease regulation: tagged for 1 gene(s)

## Recurring Disease Themes in the Selected Publications

- inflammation: tagged for 4 gene(s)
- cancer: tagged for 3 gene(s)
- bacterial infection: tagged for 2 gene(s)
- infection: tagged for 1 gene(s)
- melanoma: tagged for 1 gene(s)
- hepatocellular carcinoma: tagged for 1 gene(s)
- pregnancy infection defense: tagged for 1 gene(s)
- familial hemophagocytic lymphohistiocytosis: tagged for 1 gene(s)
- parasitic infection: tagged for 1 gene(s)
- glioblastoma: tagged for 1 gene(s)
- viral neuroinflammation: tagged for 1 gene(s)
- innate inflammation: tagged for 1 gene(s)
- HIV: tagged for 1 gene(s)
- HBV: tagged for 1 gene(s)
- immune pathology (limited evidence): tagged for 1 gene(s)

These are indexing tags, not evidence of disease in this dataset and not formal enrichment results.

## Confidence of Literature

| Gene | Grade | References | Reason |
| --- | --- | --- | --- |
| GZMB | B | 4 | Multiple human studies: 2 primary human studies; 2 review(s) provide context but do not determine the grade. |
| FGFBP2 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| GNLY | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| PRF1 | A | 3 | Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade. |
| NKG7 | B | 3 | Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade. |
| CST7 | B | 3 | Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade. |
| SPON2 | C | 3 | Laboratory or animal evidence predominates (3 selected experimental study/studies); repeated human evidence is insufficient. |
| GZMA | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| CCL4 | B | 3 | Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade. |
| CTSW | C | 3 | Laboratory or animal evidence predominates (2 selected experimental study/studies); repeated human evidence is insufficient. |

Grades describe the selected evidence set using the explicit A–E rules in Notebook 07. A high grade does not make every reported mechanism universal or causal.

## Unanswered Biological Questions

- Which selected markers are stable across independent healthy PBMC cohorts?
- Which markers change with NK-cell activation, maturation, or recent target-cell contact?
- Does FGFBP2 have a direct immune mechanism, or is it primarily a correlated cytotoxic-state marker?
- What direct role, if any, does SPON2 have in circulating human NK cells?
- Which substrates make CTSW functionally important in human NK cells, and under what conditions?
- How well do tumor, infection, animal, and cell-line findings transfer to healthy peripheral blood?
- Which claims have been independently replicated with both protein-level and functional measurements?

## Future Interpretation

Cross-gene reasoning, pathway synthesis, and biological conclusions are intentionally deferred to Notebook 08.


Evidence grades:
[
  {
    "gene": "GZMB",
    "evidence_grade": "B",
    "publication_count": 4,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 2 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "FGFBP2",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "GNLY",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "PRF1",
    "evidence_grade": "A",
    "publication_count": 3,
    "grade_explanation": "Repeated human evidence: 3 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "NKG7",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "CST7",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 0 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "SPON2",
    "evidence_grade": "C",
    "publication_count": 3,
    "grade_explanation": "Laboratory or animal evidence predominates (3 selected experimental study/studies); repeated human evidence is insufficient."
  },
  {
    "gene": "GZMA",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "CCL4",
    "evidence_grade": "B",
    "publication_count": 3,
    "grade_explanation": "Multiple human studies: 2 primary human studies; 1 review(s) provide context but do not determine the grade."
  },
  {
    "gene": "CTSW",
    "evidence_grade": "C",
    "publication_count": 3,
    "grade_explanation": "Laboratory or animal evidence predominates (2 selected experimental study/studies); repeated human evidence is insufficient."
  }
]

Verified references:
[
  {
    "reference_id": "PMID:15354873",
    "gene": "CCL4",
    "title": "Trafficking of natural killer cells.",
    "journal": "Current molecular medicine",
    "year": 2004,
    "DOI": "10.2174/1566524043360609",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "Review organizes chemokines and receptors involved in NK-cell movement between blood and tissues.",
    "evidence_categories": "Mechanism; Review"
  },
  {
    "reference_id": "PMID:28883824",
    "gene": "CCL4",
    "title": "Natural Killer (NK) Cell Education Differentially Influences HIV Antibody-Dependent NK Cell Activation and Antibody-Dependent Cellular Cytotoxicity.",
    "journal": "Frontiers in immunology",
    "year": 2017,
    "DOI": "10.3389/fimmu.2017.01033",
    "evidence_grade": "B",
    "study_type": "Human study",
    "summary": "Human study reports that NK-cell education influences antibody-dependent activation, cytotoxicity, and chemokine responses during HIV-related experiments.",
    "evidence_categories": "Association; Experimental evidence"
  },
  {
    "reference_id": "PMID:38687604",
    "gene": "CCL4",
    "title": "HIV/HBV coinfection remodels the immune landscape and natural killer cell ADCC functional responses.",
    "journal": "Hepatology (Baltimore, Md.)",
    "year": 2024,
    "DOI": "10.1097/HEP.0000000000000877",
    "evidence_grade": "B",
    "study_type": "Human study",
    "summary": "Human HIV/HBV coinfection study reports altered NK-cell functional responses, including chemokine-associated measurements.",
    "evidence_categories": "Association; Biomarker"
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
    "reference_id": "PMID:31801909",
    "gene": "FGFBP2",
    "title": "Discovery of specialized NK cell populations infiltrating human melanoma metastases.",
    "journal": "JCI insight",
    "year": 2019,
    "DOI": "10.1172/jci.insight.133103",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "Human melanoma single-cell study identifies specialized blood and tumor NK populations using FGFBP2 and CD16-related markers.",
    "evidence_categories": "Association; Biomarker"
  },
  {
    "reference_id": "PMID:38065972",
    "gene": "FGFBP2",
    "title": "Delineating the early dissemination mechanisms of acral melanoma by integrating single-cell and spatial transcriptomic analyses.",
    "journal": "Nature communications",
    "year": 2023,
    "DOI": "10.1038/s41467-023-43980-y",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "Human single-cell and spatial melanoma analysis reports FGFBP2-positive cytotoxic lymphocyte states across clinical tissue groups.",
    "evidence_categories": "Association; Biomarker"
  },
  {
    "reference_id": "PMID:38604154",
    "gene": "FGFBP2",
    "title": "Single-cell data revealed exhaustion of characteristic NK cell subpopulations and T cell subpopulations in hepatocellular carcinoma.",
    "journal": "Aging",
    "year": 2024,
    "DOI": "10.18632/aging.205723",
    "evidence_grade": "A",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "Single-cell analysis of human hepatocellular carcinoma labels an FGFBP2-positive NK subset and reports disease-associated state differences.",
    "evidence_categories": "Association; Computational evidence"
  },
  {
    "reference_id": "PMID:14499265",
    "gene": "GNLY",
    "title": "Granulysin.",
    "journal": "Current opinion in immunology",
    "year": 2003,
    "DOI": "10.1016/s0952-7915(03)00097-9",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "Review summarizes granulysin structure, processing, antimicrobial activity, and cytotoxic activity.",
    "evidence_categories": "Mechanism; Review"
  },
  {
    "reference_id": "PMID:30658247",
    "gene": "GNLY",
    "title": "Granulysin species segregate to different lysosome-related effector vesicles (LREV) and get mobilized by either classical or non-classical degranulation.",
    "journal": "Molecular immunology",
    "year": 2019,
    "DOI": "10.1016/j.molimm.2018.12.031",
    "evidence_grade": "B",
    "study_type": "Human laboratory study",
    "summary": "Human lymphocyte experiments report that granulysin forms occupy different effector vesicles and can follow different release routes.",
    "evidence_categories": "Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:32822574",
    "gene": "GNLY",
    "title": "Decidual NK Cells Transfer Granulysin to Selectively Kill Bacteria in Trophoblasts.",
    "journal": "Cell",
    "year": 2020,
    "DOI": "10.1016/j.cell.2020.07.019",
    "evidence_grade": "B",
    "study_type": "Human ex vivo/laboratory study",
    "summary": "Human decidual and peripheral NK-cell experiments report granulysin transfer that kills intracellular bacteria while sparing host cells.",
    "evidence_categories": "Mechanism; Experimental evidence"
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
    "reference_id": "PMID:32114394",
    "gene": "GZMB",
    "title": "Single-cell transcriptomics of blood reveals a natural killer cell subset depletion in tuberculosis.",
    "journal": "EBioMedicine",
    "year": 2020,
    "DOI": "10.1016/j.ebiom.2020.102686",
    "evidence_grade": "B",
    "study_type": "Human single-cell/transcriptomic study",
    "summary": "Human blood single-cell study reports depletion of a cytotoxic NK-cell subset in tuberculosis and uses cytotoxic-effector genes to define it.",
    "evidence_categories": "Association; Biomarker"
  },
  {
    "reference_id": "PMID:38729924",
    "gene": "GZMB",
    "title": "Pretreatment with IL-15 and IL-18 rescues natural killer cells from granzyme B-mediated apoptosis after cryopreservation.",
    "journal": "Nature communications",
    "year": 2024,
    "DOI": "10.1038/s41467-024-47574-0",
    "evidence_grade": "B",
    "study_type": "Human ex vivo/laboratory study",
    "summary": "Human NK-cell cryopreservation experiments report granzyme B-associated apoptosis and test cytokine pretreatment as a protective intervention.",
    "evidence_categories": "Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:38846935",
    "gene": "GZMB",
    "title": "Reassessing granzyme B: unveiling perforin-independent versatility in immune responses and therapeutic potentials.",
    "journal": "Frontiers in immunology",
    "year": 2024,
    "DOI": "10.3389/fimmu.2024.1392535",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "Review describes perforin-dependent and perforin-independent granzyme B activity across immune and pathological contexts.",
    "evidence_categories": "Mechanism; Association"
  },
  {
    "reference_id": "PMID:39179536",
    "gene": "GZMB",
    "title": "Natural Killer cells at the frontline in the fight against cancer.",
    "journal": "Cell death & disease",
    "year": 2024,
    "DOI": "10.1038/s41419-024-06976-0",
    "evidence_grade": "B",
    "study_type": "Review",
    "summary": "Review organizes granzyme B with perforin and granulysin in the cytotoxic arsenal used by NK cells.",
    "evidence_categories": "Mechanism; Review"
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
  },
  {
    "reference_id": "PMID:12060139",
    "gene": "PRF1",
    "title": "Functional consequences of perforin gene mutations in 22 patients with familial haemophagocytic lymphohistiocytosis.",
    "journal": "British journal of haematology",
    "year": 2002,
    "DOI": "10.1046/j.1365-2141.2002.03534.x",
    "evidence_grade": "A",
    "study_type": "Human family study",
    "summary": "Study of affected families links PRF1 variants to absent perforin expression and impaired cytotoxic function in familial HLH.",
    "evidence_categories": "Association; Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:14757862",
    "gene": "PRF1",
    "title": "Characterisation of diverse PRF1 mutations leading to decreased natural killer cell activity in North American families with haemophagocytic lymphohistiocytosis.",
    "journal": "Journal of medical genetics",
    "year": 2004,
    "DOI": "10.1136/jmg.2003.011528",
    "evidence_grade": "A",
    "study_type": "Human multicenter family study",
    "summary": "Multicenter family study characterizes diverse PRF1 mutations associated with reduced NK-cell activity in familial HLH.",
    "evidence_categories": "Association; Experimental evidence"
  },
  {
    "reference_id": "PMID:32542393",
    "gene": "PRF1",
    "title": "Frequency and spectrum of disease-causing variants in 1892 patients with suspected genetic HLH disorders.",
    "journal": "Blood advances",
    "year": 2020,
    "DOI": "10.1182/bloodadvances.2020001605",
    "evidence_grade": "A",
    "study_type": "Human clinical cohort",
    "summary": "Large clinical referral cohort reports PRF1 among the most frequent genes with pathogenic findings in suspected genetic HLH.",
    "evidence_categories": "Association; Biomarker"
  },
  {
    "reference_id": "PMID:14691481",
    "gene": "SPON2",
    "title": "The extracellular matrix protein mindin is a pattern-recognition molecule for microbial pathogens.",
    "journal": "Nature immunology",
    "year": 2004,
    "DOI": "10.1038/ni1021",
    "evidence_grade": "C",
    "study_type": "Laboratory/animal study",
    "summary": "Mouse experiments report mindin as an extracellular pattern-recognition molecule needed for normal responses to microbial challenge.",
    "evidence_categories": "Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:19153605",
    "gene": "SPON2",
    "title": "Structure of the F-spondin domain of mindin, an integrin ligand and pattern recognition molecule.",
    "journal": "The EMBO journal",
    "year": 2009,
    "DOI": "10.1038/emboj.2008.288",
    "evidence_grade": "C",
    "study_type": "Structural laboratory study",
    "summary": "Structural study examines the mindin domain involved in integrin binding and pattern recognition.",
    "evidence_categories": "Mechanism; Experimental evidence"
  },
  {
    "reference_id": "PMID:30869196",
    "gene": "SPON2",
    "title": "The pattern-recognition molecule mindin binds integrin Mac-1 to promote macrophage phagocytosis via Syk activation and NF-κB p65 translocation.",
    "journal": "Journal of cellular and molecular medicine",
    "year": 2019,
    "DOI": "10.1111/jcmm.14236",
    "evidence_grade": "C",
    "study_type": "Laboratory/animal study",
    "summary": "Experimental macrophage study reports mindin binding to Mac-1 and promotion of phagocytosis-related signaling.",
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
