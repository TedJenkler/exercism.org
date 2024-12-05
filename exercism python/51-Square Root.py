def square_root(number):
    for i in range(1, number):
        if i * i == number:
            return i
    return 1