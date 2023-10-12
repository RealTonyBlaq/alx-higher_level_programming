#!/usr/bin/python3

"""
Module for class Rectangle which inherits
from the BaseGeometry class

"""


class BaseGeometry:
    """ Define a class """

    def area(self):
        """ Public instance method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0". format(name))


class Rectangle(BaseGeometry):
    """ Define the class Rectangle """

    def __init__(self, width, height):
        """ Initializes the private attributes """
        self.__width = width
        self.__height = height
        super().__init__()
