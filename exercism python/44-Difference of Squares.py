def square_of_sum(number):
    total = 0
    for i in range(1, number + 1):
        total += i
    return total * total


def sum_of_squares(number):
    total = 0
    for i in range(1, number + 1):
        total += i ** 2
    return total


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)