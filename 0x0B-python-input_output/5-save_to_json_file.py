#!/usr/bin/python3

""" Module for writing JSON representation to files """


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - Writes the JSON representation of an object to a file
    -----------------

    Parameters:

    my_obj: The object to be serialized
    filename: The file

    Return: Nothing
    """
    import json

    with open(filename, mode='w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(my_obj))
