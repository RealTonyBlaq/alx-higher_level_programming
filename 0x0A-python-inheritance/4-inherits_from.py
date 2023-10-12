#!/usr/bin/python3
""" Module checks an instance of an object in a class"""


def inherits_from(obj, a_class):
    """
    Returns True or False, if:

    the object is an instance of a class that
    inherited (directly or indirectly) from the specified class

    """
    return ((issubclass(type(obj), a_class)) and type(obj) is not a_class)
