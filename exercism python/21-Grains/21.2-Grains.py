def square(n):
    if n < 1 or n > 64:
        raise ValueError("square must be between 1 and 64")
    total = 0
    multi = 1
    for i in range(0, n):
        total = multi
        multi += multi
    return total


def total():
    result = 0
    for i in range(1, 65):
        result += square(i)
    return result