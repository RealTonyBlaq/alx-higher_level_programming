#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):

    """
    Function:
    ---------
    multiply_list_map - Returns a new dictionary with all values multiplied
                        by number

    Parameters:
    -----------
    my_list - The list
    number - The number

    Return: The updated/new list
    """
    return ([map(lambda x: x * number, my_list])
