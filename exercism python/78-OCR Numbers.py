PATTERNS = {
    "0": [" _ ", "| |", "|_|", "   "],
    "1": ["   ", "  |", "  |", "   "],
    "2": [" _ ", " _|", "|_ ", "   "],
    "3": [" _ ", " _|", " _|", "   "],
    "4": ["   ", "|_|", "  |", "   "],
    "5": [" _ ", "|_ ", " _|", "   "],
    "6": [" _ ", "|_ ", "|_|", "   "],
    "7": [" _ ", "  |", "  |", "   "],
    "8": [" _ ", "|_|", "|_|", "   "],
    "9": [" _ ", "|_|", " _|", "   "],
}

def find_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    results = []
    for i in range(0, len(input_grid), 4):
        segment = input_grid[i:i+4]
        num_columns = len(segment[0])
        num_digits = num_columns // 3
        result = ""
        for j in range(num_digits):
            digit_pattern = [row[j * 3 : (j + 1) * 3] for row in segment]
            digit = find_key_by_value(PATTERNS, digit_pattern)
            result += digit if digit is not None else "?"
        results.append(result)
    return ",".join(results)