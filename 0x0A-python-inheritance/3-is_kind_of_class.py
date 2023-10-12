#!/usr/bin/python3
""" Module checks for instance of an object """


def is_kind_of_class(obj, a_class):
    """ Returns True or False
    if obj is an instance of a_class or inherited from a_class
    """
    return isinstance(obj, a_class)
