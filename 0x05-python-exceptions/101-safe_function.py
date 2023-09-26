#!/usr/bin/python3

def safe_function(fct, *args):
    """
    safe_function - Function that executes another function safely
    --------------
    Parameters:

    fct: The function
    args: The argument to fct
    ---------------

    Return: The result of the function
            else;
            False, and prints the error to stderr
    """
    try:
        ret = fct(*args)
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
    return ret
