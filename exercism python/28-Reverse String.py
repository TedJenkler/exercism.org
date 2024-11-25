def reverse(text):
    if text == "":
        return ""
    arr = list(text)
    return "".join(arr[::-1])