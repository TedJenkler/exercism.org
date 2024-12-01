COLORS = { "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9 }
TOLERANCE = { "grey": " ±0.05%", "violet": " ±0.1%", "blue": " ±0.25%", "green": " ±0.5%", "brown": " ±1%", "red": " ±2%", "gold": " ±5%", "silver": " ±10%" }
def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    if len(colors) != 4 and len(colors) != 5:
        raise ValueError("Invalid number of color bands")
    if len(colors) == 4:
        c1, c2, m, t = colors
        exponent = COLORS[m]
        tolerance = TOLERANCE[t]
        terms = [c1, c2]
    else:
        c1, c2, c3, m, t = colors
        exponent = COLORS[m]
        tolerance = TOLERANCE[t]
        terms = [c1, c2, c3]
    sum = 0
    terms.reverse()
    for i, term in enumerate(terms):
        multi = 10 ** i
        sum += COLORS[term] * multi
    total = sum * (10 ** exponent)
    print(total)
    if total < 1000:
        return f"{total} ohms{tolerance}"
    elif total < 1000000:
        return f"{total / 1000}".rstrip("0").rstrip(".") + f" kiloohms{tolerance}"
    elif total < 1000000000:
        return f"{total / 1000000}".rstrip("0").rstrip(".") + f" megaohms{tolerance}"
    elif total < 1000000000000:
        return f"{total / 1000000000}".rstrip("0").rstrip(".") + f" gigaohms{tolerance}"