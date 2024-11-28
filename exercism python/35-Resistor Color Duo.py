color_map = { "black": "0",  "brown": "1", "red": "2", "orange": "3", "yellow": "4", "green": "5", "blue": "6", "violet": "7", "grey": "8", "white": "9"}

def value(colors):
    total = ""
    for color in colors[:2]:
        total += color_map[color]
    return int(total)