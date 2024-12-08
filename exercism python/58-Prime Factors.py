def factors(value):
    prime = []
    divider = 2
    while value > 1:
        if value % divider == 0:
            prime.append(divider)
            value /= divider
        else:
            divider += 1
    return prime