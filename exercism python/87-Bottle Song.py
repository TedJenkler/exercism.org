NUMBERS = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

X = "NUM green BOTTLE hanging on the wall,"

Z = "And if one green bottle should accidentally fall,"

Y = "There'll be NUM green BOTTLE hanging on the wall."

def recite(start, take=1):
    result = []
    print(start, take)
    for i in range(0, take):
        result.append(X.replace("NUM", NUMBERS[start].capitalize()).replace("BOTTLE", "bottles" if start > 1 else "bottle"))
        result.append(X.replace("NUM", NUMBERS[start].capitalize()).replace("BOTTLE", "bottles" if start > 1 else "bottle"))
        result.append(Z)
        result.append(
            Y.replace("NUM", NUMBERS[start - 1])
            .replace("BOTTLE", "bottles" if start - 1 > 1 else "bottles" if start - 1 == 0 else "bottle")
        )
        result.append("")
        start -= 1
    return result if result[-1] != "" else result[:-1]