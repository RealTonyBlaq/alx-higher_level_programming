#!/usr/bin/python3

""" Module for a lookup function """


def lookup(obj):
    """
    lookup - Returns a list of available attributes and methods
            of an object
    -------

    Parameter:

    obj: The object
    -------

    Return: A list of attributes
    """
    return dir(obj)
