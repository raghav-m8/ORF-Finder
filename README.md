# ORF Finder

A modular Python-based bioinformatics tool for identifying Open Reading Frames (ORFs) in DNA sequences. The program scans all six reading frames, translates detected ORFs into protein sequences, and generates output files for downstream analysis.

---

## Features

- FASTA file parsing
- Multiple sequence support
- Six reading frame ORF detection
- Reverse complement generation
- DNA to protein translation
- ORF FASTA export
- Protein FASTA export
- Analysis report generation

---

## Requirements

- Python 3.11 or later
- Biopython

Install the required dependency:

```bash
pip install biopython
```

---

## Usage

Run the program:

```bash
python src/main.py
```

Provide the input FASTA file when prompted. The program scans all six reading frames, identifies Open Reading Frames, translates them into proteins, and automatically generates the output files.

---

## Output

The program generates the following files:

- **orf_output.fasta** – Detected ORFs
- **protein_output.fasta** – Translated protein sequences
- **Analysis Report.txt** – Analysis summary and statistics

---

## Current Capabilities

- Parses FASTA files containing one or more DNA sequences.
- Identifies ORFs across all six reading frames.
- Generates reverse complement sequences.
- Translates nucleotide sequences into proteins using the standard genetic code.
- Exports ORF and protein sequences in FASTA format.
- Produces an analysis report summarizing the results.

---

## License

This project is licensed under the MIT License.

---

## Author

Raghav Menon

Developed as a bioinformatics project to strengthen Python programming, software engineering practices, and computational biology skills.