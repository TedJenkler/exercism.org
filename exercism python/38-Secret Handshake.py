list_of_actions = ['reverse', 'jump', 'close your eyes', 'double blink', 'wink']

def commands(binary_str):
    arr = list(binary_str)
    action = []
    for i, item in enumerate(arr):
        if item == "1" and i != 0:
            action.append(list_of_actions[i])
    if arr[0] == "1":
        return action
    action.reverse()
    return action