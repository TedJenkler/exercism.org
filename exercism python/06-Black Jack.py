"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    if card in ['K', 'Q', 'J']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)

def higher_card(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one_value > card_two_value:
        return card_one
    elif card_one_value < card_two_value:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    if card_one == 'A' or card_two == 'A':
        return 1
    elif value_of_card(card_one) + value_of_card(card_two) <= 10:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    if (card_one in ['10', 'K', 'Q', 'J'] and card_two == 'A') or (card_two in ['10', 'K', 'Q', 'J'] and card_one == 'A'):
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    if total in [9, 10, 11]:
        return True
    else:
        return False