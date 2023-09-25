#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    safe_print_list_integers - Prints x elements of type (int) from a list
                            which could contain both integers and strings
    ------------------------
    Parameters:

    my_list: The list
    x: Number of elements to print
    ------------------------

    Return: Total number of integers printed
    """
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count
