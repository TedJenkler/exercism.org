def abbreviate(words):
    arr = list(words)
    result = []
    for i, letter in enumerate(words):
        if i == 0:
            result.append(words[i])
        if (letter == " " or letter == "-" or letter == "_") and words[i + 1] != " " and words[i + 1] != "-" and words[i + 1] != "_":
            result.append(words[i + 1])
    return "".join(result).upper()