def triplets_with_sum(N):
    triplets = []

    for a in range(1, N // 3):
        for b in range(a + 1, N // 2):
            c = N - a - b
            if a < b < c and a * a + b * b == c * c:
                triplets.append([a, b, c])
    return triplets