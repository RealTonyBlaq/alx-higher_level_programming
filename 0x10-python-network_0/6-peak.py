#!/usr/bin/python3
""" Script returns the largest number in a list """


def find_peak(list_of_integers):
    if not list_of_integers or list_of_integers == []\
      or not isinstance(list_of_integers, list):
        return None

    low = 0
    high = len(list_of_integers) - 1
    while low < high:
        mid = (low + high) / 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return list_of_integers[low]
