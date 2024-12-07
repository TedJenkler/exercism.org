import string

ALPHABET = "".join(string.ascii_lowercase)

ALPHABET_REVERSED = "".join(reversed(ALPHABET))

ENCODE = str.maketrans(ALPHABET, ALPHABET_REVERSED)
DECODE = str.maketrans(ALPHABET_REVERSED, ALPHABET)



def encode(plain_text):
    arr = list(plain_text.lower().translate(ENCODE))
    count = 0
    result = []
    for letter in arr:
        if count == 5:
            result.append(" ")
            count = 0
        if letter == "." or letter == "," or letter == " ":
            continue
        else:
            count += 1
            result.append(letter)
    return "".join(result).strip()
    


def decode(ciphered_text):
    arr = list(ciphered_text.lower().translate(DECODE))
    result = []
    for letter in arr:
        if letter == "." or letter == "," or letter == " ":
            continue
        else:
            result.append(letter)
    return "".join(result)