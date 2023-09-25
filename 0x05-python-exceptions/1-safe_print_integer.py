#!/usr/bin/python3

def safe_print_integer(value):
    """
    safe_print_integer - Prints an integer (value)
                        if value is a string, it returns false
    -------------------
    Parameter:

    value: The integer to be printed
    -------------------

    Return: True if an integer was printed, else False
    """
    try:
        print("{:d}".format(value))
    except TypeError:
        return False
    return True
