#!/usr/bin/python3

""" Module for JSON representation """


def from_json_string(my_str):
    """
    to_json_string - Returns an object represented by a JSON string
    --------------

    Parameter:

    my_obj: The object
    --------------

    Return: Python object
    """
    import json as j

    data = j.load(my_str)

    return data
