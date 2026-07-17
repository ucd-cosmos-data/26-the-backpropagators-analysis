# PBMC3k

This folder contains the unmodified Cell Ranger 1.1.0 outputs for the **3k
PBMCs from a Healthy Donor** dataset.

---

## 1. Source

- **Provider:** 10x Genomics
- **Dataset name:** 3k PBMCs from a Healthy Donor
- **Dataset page:** [3k PBMCs from a Healthy Donor](https://www.10xgenomics.com/datasets/3-k-pbm-cs-from-a-healthy-donor-1-standard-1-1-0)
- **Output and supplemental files:**
  - [Genome-aligned BAM](https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_possorted_genome_bam.bam)
  - [Genome-aligned BAM index](https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_possorted_genome_bam_index.bam.bai)
  - [Per-molecule read information](https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_molecule_info.h5)
  - [Gene / cell matrix (filtered)](https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_filtered_gene_bc_matrices.tar.gz)
  - [Gene / cell matrix (raw)](https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_raw_gene_bc_matrices.tar.gz)
  - [Clustering analysis](https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_analysis.tar.gz)
  - [Summary CSV](https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_metrics_summary.csv)
  - [Summary HTML](https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_web_summary.html)
- **License:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

---

## 2. Folder structure

The downloads are stored in `PBMC3k/data/raw` without being renamed,
extracted, cleaned, or otherwise modified.

```text
PBMC3k/
├── README.md
└── data/
    └── raw/
        ├── pbmc3k_analysis.tar.gz
        ├── pbmc3k_filtered_gene_bc_matrices.tar.gz
        ├── pbmc3k_metrics_summary.csv
        ├── pbmc3k_molecule_info.h5
        ├── pbmc3k_possorted_genome_bam.bam
        ├── pbmc3k_possorted_genome_bam_index.bam.bai
        ├── pbmc3k_raw_gene_bc_matrices.tar.gz
        └── pbmc3k_web_summary.html
```

---

## 3. Download command

Run this command from the `PBMC3k` directory. The `curl` command downloads
all output and supplemental files listed on the dataset page.

```bash
mkdir -p data/raw
cd data/raw

curl --fail --location --remote-name-all --continue-at - \
  https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_possorted_genome_bam.bam \
  https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_possorted_genome_bam_index.bam.bai \
  https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_molecule_info.h5 \
  https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_filtered_gene_bc_matrices.tar.gz \
  https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_raw_gene_bc_matrices.tar.gz \
  https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_analysis.tar.gz \
  https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_metrics_summary.csv \
  https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_web_summary.html
```

## 4. What each command does

- `mkdir -p data/raw` creates the raw-data directory if it does not already
  exist. It does not overwrite existing files.
- `cd data/raw` makes the raw-data directory the destination for the files.
- `curl` transfers the files from the official 10x Genomics server.
- `--fail` makes `curl` report an error for an unsuccessful HTTP response
  instead of saving the server's error page as a data file.
- `--location` follows HTTP redirects.
- `--remote-name-all` preserves the filename supplied by 10x Genomics for
  every URL in the command.
- `--continue-at -` resumes an interrupted download from the existing file's
  size when the server supports byte-range requests.
- The trailing backslash (`\`) continues one shell command onto the next line.

## 5. Raw files

| Raw file | Meaning |
|---|---|
| `pbmc3k_possorted_genome_bam.bam` | Coordinate-sorted BAM containing sequencing reads aligned to the reference genome. |
| `pbmc3k_possorted_genome_bam_index.bam.bai` | BAM index used by compatible tools to access genomic regions without scanning the entire BAM. |
| `pbmc3k_molecule_info.h5` | HDF5 file containing per-molecule barcode, UMI, gene, and read-count information produced by Cell Ranger. |
| `pbmc3k_filtered_gene_bc_matrices.tar.gz` | Compressed sparse gene-by-cell count matrix restricted to barcodes Cell Ranger identified as cells. |
| `pbmc3k_raw_gene_bc_matrices.tar.gz` | Compressed sparse gene-by-barcode count matrix containing all observed barcodes, including background/empty droplets. |
| `pbmc3k_analysis.tar.gz` | Compressed Cell Ranger secondary-analysis output, including dimensionality reduction, clustering, and differential-expression results. |
| `pbmc3k_metrics_summary.csv` | One-row CSV of Cell Ranger run and quality-control summary metrics. |
| `pbmc3k_web_summary.html` | Standalone interactive HTML report of run metrics, quality-control results, and analysis summaries. |

## 6. Important rule

This instruction file is for downloading raw data only.

Do not do any of the following in this step:

- Do not rename columns.
- Do not clean the data.
- Do not remove rows.
- Do not create `train.csv` or `test.csv`.
- Do not create a `processed/` folder.
- Do not train a model.
- Do not calculate accuracy.
- Do not do visualization.

## 7. Usage in Python

The following code reads the first five cell observations directly from the
filtered matrix archive. It does not extract, alter, or write any raw data.
Run it from the `PBMC3k` directory with `pandas` and `scipy` installed.

```python
import tarfile

import pandas as pd
from scipy.io import mmread

archive_path = "data/raw/pbmc3k_filtered_gene_bc_matrices.tar.gz"

with tarfile.open(archive_path, "r:gz") as archive:
    members = {member.name: member for member in archive.getmembers()}

    matrix_name = next(name for name in members if name.endswith("/matrix.mtx"))
    genes_name = next(name for name in members if name.endswith("/genes.tsv"))
    barcodes_name = next(name for name in members if name.endswith("/barcodes.tsv"))

    matrix = mmread(archive.extractfile(members[matrix_name])).tocsr()
    genes = pd.read_csv(
        archive.extractfile(members[genes_name]),
        sep="\t",
        header=None,
        names=["gene_id", "gene_name"],
    )
    barcodes = pd.read_csv(
        archive.extractfile(members[barcodes_name]),
        sep="\t",
        header=None,
        names=["barcode"],
    )

first_five = pd.DataFrame.sparse.from_spmatrix(
    matrix[:, :5].T,
    index=barcodes.iloc[:5, 0],
    columns=genes["gene_name"],
)

print(first_five)
```
