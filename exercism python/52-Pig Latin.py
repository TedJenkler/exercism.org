vowels = ["a", "e", "i", "o", "u"]

ay = ["xr", "yt"]

def rule_1(letters):
    print(letters[:2])
    return "".join(letters) + "ay"

def rule_2(letters):
    move = []
    result = []
    no_vowel_yet = True
    for letter in letters:
        if letter not in vowels and no_vowel_yet == True:
            move.append(letter)
        else:
            result.append(letter)
            no_vowel_yet = False
    result = result + move
    result.append("ay")
    return "".join(result)

def rule_3(letters):
    move = []
    result = []
    no_vowel_yet = True
    i = 0

    while i < len(letters):
        if (i < len(letters) - 1 and letters[i] == "q" and letters[i + 1] == "u" and no_vowel_yet):
            move.append("qu")
            i += 2 
        elif no_vowel_yet and letters[i] not in vowels:
            move.append(letters[i])
            i += 1
        else:
            no_vowel_yet = False
            result.append(letters[i])
            i += 1

    result.extend(move)
    return "".join(result) + "ay"

def rule_4(letters):
    move = []
    result = []
    no_vowel_yet = True

    for i, letter in enumerate(letters):
        if no_vowel_yet and letter not in vowels:
            if letter == "y":
                no_vowel_yet = False
                result.append(letter)
            else:
                move.append(letter)
        else:
            no_vowel_yet = False
            result.append(letter)

    result.extend(move)
    return "".join(result) + "ay"

def translate(text):
    vowels = ["a", "e", "i", "o", "u"]
    ay = ["xr", "yt"]

    def process_word(word):
        letters = list(word)
        if letters[0] in vowels or "".join(letters[:2]) in ay:
            return rule_1(letters)
        elif "y" in word and letters[0] not in vowels and letters[0] != "y":
            return rule_4(letters)
        elif "qu" in word:
            return rule_3(letters)
        elif letters[0] not in vowels:
            return rule_2(letters)

    words = text.split()
    translated_words = [process_word(word) for word in words]
    return " ".join(translated_words)
    
    return result