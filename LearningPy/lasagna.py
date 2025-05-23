"""Functions used in preparing Guido's gorgeous lasagna.
Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_LAYER = 2

def bake_time_remaining(remaining_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    bake_time_remaining = EXPECTED_BAKE_TIME - remaining_time
    return bake_time_remaining

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.""" 
    preparation_time_in_minutes = number_of_layers * PREPARATION_TIME_LAYER
    return preparation_time_in_minutes

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Return the elapsed cooking time. 
    This function takes two integers representing the number of lasagna layers and the time already spent baking and calculates the total elapsed minutes spent cooking the lasagna. 
    """
    elapsed_time_in_minutes = (number_of_layers*PREPARATION_TIME_LAYER) + elapsed_bake_time
    return elapsed_time_in_minutes
