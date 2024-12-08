single = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
double = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    
    if number == 0:
        return "zero"
    
    def under_hundred(n):
        if n < 10:
            return single[n]
        elif n < 20:
            return double[n]
        else:
            tens = n // 10 * 10  # Tens place value
            ones = n % 10        # Ones place value
            return double[tens] + ("-" + single[ones] if ones > 0 else "")
    
    def recursive_say(n):
        if n < 100:
            return under_hundred(n)
        elif n < 1_000:
            hundreds = n // 100
            rest = n % 100
            return single[hundreds] + " hundred" + (" " + recursive_say(rest) if rest > 0 else "")
        elif n < 1_000_000:
            thousands = n // 1_000
            rest = n % 1_000
            return recursive_say(thousands) + " thousand" + (" " + recursive_say(rest) if rest > 0 else "")
        elif n < 1_000_000_000:
            millions = n // 1_000_000
            rest = n % 1_000_000
            return recursive_say(millions) + " million" + (" " + recursive_say(rest) if rest > 0 else "")
        else:
            billions = n // 1_000_000_000
            rest = n % 1_000_000_000
            return recursive_say(billions) + " billion" + (" " + recursive_say(rest) if rest > 0 else "")
    
    return recursive_say(number)