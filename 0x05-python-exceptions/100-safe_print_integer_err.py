#!/usr/bin/python3

def safe_print_integer_err(value):
    """
    safe_print_integer_err - Prints an integer
    ----------------------
    Parameter:

    value: The integer
    ----------------------

    Return: True, if value was correctly printed
            else;
            False, and prints in stderr the error
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as err:
        import sys
        print("Exception: {}".format(err), file=sys.stderr)
    return False
