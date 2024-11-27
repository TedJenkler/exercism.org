import re

pattern = r"^[a-zA-Z]+$"

def is_pangram(sentence):
    unique_list = set(sentence.upper())
    only_letters = [s for s in unique_list if re.match(pattern, s)]
    if len(only_letters) == 26:
        return True
    else:
        return False