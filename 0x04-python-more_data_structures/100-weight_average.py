#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    weight_average - Returns the weighted average of all integers in a list
    ---------------
    Parameters:

    my_list: The list
    ---------------

    Return: The weighted average, else 0
    """
    if my_list is None:
        return 0
    w_avg = 0
    w_sum = 0
    for i in range(len(my_list)):
        w_avg += my_list[i][0] * my_list[i][1]
        w_sum += my_list[i][1]
    return (w_avg / w_sum)
