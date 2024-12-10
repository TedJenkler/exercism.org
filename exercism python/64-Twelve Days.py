DAYS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]


ITEMS = ["a Partridge in a Pear Tree.", "two Turtle Doves", "three French Hens", "four Calling Birds", "five Gold Rings", "six Geese-a-Laying", "seven Swans-a-Swimming", "eight Maids-a-Milking", "nine Ladies Dancing", "ten Lords-a-Leaping", "eleven Pipers Piping", "twelve Drummers Drumming"]

def recite(start_verse, end_verse):
    result = []
    for i in range(start_verse - 1, end_verse):
        if i > 0:
            ITEMS[0] = "and a Partridge in a Pear Tree."
        result.append(f"On the {DAYS[i]} day of Christmas my true love gave to me: {', '.join(reversed(ITEMS[0:i + 1]))}")
    return result