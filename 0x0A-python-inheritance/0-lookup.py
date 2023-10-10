#!/usr/bin/python3

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
    return [attri for attri in dir(obj)]
