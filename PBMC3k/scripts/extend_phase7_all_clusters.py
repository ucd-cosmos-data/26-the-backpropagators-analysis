"""Extend the validated Phase 7 evidence workflow from Cluster 5 to all clusters.

Cluster 5 literature rows, reference rows, and gene files are preserved. New
gene evidence is selected through PubMed ESearch, verified through EFetch, and
kept deliberately conservative. A gene with no defensible PubMed match receives
an explicit grade-E insufficient-evidence record rather than a fabricated cite.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import re
import time
import xml.etree.ElementTree as ET

import pandas as pd
import requests


PROJECT = Path(__file__).resolve().parents[1]
PHASE6 = PROJECT / "results" / "phase6"
PHASE7 = PROJECT / "results" / "phase7"
GENE_DIR = PHASE7 / "genes"
CACHE_PATH = PHASE7 / "pubmed_search_cache.json"
LITERATURE_PATH = PHASE7 / "literature_summary.csv"
REFERENCES_PATH = PHASE7 / "references.csv"
CLUSTER_REPORT_PATH = PHASE7 / "cluster_reference_report.md"
COVERAGE_PATH = PHASE7 / "phase7_coverage_summary.csv"
REUSE_PATH = PHASE7 / "evidence_reuse_report.csv"
VALIDATION_PATH = PHASE7 / "phase7_validation_report.json"

ALLOWED_GRADES = {"A", "B", "C", "D", "E"}
REFERENCE_COLUMNS = [
    "gene",
    "title",
    "journal",
    "year",
    "PMID",
    "DOI",
    "evidence_grade",
    "study_type",
    "summary",
    "evidence_categories",
    "publication_types",
    "mesh_terms",
]
SUMMARY_COLUMNS = [
    "gene",
    "cluster",
    "cell_type",
    "representative_rank",
    "marker_score",
    "avg_log2FC",
    "pct_in",
    "pct_out",
    "official_gene_name",
    "immune_function",
    "immune_cell_contexts",
    "biological_role",
    "function_tags",
    "pathway_tags",
    "disease_context_tags",
    "publication_count",
    "evidence_grade",
    "grade_explanation",
    "plain_language_note",
    "interpretation_status",
]
REPORT_SEPARATOR = "\n\n---\n\n# Additional Cluster Literature Reference Reports\n"
MANUAL_RELEVANCE_EXCLUSIONS = {
    # Acronym collisions identified during publication-level relevance review.
    "CFD": {
        "29570754",
        "33762468",
        "35718672",
    },  # computational fluid dynamics, not complement factor D
    "LTB": {
        "22069646",
        "20298355",
    },  # bacterial toxin or leukotriene B4, not the human LTB marker gene
    "SDPR": {"42157490"},  # SDPR_admix method, not the SDPR marker gene
}


def natural_cluster_key(value: str) -> tuple[int, str]:
    text = str(value)
    return (int(text), text) if text.isdigit() else (10**9, text)


def request_with_retries(url: str, params: dict[str, str], attempts: int = 5) -> requests.Response:
    headers = {"User-Agent": "PBMC3k educational literature integration notebook"}
    for attempt in range(attempts):
        response = requests.get(url, params=params, headers=headers, timeout=90)
        if response.status_code == 200:
            time.sleep(0.35)
            return response
        if response.status_code in {429, 500, 502, 503, 504} and attempt < attempts - 1:
            time.sleep(2 ** (attempt + 1))
            continue
        response.raise_for_status()
    raise RuntimeError("Unreachable retry state.")


def node_text(node: ET.Element | None) -> str:
    return "" if node is None else "".join(node.itertext()).strip()


def parse_year(article: ET.Element) -> int | pd._libs.missing.NAType:
    for path in [
        ".//JournalIssue/PubDate/Year",
        ".//ArticleDate/Year",
        ".//PubDate/MedlineDate",
    ]:
        text = node_text(article.find(path))
        match = re.search(r"(?:19|20)\d{2}", text)
        if match:
            return int(match.group())
    return pd.NA


def fetch_pubmed_records(pmids: list[str]) -> pd.DataFrame:
    if not pmids:
        return pd.DataFrame(
            columns=[
                "PMID",
                "title",
                "journal",
                "year",
                "DOI",
                "abstract",
                "publication_types",
                "mesh_terms",
            ]
        )
    endpoint = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    batches = []
    for start in range(0, len(pmids), 150):
        batch = pmids[start : start + 150]
        response = request_with_retries(
            endpoint,
            {
                "db": "pubmed",
                "id": ",".join(batch),
                "retmode": "xml",
                "tool": "pbmc3k_phase7_all_clusters",
            },
        )
        root = ET.fromstring(response.content)
        for citation in root.findall(".//PubmedArticle"):
            medline = citation.find("MedlineCitation")
            article = medline.find("Article") if medline is not None else None
            if medline is None or article is None:
                continue
            doi = ""
            for article_id in citation.findall(".//PubmedData/ArticleIdList/ArticleId"):
                if article_id.attrib.get("IdType") == "doi":
                    doi = node_text(article_id)
                    break
            abstract_parts = []
            for part in article.findall(".//Abstract/AbstractText"):
                label = part.attrib.get("Label", "")
                text = node_text(part)
                abstract_parts.append(f"{label}: {text}" if label else text)
            batches.append(
                {
                    "PMID": node_text(medline.find("PMID")),
                    "title": node_text(article.find("ArticleTitle")),
                    "journal": node_text(article.find("Journal/Title")),
                    "year": parse_year(article),
                    "DOI": doi,
                    "abstract": " ".join(abstract_parts),
                    "publication_types": "; ".join(
                        node_text(x)
                        for x in article.findall(".//PublicationTypeList/PublicationType")
                    ),
                    "mesh_terms": "; ".join(
                        node_text(x)
                        for x in medline.findall(".//MeshHeading/DescriptorName")
                    ),
                }
            )
    return pd.DataFrame(batches).drop_duplicates("PMID")


def context_terms(cell_types: set[str]) -> list[str]:
    text = " ".join(sorted(cell_types)).lower()
    if "platelet" in text:
        return ["platelet", "megakaryocyte", "blood", "single-cell"]
    if "monocyte" in text:
        return ["monocyte", "myeloid", "blood", "PBMC", "single-cell"]
    if "b cells" in text:
        return ["B cell", "lymphocyte", "blood", "PBMC", "single-cell"]
    if "t cells" in text:
        return ["T cell", "lymphocyte", "blood", "PBMC", "single-cell"]
    return ["immune", "blood", "PBMC", "single-cell"]


def build_queries(gene: str, cell_types: set[str]) -> list[str]:
    context = " OR ".join(f'"{term}"[Title/Abstract]' for term in context_terms(cell_types))
    symbol = f'"{gene}"[Title/Abstract]'
    return [
        f"{symbol} AND ({context})",
        f"{symbol} AND humans[MeSH Terms]",
        symbol,
    ]


def search_pubmed(gene: str, cell_types: set[str], cache: dict[str, dict]) -> dict:
    cached = cache.get(gene)
    if cached:
        return cached
    endpoint = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    selected_query = ""
    ids: list[str] = []
    for query in build_queries(gene, cell_types):
        ids = []
        for payload_attempt in range(4):
            response = request_with_retries(
                endpoint,
                {
                    "db": "pubmed",
                    "term": query,
                    "retmode": "json",
                    "retmax": "15",
                    "sort": "relevance",
                    "tool": "pbmc3k_phase7_all_clusters",
                },
            )
            payload = response.json().get("esearchresult", {})
            if "idlist" in payload:
                ids = payload["idlist"]
                break
            if payload_attempt < 3:
                time.sleep(2 ** (payload_attempt + 1))
        else:
            print(f"{gene}: PubMed search payload remained unusable for query {query!r}.")
        selected_query = query
        if ids:
            break
    result = {"query": selected_query, "candidate_pmids": ids}
    cache[gene] = result
    return result


def gene_pattern(gene: str) -> re.Pattern:
    return re.compile(rf"(?<![A-Za-z0-9]){re.escape(gene)}(?![A-Za-z0-9])", re.IGNORECASE)


def gene_specific_match(gene: str, text: str) -> bool:
    """Require disambiguating biological language for symbols with common acronym collisions."""
    lowered = text.lower()
    if gene == "CFD":
        return "complement factor d" in lowered or bool(
            re.search(r"\bcfd\s*[+⁺]", text, flags=re.IGNORECASE)
        )
    if gene == "LTB":
        return "lymphotoxin beta" in lowered or bool(
            re.search(r"\bltb\s*[+⁺]", text, flags=re.IGNORECASE)
        ) or "expressing ltb" in lowered
    return bool(gene_pattern(gene).search(text))


def classify_study(row: pd.Series) -> str:
    text = " ".join(
        [
            str(row["title"]),
            str(row["abstract"]),
            str(row["publication_types"]),
            str(row["mesh_terms"]),
        ]
    ).lower()
    publication_types = str(row["publication_types"]).lower()
    mesh_terms = str(row["mesh_terms"]).lower()
    is_review = "review" in publication_types
    is_human = "humans" in mesh_terms
    is_animal = any(term in mesh_terms for term in ["mice", "animals"])
    is_single_cell = any(
        term in text for term in ["single-cell", "single cell", "scrna-seq", "spatial transcript"]
    )
    is_computational = any(
        term in text for term in ["bioinformatic", "database", "machine learning", "computational"]
    )
    is_laboratory = any(
        term in text
        for term in [
            "cells, cultured",
            "cell line",
            "in vitro",
            "knockout",
            "experimental",
            "transfection",
        ]
    )
    if is_review:
        return "Review"
    if is_human and is_single_cell:
        return "Human single-cell/transcriptomic study"
    if is_human and is_animal:
        return "Human and laboratory/animal study"
    if is_human and is_laboratory:
        return "Human laboratory study"
    if is_human:
        return "Human study"
    if is_animal:
        return "Laboratory/animal study"
    if is_computational:
        return "Computational study"
    if is_laboratory:
        return "Laboratory or other primary study"
    return "Other PubMed-indexed study"


def candidate_score(row: pd.Series, gene: str) -> tuple[int, int, int, int]:
    title = str(row["title"])
    text = f"{title} {row['abstract']}"
    study_type = str(row["study_type"])
    exact_title = int(bool(gene_pattern(gene).search(title)))
    human = int(study_type.startswith("Human"))
    review = int(study_type == "Review")
    focused = int(
        any(
            term in text.lower()
            for term in ["single-cell", "single cell", "pbmc", "blood", "lymphocyte", "monocyte", "platelet"]
        )
    )
    return (exact_title, human + review, focused, int(row["year"]) if pd.notna(row["year"]) else 0)


def select_gene_records(gene: str, candidates: pd.DataFrame, max_records: int = 3) -> pd.DataFrame:
    if candidates.empty:
        return candidates.copy()
    candidates = candidates[
        ~candidates["PMID"].astype(str).isin(MANUAL_RELEVANCE_EXCLUSIONS.get(gene, set()))
    ].copy()
    if candidates.empty:
        return candidates
    matched = candidates[
        candidates.apply(
            lambda row: gene_specific_match(gene, f"{row['title']} {row['abstract']}"),
            axis=1,
        )
    ].copy()
    if matched.empty:
        return matched
    matched["study_type"] = matched.apply(classify_study, axis=1)
    matched["_score"] = matched.apply(lambda row: candidate_score(row, gene), axis=1)
    matched = matched.sort_values("_score", ascending=False, kind="stable")

    chosen_indices = []
    # Preserve evidence diversity: one review when available, then strongest primary records.
    review_indices = matched.index[matched["study_type"].eq("Review")].tolist()
    if review_indices:
        chosen_indices.append(review_indices[0])
    for index in matched.index:
        if index not in chosen_indices:
            chosen_indices.append(index)
        if len(chosen_indices) >= max_records:
            break
    return matched.loc[chosen_indices].drop(columns="_score")


def evidence_excerpt(row: pd.Series, gene: str) -> str:
    abstract = re.sub(r"\s+", " ", str(row["abstract"])).strip()
    sentences = re.split(r"(?<=[.!?])\s+", abstract)
    pattern = gene_pattern(gene)
    candidates = [sentence for sentence in sentences if pattern.search(sentence)]
    if candidates:
        excerpt = candidates[0].strip()
    elif pattern.search(str(row["title"])):
        excerpt = (
            f"The publication title identifies {gene} as its subject: "
            f"{str(row['title']).strip()}"
        )
    elif sentences:
        excerpt = sentences[-1].strip()
    else:
        excerpt = str(row["title"]).strip()
    if len(excerpt) > 420:
        excerpt = excerpt[:417].rsplit(" ", 1)[0] + "..."
    return f"PubMed abstract evidence: {excerpt}"


def evidence_categories(row: pd.Series) -> str:
    study_type = str(row["study_type"])
    text = f"{row['title']} {row['abstract']}".lower()
    categories = []
    if study_type == "Review":
        categories.append("Review")
    else:
        categories.append("Association")
    if any(term in text for term in ["mechanism", "regulat", "required", "inhibit", "activation"]):
        categories.append("Mechanism")
    if any(term in text for term in ["marker", "expression", "single-cell", "single cell"]):
        categories.append("Biomarker")
    if any(
        term in study_type.lower()
        for term in ["laboratory", "animal", "primary", "human study", "single-cell"]
    ):
        categories.append("Experimental evidence")
    return "; ".join(dict.fromkeys(categories))


def assign_grade(gene_refs: pd.DataFrame) -> tuple[str, str]:
    if gene_refs.empty:
        return (
            "E",
            "Selected evidence is insufficient: no verified gene-specific PubMed record met the focused relevance criteria.",
        )
    types = gene_refs["study_type"].astype(str)
    human_primary = int(types.str.startswith("Human").sum())
    reviews = int(types.eq("Review").sum())
    experimental = int(
        types.str.contains("Laboratory|animal|primary", case=False, regex=True).sum()
    )
    computational = int(types.str.contains("Computational", case=False).sum())
    if human_primary >= 3:
        return (
            "A",
            f"Repeated human evidence: {human_primary} primary human studies; "
            f"{reviews} review(s) provide context but do not determine the grade.",
        )
    if human_primary >= 2:
        return (
            "B",
            f"Multiple human studies: {human_primary} primary human studies; "
            f"{reviews} review(s) provide context but do not determine the grade.",
        )
    if experimental >= 1:
        return (
            "C",
            f"Laboratory or animal evidence predominates ({experimental} selected experimental "
            "study/studies); repeated human evidence is insufficient.",
        )
    if computational >= 1:
        return (
            "D",
            "Selected evidence is computational and lacks stronger primary experimental support "
            "in this collection.",
        )
    return (
        "E",
        "Selected evidence is limited and does not meet the thresholds for grades A–D.",
    )


def md_table(frame: pd.DataFrame) -> str:
    shown = frame.fillna("").astype(str)
    headers = list(shown.columns)
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in shown.itertuples(index=False, name=None):
        clean = [str(value).replace("|", "\\|").replace("\n", " ") for value in row]
        lines.append("| " + " | ".join(clean) + " |")
    return "\n".join(lines)


def profile_for_gene(gene: str, gene_refs: pd.DataFrame) -> dict:
    if gene_refs.empty:
        return {
            "official_name": gene,
            "immune_function": (
                "Direct gene-specific immune evidence was not identified by the focused PubMed "
                "search; the supplied evidence is insufficient to assign a literature-supported function."
            ),
            "immune_cells": (
                "No literature-supported immune-cell context is assigned from this evidence collection."
            ),
            "biological_role": (
                "No mechanism is assigned. The supplied evidence is insufficient to determine this."
            ),
            "function_tags": ["insufficient direct evidence"],
            "pathway_tags": ["no pathway assigned"],
            "disease_tags": ["no evidence-based disease context assigned"],
            "plain": (
                f"The focused search did not find enough direct evidence to explain {gene}; "
                "the dataset observation remains separate from literature claims."
            ),
        }
    return {
        "official_name": gene,
        "immune_function": (
            f"The selected PubMed collection discusses {gene} in publication-specific biological "
            "or immune contexts; claims are limited to the verified article summaries below."
        ),
        "immune_cells": (
            "Cell contexts vary across the selected publications; no cell type is treated as unique."
        ),
        "biological_role": (
            "No single cross-publication mechanism is asserted; publication-specific evidence is listed below."
        ),
        "function_tags": ["gene-specific literature evidence"],
        "pathway_tags": ["publication-specific; no combined pathway inference"],
        "disease_tags": ["publication contexts only"],
        "plain": (
            f"Selected PubMed records provide context for {gene}, but they do not by themselves "
            "establish what the gene does in this PBMC3k cluster."
        ),
    }


def disease_section(gene_refs: pd.DataFrame) -> str:
    category_order = ["Association", "Mechanism", "Biomarker", "Experimental evidence"]
    lines = []
    for category in category_order:
        subset = gene_refs[
            gene_refs["evidence_categories"].astype(str).str.contains(
                category, case=False, regex=False
            )
        ]
        lines.append(f"### {category}\n")
        if subset.empty:
            lines.append(
                "No publication in the selected evidence set was assigned to this category.\n"
            )
        else:
            for row in subset.itertuples():
                lines.append(f"- PMID {row.PMID}: {row.summary}\n")
    return "\n".join(lines)


def gene_report(
    gene: str,
    markers: pd.DataFrame,
    profile: dict,
    gene_refs: pd.DataFrame,
    grade: str,
    grade_explanation: str,
) -> str:
    dataset_table = markers[
        [
            "cluster",
            "cell_type",
            "representative_rank",
            "marker_score",
            "avg_log2FC",
            "pct_in",
            "pct_out",
            "specificity_delta",
        ]
    ].copy()
    literature_blocks = []
    for ref in gene_refs.itertuples(index=False):
        doi_text = ref.DOI if ref.DOI else "not listed in the PubMed record"
        literature_blocks.append(
            f"### {ref.title}\n\n"
            f"- **Journal:** {ref.journal}\n"
            f"- **Year:** {ref.year}\n"
            f"- **PMID:** [{ref.PMID}](https://pubmed.ncbi.nlm.nih.gov/{ref.PMID}/)\n"
            f"- **DOI:** {doi_text}\n"
            f"- **Study type:** {ref.study_type}\n"
            f"- **Organizing summary:** {ref.summary}\n"
        )
    literature_text = (
        "\n".join(literature_blocks)
        if literature_blocks
        else "No verified gene-specific PubMed record met the focused relevance criteria."
    )
    return f"""# {gene} — Literature Evidence File

