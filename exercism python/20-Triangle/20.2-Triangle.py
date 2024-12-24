def is_tri(a, b, c):
    if a + b >= c and b + c >= a and a + c >= b and a > 0 and b > 0 and c > 0:
        return True
    else:
        return False

def equilateral(sides):
    a, b, c = sides
    if a == b and b == c and is_tri(a, b, c):
        return True
    else:
        return False


def isosceles(sides):
    a, b, c = sides
    if len(set(sides)) < 3 and is_tri(a, b, c):
        return True
    else:
        return False


def scalene(sides):
    a, b, c = sides
    if len(set(sides)) == 3 and is_tri(a, b, c):
        return True
    else:
        return False
