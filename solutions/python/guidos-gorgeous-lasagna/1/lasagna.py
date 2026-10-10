"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time in minutes.

    This function takes the actual minutes the lasagna has been
    in the oven and returns how many minutes it still needs to bake.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.

    Returns:
        int: The preparation time in minutes.

    This function takes the number of layers in the lasagna and
    calculates the total preparation time.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.

    Returns:
        int: The total time elapsed in minutes preparing and baking.

    This function takes two integers representing the number of lasagna
    layers and the time already spent baking the lasagna. It calculates
    the total elapsed minutes spent cooking (preparing + baking).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time