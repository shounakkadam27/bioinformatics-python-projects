from Bio import SeqIO
import matplotlib.pyplot as plt

# === Step 1: Load the FASTA file ===
fasta_path = "sequence.fasta"

# Parse all record and print their IDs
records = list(SeqIO.parse(fasta_path, "fasta"))

print(f"Number of sequences in file: {len(records)}")
for i, rec in enumerate(records):
    print(f"[{i}] ID: {rec.id}, length: {len(rec.seq)}")

# Choose the first one for now
sequence = records[0].seq.upper()

# Print the first 100 bases
print("\nFirst 100 bases of selected sequence:")
print(sequence[:100])

# === Step 2: Calculate GC content ===
window_size = 100
gc_values = []
positions = []

for i in range(0, len(sequence) - window_size + 1, window_size):
    window = sequence[i:i+window_size]
    gc_count = window.count("G") + window.count("C")
    gc_percent = (gc_count / window_size) * 100
    gc_values.append(gc_percent)
    positions.append(i + window_size // 2)

# === Step 3: Plot ===
plt.figure(figsize=(10, 5))
plt.plot(positions, gc_values, color='green')
plt.title("GC content of Genomic Region Containing CHI3L1 (100 bp window)")
plt.xlabel("Position (bp)")
plt.ylabel("GC Content (%)")
plt.grid(True)
plt.tight_layout()
plt.savefig("gc_content_CHI3L1.png")
plt.show()