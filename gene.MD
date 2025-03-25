# Gene Research

## Sequence Databases

- **GenBank** – A comprehensive database for storing publicly available DNA sequences. Useful for retrieving genetic sequences for comparative analysis.
- **RefSeq** – A curated database of reference sequences for genes, transcripts, and proteins. Used to standardize genomic research.
- **UniProt** – A repository of protein sequences and functional annotations. Essential for studying protein interactions and functions.
- **RCSB PDB** – Stores 3D structural models of proteins. Useful for understanding protein folding, interactions, and drug targeting.
- **KEGG (Kyoto Encyclopedia of Genes and Genomes)** – A pathway database that maps genes to biochemical networks. Critical for studying gene function within cellular pathways.
- **OMIM (Online Mendelian Inheritance in Man)** – A catalog of human genes and genetic disorders. Used for investigating genetic diseases.

## Sequence Alignment & Homology Search

- **BLAST (Basic Local Alignment Search Tool)** – Identifies sequence similarity and potential homologs. Crucial for functional annotation of unknown genes.
  - Sorted by E-value (Expect value) – Represents the probability that a match occurred by chance. Lower values indicate more statistically significant matches.
  - An E-value of 1000 suggests the match is likely random, whereas values <1 indicate a high-confidence alignment.
- **Pairwise Alignment Tools:**
  - **Needle (Needleman-Wunsch Algorithm)** – Global alignment, useful for comparing sequences of similar length and high similarity (e.g., orthologs).
  - **Water (Smith-Waterman Algorithm)** – Local alignment, useful for identifying conserved regions within large sequences.
  - **Dotmatcher** – Visualizes sequence similarity using dot plots. Larger window sizes reveal major trends, while smaller sizes show fine details but may introduce noise.

## Gene Prediction & Annotation

Predicting genes in eukaryotes is complex due to introns and exons. Several computational and biological markers assist in gene identification:

- **CpG Islands** – Regions of high GC content near promoters, identified using tools like CpGPlot.
  - Observed/expected CpG ratio >0.6 suggests a CpG island.
  - Methylation of CpG islands is linked to gene silencing.
- **Splice Sites** – Exons are flanked by conserved intron sequences, typically following the GT-AG rule.
- **Open Reading Frames (ORFs)** – Long stretches of codons without stop codons indicate possible coding sequences.
  - ORFs are identified by scanning all six reading frames.
  - Frames further down the sequence may be blocked due to prior translation initiation.
- **Regulatory Motifs** – Found using tools like JASPAR and MEME.
  - **JASPAR** – Stores transcription factor binding motifs as Position Frequency Matrices (PFMs).
  - **MEME** – Identifies novel regulatory motifs in DNA sequences.

## Functional Genomics & Variant Analysis

- **RNA-Seq Analysis** – Used to study gene expression levels across different conditions.
  - Tools: HISAT2, STAR for alignment; DESeq2 for differential expression analysis.
- **ChIP-Seq** – Identifies transcription factor binding sites.
  - Tools: MACS2 for peak calling.
- **ATAC-Seq** – Determines chromatin accessibility.
  - Tools: HOMER, TOBIAS for motif analysis.
- **Variant Annotation** – Used for interpreting genomic mutations.
  - Tools: ANNOVAR, VEP (Variant Effect Predictor).
- **GWAS (Genome-Wide Association Studies)** – Identifies SNPs associated with traits or diseases.
  - Tools: PLINK, GWAS Catalog.

## Structural & Evolutionary Genomics

- **Phylogenetics** – Used for reconstructing evolutionary relationships.
  - Tools: MEGA, IQ-TREE, BEAST.
- **Structural Variant Detection** – Identifies large genomic changes like deletions or duplications.
  - Tools: SVIM, Manta.
- **Comparative Genomics** – Aligns whole genomes across species to identify conserved elements.
  - Tools: Mauve, LASTZ.

## Epigenetics & Non-Coding RNA

- **DNA Methylation Analysis** – Assesses epigenetic modifications using bisulfite sequencing.
  - Tools: Bismark.
- **Histone Modifications** – Determines chromatin structure and regulation.
  - Tools: ChIPseeker.
- **Non-Coding RNA Analysis** – Predicts and annotates lncRNAs and miRNAs.
  - Tools: miRBase, RNAfold.

## CRISPR & Gene Editing

- **CRISPR Guide RNA Design** – Essential for genome editing.
  - Tools: CHOPCHOP, Benchling, CRISPRscan.
- **Off-Target Analysis** – Ensures precision in CRISPR experiments.
  - Tools: Cas-OFFinder, GuideScan.
- **Base Editing & Prime Editing** – Advanced genome editing methods.

## Bioinformatics & Programming Tools

- **Programming Languages**
  - **Python** – BioPython, scikit-bio for sequence manipulation.
  - **R** – Bioconductor for statistical genomics.
  - **Bash** – Essential for automating pipelines.
- **Machine Learning in Genomics**
  - DeepVariant – Uses deep learning for variant calling.
  - DeepSEA – Predicts enhancer activity using neural networks.

## Data Repositories & Visualization

- **UCSC Genome Browser** – Interactive genome visualization.
- **Ensembl** – Provides gene annotation and variation data.
- **Gencode** – High-quality human and mouse genome annotations.
- **TCGA (The Cancer Genome Atlas)** – Cancer-specific genomic alterations.
- **GTEx (Genotype-Tissue Expression Project)** – Gene expression data across tissues.
- **dbSNP** – Repository of single nucleotide polymorphisms.
- **ClinVar** – Database of clinically significant genetic variants.
