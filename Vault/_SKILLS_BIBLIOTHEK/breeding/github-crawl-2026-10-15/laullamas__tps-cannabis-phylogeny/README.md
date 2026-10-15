# Terpene synthase phylogeny in *Cannabis sativa*

Phylogenetic analysis of the TPS gene family in *Cannabis sativa* using *Arabidopsis thaliana* as reference species. 

## Repository structure

### `data/`
| File | Description |
|------|-------------|
| `tps_arath.fasta` | 33 *A. thaliana* TPS sequences (Swiss-Prot, reviewed) |
| `bona_fide.fasta` | 3 biochemically characterized anchor sequences (Swiss-Prot, PE=1) |
| `cannabis_tps_candidates.fasta` | 33 *C. sativa* TPS candidates filtered from BLASTP results (RefSeq) |

### `alignment/`
| File | Description |
|------|-------------|
| `tps_arath_bonafide_cannabis_raw.fasta` | Concatenated input for MAFFT (69 sequences) |
| `tps_arath_bona_cannabis_aligned.fasta` | Multiple sequence alignment (69 sequences, 1272 positions) |

### `results/`
| File | Description |
|------|-------------|
| `tree_tps_cannabis.nhx` | Maximum-likelihood phylogenetic tree in Newick format (PhyML 3.3) |
| `tree_tps_cannabis_itol.pdf` | Annotated tree visualization exported from iTOL v6 |
| `informe.pdf` | Full analysis report |

## Author
Laura Llamas — Máster en Bioinformática, Asignatura Análisis de Datos Ómicos, Universidad de Murcia, 2026
