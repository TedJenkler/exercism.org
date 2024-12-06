SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def is_contiguous_sublist(smaller, larger):
    if not smaller:
        return True
    for i in range(len(larger) - len(smaller) + 1):
        if larger[i:i + len(smaller)] == smaller:
            return True
    return False


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif is_contiguous_sublist(list_one, list_two):
        return SUBLIST
    elif is_contiguous_sublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL