

YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def score(dices, category):
    pairs = {}
    for dice in dices:
        if dice in pairs:
            pairs[dice] += 1
        else:
            pairs[dice] = 1
    print(pairs)
    if category == "YACHT" and len(pairs) == 1:
        return 50
    if category == "ONES" and 1 in pairs:
        return pairs[1] * 1
    if category == "TWOS" and 2 in pairs:
        return pairs[2] * 2
    if category == "THREES" and 3 in pairs:
        return pairs[3] * 3
    if category == "FOURS" and 4 in pairs:
        return pairs[4] * 4
    if category == "FIVES" and 5 in pairs:
        return pairs[5] * 5
    if category == "SIXES" and 6 in pairs:
        return pairs[6] * 6
    if category == "FULL_HOUSE" and len(pairs) == 2:
        values = list(pairs.values())
        if sorted(values) == [2, 3]:
            return sum(dices)
    if category == "FOUR_OF_A_KIND":
        for die_value, count in pairs.items():
            if count >= 4:
                return die_value * 4
    if category == "LITTLE_STRAIGHT" and sorted(dices) == [1,2,3,4,5]:
        return 30
    if category == "BIG_STRAIGHT" and sorted(dices) == [2,3,4,5,6]:
        return 30
    if category == "CHOICE":
        return sum(dices)
    return 0