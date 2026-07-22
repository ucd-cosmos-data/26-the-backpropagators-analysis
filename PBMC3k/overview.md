# hi guys this is an overview of our dataset for our group!!

The PBMC3K dataset is probably the most widely used dataset in single-cell RNA sequencing (scRNA-seq). While it's often introduced as a machine learning or data analysis dataset, its real purpose is biological: it captures the gene activity of about 2,700 individual immune cells from the blood of a healthy human.

The key idea is simple:

Instead of measuring the average gene expression across millions of cells, PBMC3K measures each cell individually. Every row of data represents one cell's "snapshot" of which genes are turned on and how strongly.

Step 1: What are PBMCs?

PBMC stands for Peripheral Blood Mononuclear Cell.

Let's break that apart.

Peripheral blood

This simply means blood drawn from your veins (not bone marrow or organs).

Mononuclear

"Nucleus" means the compartment containing DNA.

Some blood cells have:

one round nucleus → mononuclear
multi-lobed nuclei → granulocytes like neutrophils

PBMCs only include cells with one nucleus.

Which cells are PBMCs?

PBMCs are mainly immune cells.

Cell Type	Approximate abundance	Job
T cells	~70%	Kill infected cells and coordinate immunity
B cells	~10%	Produce antibodies
NK cells	~10%	Kill infected and cancer cells
Monocytes	~10%	Become macrophages and clean up pathogens
Dendritic cells	Rare	Present antigens to activate T cells

Notice what is not included:

red blood cells
platelets
neutrophils
eosinophils
basophils

These are removed during PBMC isolation.

Step 2: Why study PBMCs?

PBMCs are one of the easiest human tissues to obtain.

Doctors only need a blood sample.

Because immune cells travel throughout the body, PBMCs are useful for studying

infection
cancer
autoimmune diseases
vaccines
aging
COVID
HIV
leukemia

Thousands of research papers use PBMCs because they provide a window into the immune system.

Step 3: What does one cell represent?

Imagine one T cell.

Inside that cell:

all ~20,000 human genes exist
only a subset are currently active

For example:

Gene      Expression

CD3D      340
IL7R      220
LTB       120
ACTB      500
MS4A1       0

This means:

CD3D is highly active
IL7R is active
ACTB is active (housekeeping)
MS4A1 is off

This activity pattern acts like a fingerprint that tells us what kind of cell it is.

Step 4: Gene expression

Genes are pieces of DNA.

DNA itself usually isn't measured.

Instead, scRNA-seq measures messenger RNA (mRNA), which reflects which genes are currently being used.

The flow is:

template
mRNA
3'
5'
5'
3'
T
A
C
G
T
T
A
G
C
A
U
G
C
A
base 5: template DNA T → mRNA A
Base
Base

DNA → mRNA → protein

If a cell contains many RNA copies of a gene, that gene is considered highly expressed.

Step 5: What do gene names mean?

Gene names follow standardized naming conventions.

Examples:

CD3D
CD = Cluster of Differentiation
3 = protein family
D = specific component

CD3 proteins are found almost exclusively on T cells.

Therefore:

High CD3D →
likely a T cell.

MS4A1

Official gene name:

MS4A1

Protein produced:

CD20

Biologists often use CD20 instead of MS4A1.

High MS4A1

→ B cell.

NKG7
Natural Killer Cell Granule Protein 7

High NKG7

→ NK cells.

LST1
Leukocyte Specific Transcript 1

Mostly expressed in

monocytes
macrophages
FCGR3A
Fc Gamma Receptor IIIA

Protein:

CD16

Common in

NK cells
CD16 monocytes
PPBP
Pro-Platelet Basic Protein

Very high

→ platelets

Sometimes platelet contamination appears in PBMC datasets.

Step 6: Marker genes

A marker gene is a gene that is much more active in one cell type than others.

For example

