#!/usr/bin/python3
""" Module for class_to_json """


def class_to_json(obj):
    """
    class_to_json - Returns the dictionary description
                    of a simple data structure
    ---------------

    Parameter:

    obj: An instance of a class
        All attributes of obj are serializable
        - list
        - dictionary
        - string
        - integer
        - boolean
    ---------------

    Return: A dictionary representation of JSON
    """
    my_dict = {}
    for key in obj.__dict__:
        value = getattr(obj, key)
        if type(value) in [list, dict, str, int, bool]:
            my_dict[key] = value

    return my_dict
