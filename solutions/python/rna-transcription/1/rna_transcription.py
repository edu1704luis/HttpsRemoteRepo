def to_rna(dna_strand):
    rna_complement = {"G": "C", "C": "G", "T": "A", "A": "U"}
    rna = ""
    if len(dna_strand) >= 1:
        for nucleotides in dna_strand:
            if nucleotides in rna_complement:
                rna += rna_complement[nucleotides]
        return rna
    return ""
            
