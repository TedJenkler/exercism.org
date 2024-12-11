VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


ROMAN = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I", 900: "CM", 400: "CD", 90: "XC", 40: "XL", 9: "IX", 4: "IV"}

x = sorted(ROMAN.keys(), reverse=True)

def roman(number):
    if number < 1 or number > 3999:
        raise ValueError("Number out of range (1-3999)")
    iteration = 0
    result = []
    while number > 0:
        if number >= x[iteration]:
            number -= x[iteration]
            result.append(ROMAN[x[iteration]])
        else:
            iteration += 1
    return "".join(result)