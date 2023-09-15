#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    """
    Function:
    only_diff_elements - Returns a set of all elements present in one set
                        and not in both sets

    Parameters:
    set_1 - The first set of elements
    set_2 - The second set of elements

    Return: A new set with the elements
    """
    return (set_1 ^ set_2)
