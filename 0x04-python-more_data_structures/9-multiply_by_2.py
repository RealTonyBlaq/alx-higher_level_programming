#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    """
    Function:
    ---------
    multiply_by_2 - multiplies all values in the dictionary by 2

    Parameters:
    -----------
    a_dictionary - The dictionary


    Return: The updated dictionary
    """
    new = {}
    for u, v in a_dictionary.items():
        new[u] = v * 2
    return new
