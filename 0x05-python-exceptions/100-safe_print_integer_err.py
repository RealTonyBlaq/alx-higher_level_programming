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
    import sys
    try:
        print("{:d}".format(value))
        return True
    except TypeError as err:
        sys.stderr.write("Exception: ")
        sys.stderr.write(err)
        sys.stderr.write("\n")
    except ValueError as er:
        sys.stderr.write("Exception: ")
        print(er, file=sys.stderr)
        sys.stderr.write("\n")
    return False
