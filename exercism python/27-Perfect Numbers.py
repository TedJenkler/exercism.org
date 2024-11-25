def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"

    factors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i and i != 1:
                factors.append(number // i)
    
    proper_sum = sum(factors)

    if proper_sum == number:
        return 'perfect'
    elif proper_sum > number:
        return 'abundant'
    else:
        return 'deficient'