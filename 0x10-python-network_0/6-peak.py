#!/usr/bin/python3
""" Script returns the largest number in a list """


def find_peak(list_of_integers):
    if not list_of_integers or list_of_integers == []\
      or not isinstance(list_of_integers, list):
        return None

    low = 0
    high = len(list_of_integers) - 1
    while low < high:
        mid
        if list_of_integers[low] > list_of_integers
