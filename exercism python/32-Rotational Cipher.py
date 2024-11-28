def rotate(text, key):
    arr = list(text)
    new_arr = []
    for letter in arr:
        if letter.isalpha():
            position = (ord(letter.upper()) - ord('A') + key) % 26
            new_letter = chr(position + ord('A'))
            if letter.islower():
                new_letter = new_letter.lower()
            new_arr.append(new_letter)
        else:
            new_arr.append(letter)
    return ''.join(new_arr)