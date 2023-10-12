#!/usr/bin/python3
""" Module for checking class """


def is_same_class(obj, a_class):
    """ Returns True or False
    if an object is an instance of the specified class
    """

    return (type(obj) == a_class)
