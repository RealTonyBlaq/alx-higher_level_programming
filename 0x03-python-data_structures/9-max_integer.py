#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is []:
        return None
    for i in range(0, len(my_list)):
        if i + 1 != len(my_list):
            if my_list[i] > my_list[i + 1]:
                tmp = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = tmp
    return my_list[-1]
