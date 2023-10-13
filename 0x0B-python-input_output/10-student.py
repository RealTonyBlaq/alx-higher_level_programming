#!/usr/bin/python3
""" Module for class Student """


class Student:
    """
    Defining the class Student:

    Public instance attributes:
    --------------------------

    first_name
    last_name
    age

    Public method:

    to_json: Retrieves the dictionary representation of
            a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """ Initializes the attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if attrs is not None:
            if isinstance(attrs, list):
                new = {}
                for attr in attrs:
                    if attr in ["first_name", "last_name", "age"]:
                        value = getattr(self, attr)
                        new[attr] = value
                return new
            else:
                return self.__dict__
        else:
            return self.__dict__
