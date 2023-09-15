#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Function:
    common_elements - Returns a set of common elements in two sets

    Parameters:
    set_1 - The first set of elements
    set_2 - The second set of elements

    Return: A new set with common elements between set_1 and set_2
    """
    return (set_1 & set_2)
