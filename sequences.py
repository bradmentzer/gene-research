import Bio

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

# Read the sequences from the FASTA file
def read_fasta(file_path):
    record = SeqIO.read(file_path, "fasta")
    return record.seq # Return the sequence

# Calculate the GC content of the sequence
def calculate_gc(seq):
    return gc_fraction(seq) *100# Return the GC content

if __name__ == "__main__":
    file_path = "data/example.fasta"
    sequence = read_fasta(file_path)
    gc_content = calculate_gc(sequence)
    print(f"GC Content: {gc_content:.2f}%") # Print the GC content