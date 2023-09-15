#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    """
    Function:
    ---------
    print_sorted_dictionary - prints a dictionary by ordered keys

    Parameter:
    -----------
    a_dictionary - The dictionary

    Return: Nothing
    """
    for a, b in sorted(a_dictionary.items()):
        print("{}: {}".format(a, b))
