def equilateral(sides):
    a, b, c = sides
    if a + b + c == 0:
        return False
    if a == b and b == c:
        return True
    else:
        return False


def isosceles(sides):
    a, b, c = sides
    if a + b >= c and b + c >= a and a + c >= b:
        return a == b or b == c or a == c
    else:
        return False


def scalene(sides):
    a, b, c = sides
    if a + b >= c and b + c >= a and a + c >= b:
        return a != b and b != c and a != c
    else:
        return False