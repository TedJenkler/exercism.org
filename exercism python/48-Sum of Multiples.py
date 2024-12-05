def sum_of_multiples(level, base):
    if base == []:
        return 0
    xp = []
    total = 0
    
    for num in base:
        if num == 0:
            continue
        for i in range(num, level, num):
            xp.append(i)
    points = set(xp)
    for point in points:
        total += point
    return total