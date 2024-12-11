def proverb(*args, **kwargs):
    arr = list(args)
    result = []
    if len(arr) == 0:
        return []
    for i in range(len(arr) - 1):
        result.append(f"For want of a {arr[i]} the {arr[i + 1]} was lost.")
        
    if kwargs['qualifier'] != None:
        result.append(f"And all for the want of a {kwargs['qualifier']} {arr[0]}.")
    else:
        result.append(f"And all for the want of a {arr[0]}.")
    return result