#!/usr/bin/python3
def no_c(my_string):
    if my_string == None:
        return None
    new_string = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            new_string += c
    return new_string