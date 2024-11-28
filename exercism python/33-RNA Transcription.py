def to_rna(dna_strand):
    print(dna_strand)
    arr = list(dna_strand)
    total = []
    for strand in arr:
        if strand == "G":
            total.append("C")
        elif strand == "C":
            total.append("G")
        elif strand == "T":
            total.append("A")
        elif strand == "A":
            total.append("U")
        else:
            raise TypeError('Not valid strain')
    return ''.join(total)