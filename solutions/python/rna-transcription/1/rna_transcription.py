def to_rna(dna_strand):
    if dna_strand == "":
        return dna_strand
    
    complements = {"G": "C", "C": "G", "T": "A", "A": "U"}
    char_array = [complements.get(char) for char in dna_strand]
    
    return ''.join(char_array)
