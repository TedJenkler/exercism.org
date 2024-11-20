def is_armstrong_number(number):
    num_arr = [int(digit) for digit in str(number)]
    length = len(num_arr)
    total = 0

    for num in num_arr:
        total += num ** length
    if total == number:
        return True
    else:
        return False