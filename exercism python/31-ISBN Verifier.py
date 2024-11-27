def is_valid(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    d = []
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        d.append(int(isbn[i]))

    if isbn[-1] == "X":
        d.append(10)
    elif isbn[-1].isdigit():
        d.append(int(isbn[-1]))
    else:
        return False
    
    checksum = sum(d[i] * (10 - i) for i in range(10))
    
    if checksum % 11 == 0:
        return True
    else:
        return False