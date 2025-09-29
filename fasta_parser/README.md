# FASTA Parser

This project is a simple bioinformatics tool written in Python that:
- Parses a FASTA file
- Reports each sequence ID
- Calculates sequence length (bp)
- Calculates GC content (%)

It demonstrates how to work with biological sequence data using **Biopython**.

---

## 🔧 Requirements
- Python 3.x
- Biopython library

Install Biopython with:
```bash
pip install biopython

# Usage
python fasta_parser.py example.fasta

# Example input
>seq1
ATGCGTAGCTAGC
>seq2
GGGCCCATTAA

# Example output
ID: seq1
Length: 13 bp
GC Content: 53.85%

ID: seq2
Length: 11 bp
GC Content: 54.55%

Skills Demonstrated
- Python functions and string handling
- File parsing with Biopython (SeqIO)
- Basic bioinformatics concepts (GC content)





