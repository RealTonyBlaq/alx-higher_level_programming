#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    safe_print_list - Function prints values in a list
        which could be a string or an integer on a single
        line which then ends with a new line
    Parameters:
    -----------
    my_list: The list
    x: Number of elements to print from my_list
    -----------
    Return: Count of printed elements
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
