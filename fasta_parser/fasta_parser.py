# SeqIO helps us read/write sequence files (FASTA, FASTQ, GenBank, etc.)
from Bio import SeqIO

def gc_content(seq):
    """Calculate GC Content percentage of a DNA Sequence"""
    g = seq.count("G")
    c = seq.count("C")
    return round ((g + c) / len(seq) * 100, 2) if len(seq) > 0 else 0

# Input FASTA file
# Seq.IO reads each sequence record in the file one by one
fasta_file = "sequence.fasta"

for record in SeqIO.parse(fasta_file, "fasta"):
    seq_id = record.id # Sequence Identifier (e.g., >seq1)
    seq_len = len(record.seq) # Sequence length in base pairs
    gc = gc_content(record.seq.upper()) # GC Content of the sequence in percentage

# print results for this sequence
    print(f"ID: {seq_id}")
    print(f"Length: {seq_len} bp")
    print(f"GC Content: {gc}%\n")





