PROTEIN = ["Methionine", "Phenylalanine", "Leucine", "Serine", "Tyrosine", "Cysteine", "Tryptophan"]


CODON = { "AUG": 0, "UUU": 1, "UUC": 1, "UUA": 2, "UUG": 2, "UCU": 3, "UCC": 3, "UCA": 3, "UCG": 3, "UAU": 4, "UAC": 4, "UGU": 5, "UGC": 5, "UGG": 6}

def proteins(strand):
    result = []
    arr = list(strand)
    pairs = []
    pair = ""
    for letter in arr:
        pair += letter
        if len(pair) == 3:
            pairs.append(pair)
            pair = ""
    for codon in pairs:
        if codon == "UAA" or codon == "UAG" or codon == "UGA":
            return result 
        else:
            result.append(PROTEIN[CODON[codon]])
    return result        