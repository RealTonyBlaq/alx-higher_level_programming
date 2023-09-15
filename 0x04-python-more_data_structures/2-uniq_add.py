#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    The function (uniq_add) - adds all unique integers in the list
    Parameter: (my_list) - The list

    This addition is performed only once

    Return: if the list is empty, it returns 0
    else, the sum of unique numbers is returned.
    """
    if my_list == []:
        return 0
    sum = 0
    new = set(my_list)
    for value in new:
        sum += value
    return sum
