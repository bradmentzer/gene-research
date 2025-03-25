from Bio import SeqIO

#Read FASTA file
def read_fasta(file_path):
    record = SeqIO.read(file_path, "fasta")
    return record.seq

#Find longest ORF
def find_longest_orf(seq):
    longest_orf = ""

    for frame in range(3):  # Three possible reading frames
        translated_seq = seq[frame:].translate(to_stop=True)  # Translate until stop codon
        if len(translated_seq) > len(longest_orf):
            longest_orf = translated_seq  # Update longest ORF

    return longest_orf


# Main execution
if __name__ == "__main__":
    fasta_file = "data/example.fasta"  
    dna_sequence = read_fasta(fasta_file)

    longest_orf = find_longest_orf(dna_sequence)

    print(f"Longest translated protein sequence: {longest_orf}")