Cell Type	Marker genes
T cell	CD3D, CD3E, IL7R
B cell	MS4A1, CD79A, CD79B
NK cell	NKG7, GNLY
Monocyte	LST1, S100A8, FCGR3A
Dendritic cell	FCER1A, CST3
Platelet	PPBP

When clustering cells computationally, researchers often identify the cell type by checking which marker genes are highly expressed in each cluster.

Step 7: Major PBMC cell types
1. T cells

Largest population.

Role:

recognize infected cells
coordinate immune response
destroy virus-infected cells

Markers

CD3D
CD3E
IL7R
LTB

Subtypes include:

CD4 helper T cells
CD8 cytotoxic T cells
regulatory T cells
memory T cells
2. B cells

Produce antibodies.

Markers

MS4A1
CD79A
CD79B
HLA-DRA

After activation they become plasma cells.

3. NK cells

Natural killer cells belong to the innate immune system.

They can kill infected cells without prior exposure.

Markers

NKG7
GNLY
PRF1
FCGR3A

GNLY = granulysin

PRF1 = perforin

These proteins punch holes in target cells.

4. Monocytes

Large circulating immune cells.

Jobs:

engulf bacteria
become macrophages
become dendritic cells
produce inflammatory signals

Markers

LST1
S100A8
S100A9
FCGR3A
CTSS

There are two major types:

Classical

S100A8
S100A9

Non-classical

FCGR3A
5. Dendritic cells

Professional antigen-presenting cells.

They "show" fragments of pathogens to T cells, helping initiate adaptive immune responses.

Markers

FCER1A
CST3
HLA-DRA

They are uncommon but important.

Step 8: Housekeeping genes

Some genes are active in nearly every cell because they're needed for basic cellular function.

Examples

ACTB
GAPDH
RPL13A
RPS18

These genes are involved in:

metabolism
ribosomes
cytoskeleton
energy production

High expression of housekeeping genes does not indicate cell identity—they simply reflect essential cellular processes.

Step 9: Why aren't all genes expressed?

Every cell contains the same DNA.

The difference between a neuron and a T cell is which genes are turned on.

Think of the genome as a giant library:

every cell owns every book (gene)
each cell reads only the books relevant to its job

A T cell reads:

CD3D
IL7R

A B cell reads:

MS4A1
CD79A

A neuron would read entirely different genes.

Gene expression defines a cell's identity and function.

Step 10: Why do some genes have very high numbers?

Some proteins are needed in large quantities.

For example:

ACTB

(actin)

The cell constantly needs actin to maintain its shape, so many mRNA copies are present.

Similarly,

MALAT1

is an abundant non-coding RNA involved in regulating gene expression, making it one of the highest-expressed transcripts in many cell types.

High expression does not necessarily mean a gene is biologically more important—it may simply be required in large amounts.

Step 11: Putting it all together

Imagine you observe a cell with the following expression profile:

Gene	Expression
CD3D	420
CD3E	360
IL7R	240
NKG7	2
MS4A1	0
LST1	1

A biologist would reason:

High CD3D and CD3E indicate a T-cell receptor complex.
High IL7R is characteristic of many helper or memory T cells.
MS4A1 is absent, so it's unlikely to be a B cell.
LST1 is nearly absent, so it's unlikely to be a monocyte.
NKG7 is very low, making an NK cell unlikely.

Conclusion: this cell is most likely a CD4⁺ helper or memory T cell.

Why PBMC3K is so valuable

The PBMC3K dataset is a benchmark because it contains several well-understood immune cell types whose identities can be inferred from their gene expression patterns. This makes it ideal for learning how single-cell RNA sequencing works: each individual cell is represented by thousands of gene-expression measurements, and differences in those measurements reveal distinct cell populations without needing to know their identities in advance.

When you cluster the cells computationally, you're essentially grouping together cells with similar "gene activity fingerprints." Looking at marker genes then lets you assign biological identities to those clusters. In other words, cell type emerges from patterns of gene expression rather than being predefined—which is the central biological insight behind single-cell transcriptomics.