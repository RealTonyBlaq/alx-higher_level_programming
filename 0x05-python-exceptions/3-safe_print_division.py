#!/usr/bin/python3

def safe_print_division(a, b):
    """
    safe_print_division - Safely prints the result of a division
    --------------------
    Parameters:

    a: The numerator
    b: The denominator
    --------------------

    Return: The result of the division
    """
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
    return result