> Scope: evidence collection only. Dataset observations, publication findings, and future interpretation are kept separate.

## Dataset Evidence

{md_table(dataset_table)}

These are observations from this PBMC3k analysis, not literature claims.

## Biological Function

- **Official gene name:** {profile['official_name']}
- **Immune function:** {profile['immune_function']}
- **Common immune-cell contexts:** {profile['immune_cells']}
- **Reported biological role:** {profile['biological_role']}

## Literature Evidence

{literature_text}

## Disease Associations

{disease_section(gene_refs)}

**Safety statement:** These are contexts reported by publications. Expression of {gene} in this dataset does not diagnose, predict, or demonstrate any disease.

## Evidence Grade

**{grade}** — {grade_explanation}

The grade applies only to this selected literature collection and may change as evidence is added.

## Limitations

- Association is not diagnosis and does not establish causality.
- Gene expression is context-dependent and can change with cell state or stimulation.
- Evidence from tumors, infected tissue, animal models, or cell lines may not transfer to peripheral blood.
- Cell-type and tissue specificity limit generalization.
- A marker can identify a cell state without being the mechanism that creates that state.
- This is a focused evidence set, not a formal systematic review or meta-analysis.

## Plain Language Notes

{profile['plain']}

Finding this gene in PBMC3k helps describe the cells. By itself, it cannot reveal a person's health, identity, or future.

