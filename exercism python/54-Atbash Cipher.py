ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ALPHABET_REV = list(reversed(ALPHABET))

def encode(plain_text):
    lower_text = plain_text.lower()
    arr = list(lower_text)
    result = []
    count = 0
    for letter in arr:
        if letter in ALPHABET:
            index = ALPHABET.index(letter)
            result.append(ALPHABET_REV[index])
            count += 1
            if count == 5:
                count = 0
                result.append(" ")
        elif letter not in " ,." and letter != " ":
            result.append(letter)
            count += 1
            if count == 5:
                count = 0
                result.append(" ")

    if result and result[-1] == " ":
        result.pop()
    
    return "".join(result)


def decode(ciphered_text):
    lower_text = ciphered_text.lower()
    arr = list(lower_text)
    result = []
    count = 0
    for letter in arr:
        if letter in ALPHABET:
            index = ALPHABET.index(letter)
            result.append(ALPHABET_REV[index])
        elif letter not in " ,." and letter != " ":
            result.append(letter)
    if result and result[-1] == " ":
        result.pop()
    
    return "".join(result)