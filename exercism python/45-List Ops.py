def append(list1, list2):
    if isinstance(list2, (int, float, str)):
        return list1 + [list2]
    return list1 + list2 

def concat(lists):
    result = []
    for item in lists:
        if isinstance(item, list):
            result.extend(item)
        else:
            append(result, item)
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result = append(result, item)
    return result


def length(list):
    count = 0
    for item in list:
        count += 1
    return count

def map(function, list):
    result = []
    for item in list:
        result = append(result, function(item))
    return result


def foldl(function, list, initial):
    if not list:
        return initial
    result = initial
    for item in list:
        result = function(result, item)
    return result


def foldr(function, list, initial):
    return foldl(function, reverse(list), initial)


def reverse(list):
    result = []
    for i in range(len(list) - 1, -1, -1):
        result = result + [list[i]]
    return result