## Deferred to Notebook 08

No combined biological conclusion is made here. Future synthesis must preserve uncertainty and distinguish this dataset from the cited study populations.
"""


def cluster_report(
    cluster: str,
    cell_type: str,
    cluster_markers: pd.DataFrame,
    cluster_summary: pd.DataFrame,
    profiles: dict[str, dict],
) -> str:
    def tag_counts(field: str) -> Counter:
        return Counter(
            tag for gene in cluster_markers["gene"] for tag in profiles[gene][field]
        )

    def count_lines(counts: Counter) -> str:
        return "\n".join(
            f"- {term}: tagged for {count} gene(s)" for term, count in counts.most_common()
        )

    grade_table = cluster_summary[
        ["gene", "evidence_grade", "publication_count", "grade_explanation"]
    ].copy()
    grade_table.columns = ["Gene", "Grade", "References", "Reason"]
    return f"""# Literature Reference Report — Cluster {cluster}: {cell_type}

> This document organizes evidence for later analysis. It does not interpret the genes as a combined program and does not make a biological or clinical conclusion.

## Selected Genes

{', '.join(cluster_markers['gene'])}

## Dataset Boundary

The genes were selected from the Phase 6 marker ranking for cluster {cluster}. Marker statistics are dataset observations. All publication claims come from the verified references table. Publication contexts do not describe or diagnose the PBMC3k source.

