import re

pattern = r"^[a-zA-Z]+$"

def is_isogram(string):
    upper_string = string.upper()
    filtered_letters = [s for s in upper_string if re.match(pattern, s)]
    set_letters = set(filtered_letters)
    if len(filtered_letters) == len(set_letters):
        return True
    else:
        return False