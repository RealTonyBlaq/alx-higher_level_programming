#!/usr/bin/python3

""" Module for deserializing a JSON file """


def load_from_json_file(filename):
    """
    load_from_json_file - Loads a py object from a json file
    -------------------

    Parameter:

    filename: The json file
    -------------------

    Return: the py object
    """
    import json

    with open(filename, encoding='utf-8') as json_file:
        data_read = json_file.read()
    return json.loads(data_read)
