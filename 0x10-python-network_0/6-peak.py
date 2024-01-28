#!/usr/bin/python3
""" Script returns the largest number in a list """

def find_peak(list_of_integers):
    if list_of_integers == [] or list_of_integers is None:
        return None
    peak = list_of_integers.sort()
    return peak[-1]
