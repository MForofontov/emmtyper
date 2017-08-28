# EmMAIL - Emm Automatic Isolate Labeller

## Table of Content
1. [Introduction](##Introduction)
2. [Requirements](##Requirements)
3. [Installation](##Installation)
4. [Usage](##Usage)
5. [Result Format](##Result_Format)
6. [Contact](##Contact)

## Introduction

EmMAIL is a command line tool for emm-type classification of Streptococcus pyogenes based on the isolate's whole genome sequence.

Input	: Assembled WGS reads of Streptococcus pyogenes

Output	: BLAST output format 6 with predicted emm type of the isolate

The use of EmMAIL will follow the dependencies of the tools within its pipeline, namely BLAST and isPcr.

## Requirements

EmMAIL needs BLAST and isPcr. As is, there is no way to automatically install both within the setup.py.

User (for now) will need to manually install the tools themselves and set them on $PATH for EmMAIL to work.

## Installation

EmMAIL uses setup.py for easier installation. Clone the GitHub page for EmMAIL, and run setup.py over the command line on the directory where setup.py for EmMAIL is located.
The command is:

```sh
$ python3 setup.py install
``` 

You will then be able to use EmMAIL by calling `emmail` on the command line.

## Usage

EmMAIL has 2 branches of usage: direct BLAST, or isPcr followed with BLAST. Product of any of the two pipelines (in the form of BLAST output 6 with SubjectLength) will then go through EmMAIL's Clusterer to derive the type of the isolate.

The arguments used in the pipeline are derived from the mentioned tools.

### isPcr Path
We first extract targeted sequences using in silico PCR, and then BLAST the amplicons.
The required arguments are:

| Argument | Variable Type | Description |
| ------ | ------ | ------ |
| --primer | tsv | A tsv file containing primer set in the format "{PrimerSetName}\t{Primer1Sequence}\t{Primer2Sequence}" |
| --query | FASTA | An assembled genome FASTA. Alignment will be checked within contigs; the longer the contigs, the better chance we have to find possible existing alignments |
| --db | blast DB | A BLAST database file |

Arguments for isPcr:

| Argument | Variable Type | Default | Description |
| ------ | ------ | ------ | ------ |
| -minPerfect | integer | 15 | Minimum size of perfect match at 3' primer end |
| -minGood | integer | 15 | Minimum size where there must be 2 matches for each mismatch | 
| -maxSize | integer | 4000 | Positive integer value for maximum product length |
| -savePCR | boolean | False | On mention, PCR output file will not be automatically removed | 

Post-PCR, the arguments are the same as the ones in the BLAST path.

### BLAST Path
We directly use BLAST (specifically, blastn) against the assembled genome FASTA.
The required arguments are:

| Argument | Variable Type | Description |
| ------ | ------ | ------ |
| --query | FASTA | An assembled genome FASTA |
| --db | blast DB | A BLAST database file |

Arguments for BLAST:

| Argument | Variable Type | Default | Description |
| ------ | ------ | ------ | ------ |
| -dust | string | no | Filter query sequence with DUST |
| -perc_identity | integer | 95 | Minimal percent identity of sequence |
| -culling_limit | integer | 1 | Total hits to return in a single position |

Arguments for BLAST filter:

| Argument | Variable Type | Default | Description |
| ------ | ------ | ------ | ------ |
| -mismatch | integer | 4 | Threshold number of mismatch to allow in BLAST hit |
| -align_diff | integer | 5 | Threshold for difference between alignment length and subject length in BLAST hit |
| -gap | integer | 2 | Threshold number of gap to allow in BLAST hit |

### Clusterer Arguments

| Argument | Variable Type | Default | Description |
| ------ | ------ | ------ | ------ |
| -verbose | boolean | False | On mention, return a more verbose result |
| -outFinal | tsv | stdout | File to stream final output. Default to terminal |

An example command for direct BLAST is shown below:
```sh
$ emmail blast --query <isolate FASTA> --db <BLAST DB filepath> -outFinal <filename>.tsv
```

## Result Format
EmMAIL by default produces three tab-separated values to the command line. Calling `-verbose` will make EmMAIL return eight tab-separated values.

The short result returns: **<Isolate name> <Predicted type> <Possible imposters>**

While the verbose result returns: **<Isolate name> <Number of BLAST hits> <Clusterer decision flag> <Predicted type> <Type score> <Position in assembly> <Number of clusters> <Possible imposters>**


## Contact 

Should you want to fill issues or contact me about anything regarding EmMAIL, 
you can reach me here or on my email: andre.sutanto.91@gmail.com.