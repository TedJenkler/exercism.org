import math

def prime(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")
    primes = []
    start = 2
    while len(primes) < number:
        is_prime = True 
        for i in range(2, int(math.sqrt(start)) + 1):
            if start % i == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(start)
        
        start += 1

    return primes[number - 1]