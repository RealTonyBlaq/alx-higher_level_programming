#!/usr/bin/python3

"""
Module for class Rectangle which inherits
from the BaseGeometry class

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Define the class Rectangle """

    def __init__(self, width, height):
        """ Initializes the private attributes """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """ Returns a string representation of Rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ Returns the area of a Rectangle """
        return self.__height * self.__height
