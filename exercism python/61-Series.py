def slices(series, length):
    if series == "":
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    arr = list(series)
    result = []
    for i in range(len(arr) - length + 1):
        result.append("".join(arr[i:i + length]))
    return result