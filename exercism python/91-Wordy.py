import re

operations = ["plus", "minus", "multiplied", "divided"]

restricted = ["cubed", "Who"]

def is_number(v):
    try:
        float(v)
        return True
    except ValueError:
        return False

def answer(question):
    total = 0
    
    punctuation_regex = r"[!\"#$%&'()*+,\./:;<=>?@[\\\]^_`{|}~]"
    cleaned = "".join([letter for letter in question if not re.fullmatch(punctuation_regex, letter)])
    
    current = "plus"
    check = []
    syntax = False
    for item in cleaned.split(" "):
        if is_number(item) or item in operations:
            check.append(item)
    for i in range(0, len(check)):
        if i % 2 == 0:
            if is_number(check[i]) == False:
                raise ValueError("syntax error")
        if i % 2 != 0:
            if is_number(check[i]):
                raise ValueError("syntax error")
        if check[-1] in operations:
            raise ValueError("syntax error")
    
    for item in cleaned.split(" "):
        if item in restricted:
            raise ValueError("unknown operation")
        if item in operations:
                current = item
        if is_number(item):
            if current == "plus":
                total += float(item)
            if current == "minus":
                total -= float(item)
            if current == "multiplied":
                total *= float(item)
            if current == "divided":
                total /= float(item)
    if len(check) == 0:
            raise ValueError("syntax error")
    return total