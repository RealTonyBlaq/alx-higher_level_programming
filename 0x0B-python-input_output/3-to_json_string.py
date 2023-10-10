#!/usr/bin/python3

""" Module for JSON representation """


def to_json_string(my_obj):
    """
    to_json_string - Returns the JSON representation of any object
    --------------

    Parameter:

    my_obj: The object
    --------------

    Return: JSON representation
    """
    import json as j

    return j.dumps(my_obj)
