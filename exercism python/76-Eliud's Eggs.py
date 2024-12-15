def egg_count(display_value):
    binary = bin(display_value)
    count = 0
    for num in binary[1:]:
        if num == "1":
            count += 1
    return count