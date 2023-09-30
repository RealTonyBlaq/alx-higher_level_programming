#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    complex_delete: Deletes keys with a specific value in a dictionary
    ---------------
    Parameters:

    a_dictionary: The dictionary
    value: The value whose keys will be deleted
    ---------------

    Return: The dictionary
    """
    for x, y in a_dictionary.items():
        if y == value:
            del (x)
    return a_dictionary
