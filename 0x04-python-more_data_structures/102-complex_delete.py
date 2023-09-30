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
    for x in range(0, len(a_dictionary)):
        for y in a_dictionary:
            if a_dictionary[y] == value:
                del a_dictionary[y]
                x += 1
                break
    return a_dictionary
