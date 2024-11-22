def response(hey_bob):
    if hey_bob == "":
        return "Fine. Be that way!"
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    arr = list(hey_bob)
    if hey_bob.upper() == hey_bob and arr[-1] == "?" and any(char.isalpha() for char in hey_bob):
        return "Calm down, I know what I'm doing!"
    elif hey_bob.upper() == hey_bob and any(char.isalpha() for char in hey_bob):
        return "Whoa, chill out!"
    elif  hey_bob.strip()[-1] == "?":
        return "Sure."
    else:
        return "Whatever."