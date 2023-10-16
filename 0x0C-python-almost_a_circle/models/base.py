#!/usr/bin/python3
""" Module for class Base """

import json


class Base:
    """ Define a class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the attributes """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        to_json_string - Returns the JSON string representation
                        of list_dictionaries

        Parameter:

        list_dictionaries: A dictionary
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return []
