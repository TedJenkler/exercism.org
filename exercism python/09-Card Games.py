"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    rounds = [number, number + 1, number + 2]
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    for round in rounds:
        if round == number:
            return True
    return False


def card_average(hand):
    length = len(hand)
    return sum(hand) / length


def approx_average_is_average(hand):
    real_average = sum(hand) / len(hand)
    test_1 = (hand[0] + hand[-1]) / 2
    test_2 = hand[len(hand) // 2]
    if test_1 == real_average or test_2 == real_average:
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    odd = []
    even = []
    index = "odd"
    for card in hand:
        if index == "odd":
            odd.append(card)
            index = "even"
        else:
            even.append(card)
            index = "odd"
    if (sum(odd) / len(odd)) == (sum(even) / len(even)):
        return True
    else:
        return False


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
        return hand
    else:
        return hand