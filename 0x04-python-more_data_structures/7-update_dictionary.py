#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):

    """
    Function:
    ---------
    update_dictionary - Replaces or adds a key and/or value to a dictionary

    Parameters:
    -----------
    a_dictionary - The dictionary
    key - The key
    value - The value assigned to a key

    Return: The updated dictionary
    """
    if key in a_dictionary or key not in a_dictionary:
        a_dictionary[key] = value

    return a_dictionary
