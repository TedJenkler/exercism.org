import string
def rows(letter):
    alphabet = string.ascii_uppercase
    n = alphabet.index(letter)
    result = []
    for i in range(n + 1):
        spaces = ' ' * (n - i)
        if i == 0:
            result.append(spaces + alphabet[i] + spaces)
        else:
            result.append(spaces + alphabet[i] + ' ' * (2 * i - 1) + alphabet[i] + spaces)
    for i in range(n - 1, -1, -1):
        result.append(result[i])
    return result