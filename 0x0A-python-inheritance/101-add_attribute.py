#!/usr/bin/python3
""" Module for add_attribute """


def add_attribute(a_class, name, value=""):
    """
    add_attributes - Adds attributes to an object
    --------------

    Parameter:
    a_class: The class
    name: Object
    value: @name's value
    """
    if not hasattr(a_class, "__dict__") or hasattr(a_class, "__slots__"):
        raise TypeError("can't add new attribute")
    if not hasattr(a_class, name):
        setattr(a_class, name, value)
    else:
        raise TypeError("can't add new attribute")
