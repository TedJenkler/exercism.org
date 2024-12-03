def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    count = 0
    for i, strand in enumerate(strand_a):
        if strand != strand_b[i]:
            count += 1
    return count