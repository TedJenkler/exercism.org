def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for digit in digits:
        if digit < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        if digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    
    base_10 = 0
    for i, digit in enumerate(reversed(digits)):
        base_10 += digit * (input_base ** i)

    if base_10 == 0:
        return [0]
    
    result = []
    while base_10 > 0:
        remainder = base_10 % output_base
        result.append(remainder)
        base_10 //= output_base
    
    result.reverse()
    return result