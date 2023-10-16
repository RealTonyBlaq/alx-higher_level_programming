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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string - Returns the JSON string representation
                        of list_dictionaries

        Parameter:

        list_dictionaries: A dictionary
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file - Saves the JSON string representation of
                        list_objs to a file

        Parameter:

        cls: class
        list_objs: List of instances
        """
        filename = cls.__name__ + ".json"
        if list_objs:
            a_list = []
            for attr in list_objs:
                a_list.append(attr.to_dictionary())
            with open(filename, "w", encoding='utf-8') as f:
                f.write(Base.to_json_string(a_list))
        else:
            empty = None
            with open(filename, "w", encoding='utf-8') as f:
                f.write(Base.to_json_string(empty))

    @staticmethod
    def from_json_string(json_string):
        """ Returns a list of the json string """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(14, 6)
        elif cls.__name__ == "Square":
            dummy = cls(14)
        dummy.update(**dictionary)
        return dummy
