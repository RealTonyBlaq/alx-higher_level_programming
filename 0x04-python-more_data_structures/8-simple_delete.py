#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    """
    Function:
    ---------
    simple_delete - Deletes a key and value to a dictionary if it exists

    Parameters:
    -----------
    a_dictionary - The dictionary
    key - The key

    Return: The updated dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
