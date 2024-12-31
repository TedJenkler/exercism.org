def is_armstrong_number(number):
    num = list(str(number))
    length = len(num)
    total = 0
    for value in num:
        total += int(value) ** length

    return total == number