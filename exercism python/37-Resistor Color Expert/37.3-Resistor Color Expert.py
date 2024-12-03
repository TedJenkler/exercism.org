COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

TOLERANCE = { "grey": " ±0.05%", "violet": " ±0.1%", "blue": " ±0.25%", "green": " ±0.5%", "brown": " ±1%", "red": " ±2%", "gold": " ±5%", "silver": " ±10%" }

def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"

    *rest, m, t = colors
    
    total = 0
    multi = 1
    for color in reversed(rest):
        total += COLORS.index(color) * multi
        multi *= 10

    value = total * (10 ** COLORS.index(m))

    units = [(1000, 'ohms'), (1000000, 'kiloohms'), (1000000000, 'megaohms'), (1000000000000, 'gigaohms')]

    for threshold, unit in units:
        if value < threshold:
            result = value / (threshold / 1000)
            formatted_result = (
                str(int(result)) 
                if result.is_integer() 
                else "{:.1f}".format(result) 
                if result * 10 % 1 == 0 
                else "{:.2f}".format(result)
            )
            return "{} {}{}".format(formatted_result, unit, TOLERANCE[t])