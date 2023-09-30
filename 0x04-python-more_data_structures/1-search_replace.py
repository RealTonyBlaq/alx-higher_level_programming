#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    search_replace - Searches a list for a value(search) and replaces all occurrences
                    with another value(replace) in a new list
    --------------
    Parameters:

    my_list: The original list
    search: The value to be searched for
    replace: The value to replace "search" if found
    --------------

    Return: A new list
    """
    new = []
    for i in my_list:
        if i == search:
            new.append(replace)
        else:
            new.append(i)
    return new
