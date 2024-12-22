def is_paired(input_string):
    stack = []
    
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    
    
    for char in input_string:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs.keys():
            if stack and stack[-1] == bracket_pairs[char]:
                stack.pop()
            else: 
                return False
    return len(stack) == 0