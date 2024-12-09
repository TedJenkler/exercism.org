def decode(string):
    if not string:
        return ""
    
    result = []
    count = 0

    i = 0
    while i < len(string):
        if string[i].isdigit():
            count = count * 10 + int(string[i])
        else:
            result.append(string[i] * (count if count > 0 else 1))
            count = 0 
        i += 1

    return "".join(result)

def encode(string):
    if not string:
        return ""

    result = []
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            result.append(f"{count if count > 1 else ''}{string[i - 1]}")
            count = 1

    result.append(f"{count if count > 1 else ''}{string[-1]}")

    return "".join(result)