## Recurring Biological Functions

{count_lines(tag_counts('function_tags'))}

## Recurring Immune Pathways

{count_lines(tag_counts('pathway_tags'))}

## Recurring Disease Themes in the Selected Publications

{count_lines(tag_counts('disease_tags'))}

These are indexing tags, not evidence of disease in this dataset and not formal enrichment results.

## Confidence of Literature

{md_table(grade_table)}

Grades describe the selected evidence set using the explicit A–E rules in Notebook 07. A high grade does not make every reported mechanism universal or causal.

## Unanswered Biological Questions

- Which selected markers are stable across independent PBMC cohorts?
- Which publication-specific findings transfer to this cluster and tissue context?
- Which claims have independent protein-level and functional support?
- Which grade-E genes need better direct literature evidence?

## Future Interpretation

Cross-gene reasoning, pathway synthesis, and biological conclusions are intentionally deferred to Notebook 08.
"""


def main() -> None:
    PHASE7.mkdir(parents=True, exist_ok=True)
    GENE_DIR.mkdir(parents=True, exist_ok=True)
    selected = pd.read_csv(PHASE6 / "selected_marker_genes.csv", dtype={"cluster": str})
    selected = selected.sort_values(
        ["cluster", "representative_rank"],
        key=lambda column: column.map(natural_cluster_key)
        if column.name == "cluster"
        else column,
        kind="stable",
    )
    phase6_pairs = set(zip(selected["cluster"], selected["gene"]))
    valid_clusters = set(selected["cluster"])
    unique_genes = set(selected["gene"])

    original_summary = pd.read_csv(LITERATURE_PATH, dtype={"cluster": str})
    original_references = pd.read_csv(REFERENCES_PATH, dtype={"PMID": str})
    cluster5_summary = original_summary[original_summary["cluster"].eq("5")].copy()
    cluster5_genes = set(cluster5_summary["gene"])
    cluster5_references = original_references[
        original_references["gene"].isin(cluster5_genes)
    ].copy()
    original_report = CLUSTER_REPORT_PATH.read_text(encoding="utf-8")
    cluster5_report = original_report.split(REPORT_SEPARATOR, 1)[0].rstrip() + "\n"
    cluster5_gene_bytes = {
        gene: (GENE_DIR / f"{gene}.md").read_bytes() for gene in cluster5_genes
    }

    cache = json.loads(CACHE_PATH.read_text()) if CACHE_PATH.exists() else {}
    new_genes = sorted(unique_genes - cluster5_genes)
    gene_candidates: dict[str, list[str]] = {}
    for index, gene in enumerate(new_genes, start=1):
        cell_types = set(selected.loc[selected["gene"].eq(gene), "cell_type"])
        search_result = search_pubmed(gene, cell_types, cache)
        gene_candidates[gene] = search_result["candidate_pmids"]
        CACHE_PATH.write_text(json.dumps(cache, indent=2), encoding="utf-8")
        print(
            f"[{index:02d}/{len(new_genes)}] {gene}: "
            f"{len(search_result['candidate_pmids'])} PubMed candidate(s)"
        )
    all_candidate_pmids = sorted(
        {pmid for values in gene_candidates.values() for pmid in values}
    )
    candidate_records = fetch_pubmed_records(all_candidate_pmids)
    returned_pmids = set(candidate_records["PMID"].astype(str))
    missing_candidate_pmids = set(all_candidate_pmids) - returned_pmids
    if missing_candidate_pmids:
        print(
            "Excluding ESearch hits that EFetch did not return as PubMed articles: "
            f"{sorted(missing_candidate_pmids)}"
        )
        gene_candidates = {
            gene: [pmid for pmid in pmids if pmid in returned_pmids]
            for gene, pmids in gene_candidates.items()
        }

    new_reference_parts = []
    search_links: dict[str, set[str]] = {}
    for gene in new_genes:
        candidates = candidate_records[
            candidate_records["PMID"].isin(gene_candidates[gene])
        ].copy()
        chosen = select_gene_records(gene, candidates)
        search_links[gene] = set(chosen["PMID"].astype(str))
        if chosen.empty:
            print(f"{gene}: insufficient direct evidence; no reference selected.")
            continue
        chosen["gene"] = gene
        chosen["summary"] = chosen.apply(lambda row: evidence_excerpt(row, gene), axis=1)
        chosen["evidence_categories"] = chosen.apply(evidence_categories, axis=1)
        new_reference_parts.append(chosen)
        print(f"{gene}: selected {len(chosen)} verified reference(s).")

    if new_reference_parts:
        new_references = pd.concat(new_reference_parts, ignore_index=True)
    else:
        new_references = pd.DataFrame(columns=cluster5_references.columns)

    grade_lookup: dict[str, tuple[str, str]] = {}
    for gene in new_genes:
        grade_lookup[gene] = assign_grade(new_references[new_references["gene"].eq(gene)])
    for gene in cluster5_genes:
        row = cluster5_summary[cluster5_summary["gene"].eq(gene)].iloc[0]
        grade_lookup[gene] = (str(row["evidence_grade"]), str(row["grade_explanation"]))

    if not new_references.empty:
        new_references["evidence_grade"] = new_references["gene"].map(
            lambda gene: grade_lookup[gene][0]
        )
    combined_references = pd.concat(
        [
            cluster5_references[REFERENCE_COLUMNS],
            new_references.reindex(columns=REFERENCE_COLUMNS),
        ],
        ignore_index=True,
    )
    combined_references["PMID"] = combined_references["PMID"].astype(str)
    combined_references = combined_references.sort_values(
        ["gene", "year", "PMID"], kind="stable"
    ).reset_index(drop=True)

    profiles: dict[str, dict] = {}
    for gene in cluster5_genes:
        row = cluster5_summary[cluster5_summary["gene"].eq(gene)].iloc[0]
        profiles[gene] = {
            "official_name": row["official_gene_name"],
            "immune_function": row["immune_function"],
            "immune_cells": row["immune_cell_contexts"],
            "biological_role": row["biological_role"],
            "function_tags": str(row["function_tags"]).split("; "),
            "pathway_tags": str(row["pathway_tags"]).split("; "),
            "disease_tags": str(row["disease_context_tags"]).split("; "),
            "plain": row["plain_language_note"],
        }
    for gene in new_genes:
        profiles[gene] = profile_for_gene(
            gene, combined_references[combined_references["gene"].eq(gene)]
        )

    summary_rows = cluster5_summary.to_dict(orient="records")
    for marker in selected[~selected["cluster"].eq("5")].itertuples(index=False):
        gene = marker.gene
        profile = profiles[gene]
        gene_refs = combined_references[combined_references["gene"].eq(gene)]
        grade, explanation = grade_lookup[gene]
        summary_rows.append(
            {
                "gene": gene,
                "cluster": marker.cluster,
                "cell_type": marker.cell_type,
                "representative_rank": int(marker.representative_rank),
                "marker_score": marker.marker_score,
                "avg_log2FC": marker.avg_log2FC,
                "pct_in": marker.pct_in,
                "pct_out": marker.pct_out,
                "official_gene_name": profile["official_name"],
                "immune_function": profile["immune_function"],
                "immune_cell_contexts": profile["immune_cells"],
                "biological_role": profile["biological_role"],
                "function_tags": "; ".join(profile["function_tags"]),
                "pathway_tags": "; ".join(profile["pathway_tags"]),
                "disease_context_tags": "; ".join(profile["disease_tags"]),
                "publication_count": len(gene_refs),
                "evidence_grade": grade,
                "grade_explanation": explanation,
                "plain_language_note": profile["plain"],
                "interpretation_status": "Deferred to Notebook 08",
            }
        )
    literature_summary = pd.DataFrame(summary_rows)[SUMMARY_COLUMNS]
    literature_summary["_cluster_order"] = literature_summary["cluster"].map(
        natural_cluster_key
    )
    literature_summary = literature_summary.sort_values(
        ["_cluster_order", "representative_rank"], kind="stable"
    ).drop(columns="_cluster_order")

    # Preserve every existing Cluster 5 row value.
    new_cluster5 = literature_summary[literature_summary["cluster"].eq("5")].reset_index(
        drop=True
    )
    pd.testing.assert_frame_equal(
        cluster5_summary[SUMMARY_COLUMNS].reset_index(drop=True),
        new_cluster5[SUMMARY_COLUMNS],
        check_dtype=False,
    )
    pd.testing.assert_frame_equal(
        cluster5_references[REFERENCE_COLUMNS]
        .sort_values(["gene", "year", "PMID"], kind="stable")
        .reset_index(drop=True),
        combined_references[combined_references["gene"].isin(cluster5_genes)]
        [REFERENCE_COLUMNS]
        .sort_values(["gene", "year", "PMID"], kind="stable")
        .reset_index(drop=True),
        check_dtype=False,
    )

    # New gene files only; validated Cluster 5 gene files are never overwritten.
    for gene in new_genes:
        markers = selected[selected["gene"].eq(gene)].copy()
        gene_refs = combined_references[combined_references["gene"].eq(gene)].copy()
        grade, explanation = grade_lookup[gene]
        (GENE_DIR / f"{gene}.md").write_text(
            gene_report(gene, markers, profiles[gene], gene_refs, grade, explanation),
            encoding="utf-8",
        )
    for gene, expected_bytes in cluster5_gene_bytes.items():
        if (GENE_DIR / f"{gene}.md").read_bytes() != expected_bytes:
            raise AssertionError(f"Validated Cluster 5 gene file changed: {gene}")

    additional_reports = []
    for cluster in sorted(valid_clusters - {"5"}, key=natural_cluster_key):
        markers = selected[selected["cluster"].eq(cluster)]
        cell_type = str(markers["cell_type"].iloc[0])
        summary = literature_summary[literature_summary["cluster"].eq(cluster)]
        additional_reports.append(
            cluster_report(cluster, cell_type, markers, summary, profiles)
        )
    combined_cluster_report = (
        cluster5_report
        + REPORT_SEPARATOR
        + "\n\n---\n\n".join(additional_reports)
        + "\n"
    )

    coverage_rows = []
    for cluster in sorted(valid_clusters, key=natural_cluster_key):
        markers = selected[selected["cluster"].eq(cluster)]
        summary = literature_summary[literature_summary["cluster"].eq(cluster)]
        with_evidence = summary["publication_count"].gt(0)
        insufficient = summary["evidence_grade"].eq("E") & ~with_evidence
        status = (
            "COMPLETE"
            if len(summary) == len(markers)
            and (with_evidence | insufficient).all()
            else "PARTIAL"
            if len(summary)
            else "NOT_STARTED"
        )
        cluster_genes = set(markers["gene"])
        coverage_rows.append(
            {
                "cluster_id": cluster,
                "proposed_cell_type": str(markers["cell_type"].iloc[0]),
                "representative_gene_count": len(markers),
                "genes_with_evidence": int(with_evidence.sum()),
                "genes_with_verified_references": int(
                    summary.loc[with_evidence, "gene"].nunique()
                ),
                "genes_with_insufficient_evidence": int(insufficient.sum()),
                "verified_reference_count": int(
                    combined_references[
                        combined_references["gene"].isin(cluster_genes)
                    ]["PMID"].nunique()
                ),
                "phase7_status": status,
            }
        )
    coverage = pd.DataFrame(coverage_rows)

    reuse_rows = []
    gene_clusters = selected.groupby("gene")["cluster"].agg(
        lambda values: sorted(set(values), key=natural_cluster_key)
    )
    for gene in sorted(unique_genes):
        clusters = gene_clusters[gene]
        has_evidence = bool(
            len(combined_references[combined_references["gene"].eq(gene)])
        )
        reuse_rows.append(
            {
                "gene": gene,
                "clusters_using_gene": "; ".join(clusters),
                "evidence_reused": len(clusters) > 1 and has_evidence,
                "source_evidence_file": f"results/phase7/genes/{gene}.md",
                "notes": (
                    "The same verified gene-level evidence is reused; each cluster retains "
                    "its own marker statistics and later interpretation."
                    if len(clusters) > 1 and has_evidence
                    else "No cross-cluster evidence reuse."
                    if len(clusters) == 1
                    else "Gene recurs, but no verified reference met the focused criteria."
                ),
            }
        )
    reuse = pd.DataFrame(reuse_rows)

    validation_errors = []
    required_summary = set(SUMMARY_COLUMNS)
    required_references = set(REFERENCE_COLUMNS)
    if not required_summary.issubset(literature_summary.columns):
        validation_errors.append("literature_summary.csv is missing required fields.")
    if not required_references.issubset(combined_references.columns):
        validation_errors.append("references.csv is missing required fields.")
    if set(zip(literature_summary["cluster"], literature_summary["gene"])) != phase6_pairs:
        validation_errors.append("Literature-summary cluster–gene coverage differs from Phase 6.")
    if not set(literature_summary["cluster"]).issubset(valid_clusters):
        validation_errors.append("Literature summary contains an invalid cluster ID.")
    if not set(literature_summary["gene"]).issubset(unique_genes):
        validation_errors.append("Literature summary contains a gene absent from Phase 6.")
    if not set(combined_references["gene"]).issubset(unique_genes):
        validation_errors.append("References contain a gene absent from Phase 6.")
    if not set(literature_summary["evidence_grade"]).issubset(ALLOWED_GRADES):
        validation_errors.append("An evidence grade is outside A–E.")
    if not combined_references["PMID"].str.fullmatch(r"\d+").all():
        validation_errors.append("A PMID is malformed.")
    if combined_references["title"].fillna("").str.len().eq(0).any():
        validation_errors.append("A verified reference title is missing.")
    if combined_references.duplicated(["gene", "PMID"]).any():
        validation_errors.append("A gene–PMID reference link is duplicated.")
    verified_pmids = set(
        fetch_pubmed_records(sorted(set(combined_references["PMID"])))["PMID"].astype(str)
    )
    if verified_pmids != set(combined_references["PMID"]):
        validation_errors.append("At least one cited PMID was not reverified by PubMed.")
    for gene in new_genes:
        gene_refs = combined_references[combined_references["gene"].eq(gene)]
        if not gene_refs.empty:
            allowed = search_links[gene]
            if not set(gene_refs["PMID"]).issubset(allowed):
                validation_errors.append(
                    f"{gene}: a reference was not selected from its gene-specific search."
                )
            for row in gene_refs.itertuples(index=False):
                source = candidate_records[
                    candidate_records["PMID"].eq(row.PMID)
                ].iloc[0]
                if not gene_specific_match(gene, f"{source['title']} {source['abstract']}"):
                    validation_errors.append(
                        f"{gene}: PMID {row.PMID} does not contain the gene in title/abstract."
                    )
        else:
            rows = literature_summary[literature_summary["gene"].eq(gene)]
            acknowledged = (
                rows["evidence_grade"].eq("E").all()
                and rows["publication_count"].eq(0).all()
                and rows["grade_explanation"]
                .str.contains("insufficient", case=False)
                .all()
            )
            if not acknowledged:
                validation_errors.append(
                    f"{gene}: missing evidence is not explicitly acknowledged."
                )
    if not coverage["phase7_status"].eq("COMPLETE").all():
        validation_errors.append("At least one cluster is not COMPLETE.")
    if not literature_summary["interpretation_status"].eq(
        "Deferred to Notebook 08"
    ).all():
        validation_errors.append("A summary row bypasses Notebook 08 interpretation.")

    validation_report = {
        "status": "PASS" if not validation_errors else "FAIL",
        "errors": validation_errors,
        "valid_clusters": sorted(valid_clusters, key=natural_cluster_key),
        "cluster_gene_entries": len(literature_summary),
        "unique_genes": len(unique_genes),
        "verified_reference_rows": len(combined_references),
        "verified_unique_pmids": combined_references["PMID"].nunique(),
    }

    # Write only after all evidence assembly and verification has completed.
    literature_summary.to_csv(LITERATURE_PATH, index=False)
    combined_references[REFERENCE_COLUMNS].to_csv(REFERENCES_PATH, index=False)
    CLUSTER_REPORT_PATH.write_text(combined_cluster_report, encoding="utf-8")
    coverage.to_csv(COVERAGE_PATH, index=False)
    reuse.to_csv(REUSE_PATH, index=False)
    VALIDATION_PATH.write_text(json.dumps(validation_report, indent=2), encoding="utf-8")

    clusters_completed = coverage.loc[
        coverage["phase7_status"].eq("COMPLETE"), "cluster_id"
    ].tolist()
    insufficient_genes = sorted(
        literature_summary.loc[
            literature_summary["publication_count"].eq(0), "gene"
        ].unique()
    )
    print("\nPhase 7 completion summary")
    print(f"- Clusters completed: {', '.join(clusters_completed)}")
    print(f"- Total unique genes reviewed: {len(unique_genes)}")
    print(f"- Total cluster-gene entries covered: {len(literature_summary)}")
    print(f"- Total verified reference rows: {len(combined_references)}")
    print(f"- Total unique verified PMIDs: {combined_references['PMID'].nunique()}")
    print(
        "- Genes with insufficient evidence: "
        + (", ".join(insufficient_genes) if insufficient_genes else "None")
    )
    print(f"- Validation: {validation_report['status']}")
    print(
        "- Remaining gaps: "
        + (
            "; ".join(validation_errors)
            if validation_errors
            else "No structural or citation-validation gaps; grade-E genes remain explicitly limited."
        )
    )
    if validation_errors:
        raise RuntimeError("Phase 7 validation failed: " + "; ".join(validation_errors))


if __name__ == "__main__":
    main()
