"""
Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40

# Define the 'PREPARATION_TIME' constant below.
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    This function takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time for the lasagna.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (in minutes), where each layer takes 2 minutes.

    This function calculates the preparation time based on the number of layers,
    assuming each layer takes a fixed amount of time defined by `PREPARATION_TIME`.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time spent on preparing and baking the lasagna.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes) including both preparation and baking.

    This function sums up the preparation time (based on layers) and the elapsed
    baking time to provide the total time spent on the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time