# K-mer Counter 
# 🧩 What are k-mers?
DNA is like a long string made of four letters (A, T, G, C).
A k-mer is just a small slice of DNA of length k.
For example, if your DNA sequence is:
ATGCGTAG
For k=2 (2-mers): AT, TG, GC, CG, GT, TA, AG
For k=3 (3-mers): ATG, TGC, GCG, CGT, GTA, TAG
👉 Counting k-mers tells us which small DNA "words" appear most often.
# 🔧 Requirements
Python 3.x (no external libraries needed)
# ▶️ Usage
This is a beginner project using only Python basics (loops + dictionaries).
The script has a DNA sequence already written inside:
Sequence = ATGCGTAG
k = 3
Run it with:
python kmer_counter.py
# 📊 Example Output
Sequence: ATGCGTAG
K = 3
K-mer counts:
ATG : 1
TGC : 1
GCG : 1
CGT : 1
GTA : 1
TAG : 1
# 🧑‍💻 Skills Demonstrated
Python loops and dictionaries
String slicing
Applying coding basics to a bioinformatics problem (k-mer counting)

