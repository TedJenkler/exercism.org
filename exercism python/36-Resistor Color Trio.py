map_of_colors = { "black": "0", "brown": "1", "red": "2", "orange": "3", "yellow": "4", "green": "5", "blue": "6", "violet": "7", "grey": "8", "white": "9", }
map_of_zeros = { "black": "", "brown": "0", "red": "00", "orange": "000", "yellow": "0000", "green": "00000", "blue": "000000", "violet": "0000000", "grey": "00000000", "white": "000000000" }

def label(colors):
    total = ""
    zeros = map_of_zeros[colors[2]]
    for color in colors[:2]:
        total += map_of_colors[color]
    value = int(total + zeros)
    
    if value < 1000:
        return str(value) + " ohms"
    elif value >= 1000 and value < 10000000:
        return str(value // 1000) + " kiloohms"
    elif value >= 10000000 and value < 10000000000:
        return str(value // 1000000) + " megaohms"
    elif value > 10000000000:
        return str(value // 1000000000) + " gigaohms"