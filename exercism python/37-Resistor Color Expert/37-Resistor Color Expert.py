map_of_colors = { "black": "0", "brown": "1", "red": "2", "orange": "3", "yellow": "4", "green": "5", "blue": "6", "violet": "7", "grey": "8", "white": "9" }

map_of_zeros = { "black": "", "brown": "0", "red": "00", "orange": "000", "yellow": "0000", "green": "00000", "blue": "000000", "violet": "0000000", "grey": "00000000", "white": "000000000" }

map_of_tolerance = { "grey": " ±0.05%", "violet": " ±0.1%", "blue": " ±0.25%", "green": " ±0.5%", "brown": " ±1%", "red": " ±2%", "gold": " ±5%", "silver": " ±10%" }

def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    
    if len(colors) == 4:
        value_sum = map_of_colors[colors[0]] + map_of_colors[colors[1]]
        zeros = map_of_zeros[colors[2]]
    elif len(colors) == 5:
        value_sum = map_of_colors[colors[0]] + map_of_colors[colors[1]] + map_of_colors[colors[2]]
        zeros = map_of_zeros[colors[3]]
    else:
        raise ValueError("Invalid number of color bands")
    
    total = int(value_sum + zeros)
    
    if total < 1000:
        resistance = f"{total} ohms"
    elif total < 1000000:
        resistance = f"{total / 1000:.2f}".rstrip('0').rstrip('.')
        resistance += " kiloohms"
    elif total < 1000000000:
        resistance = f"{total / 1000000:.2f}".rstrip('0').rstrip('.')
        resistance += " megaohms"
    else:
        resistance = f"{total / 1000000000:.2f}".rstrip('0').rstrip('.')
        resistance += " gigaohms"


    if len(colors) == 4:
        tolerance = map_of_tolerance.get(colors[3], "")
    elif len(colors) == 5:
        tolerance = map_of_tolerance.get(colors[4], "")
    else:
        tolerance = ""
    
    return resistance + tolerance