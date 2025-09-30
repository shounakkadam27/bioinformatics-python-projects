# kmer_counter.py
# Simple script to count k-mers in DNA sequences

def count_kmers(seq, k=3):
    """Count all k-mers of length k in a DNA sequence"""
    counts = {}
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        counts[kmer] = counts.get(kmer, 0) + 1
    return counts

# Example sequence (you can replace with FASTA later)
sequence = "ATGCGTAG".upper()
k = 3

kmer_counts = count_kmers(sequence, k)

print("Sequence:", sequence)
print("K =", k)
print("K-mer counts:")
for kmer, count in kmer_counts.items():
    print(kmer, ":", count)
