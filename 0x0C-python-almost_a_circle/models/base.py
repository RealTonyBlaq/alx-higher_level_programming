#!/usr/bin/python3
""" Module for class Base """

import json
import csv
import os


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

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding='utf-8') as f:
                f_read = f.read()
            json_list = Base.from_json_string(f_read)
            return list(map(lambda x: cls.create(**x), json_list))
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes in CSV"""
        filename = cls.__name__ + ".csv"
        if list_objs is not None and len(list_objs) != 0:
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    my_list = [obj.id, obj.width, obj.height, obj.x, obj.y]
                else:
                    my_list = [obj.id, obj.size, obj.x, obj.y]
            with open(filename, "w", encoding='utf-8') as file:
                format = csv.writer(file)
                format.writerow(my_list)
        else:
            with open(filename, "w", encoding='utf-8') as file:
                file.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes in csv """
        filename = cls.__name__ + ".csv"
        with open(filename, "r") as file:
            if cls.__name__ == "Rectangle":
                reader = csv.DictReader(
                    file, fieldnames={'id', 'width', 'height', 'x', 'y'})
            elif cls.__name__ == "Square":
                reader = csv.DictReader(
                    file, fieldnames={'id', 'size', 'x', 'y'})

            instances = []
            for instance in reader:
                instance = {x: int(y) for x, y in instance.items()}
                temp = cls.create(**instance)
                instances.append(temp)

        return instances
