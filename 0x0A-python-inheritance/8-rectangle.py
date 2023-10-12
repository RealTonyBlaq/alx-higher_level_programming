#!/usr/bin/python3

"""
Module for class Rectangle which inherits
from the BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Define the class Rectangle """

    def __init__(self, width, height):
        """
        Initializes the private attributes:

        args:
        ----
        width: The width of the rectangle
        height: The height of the rectangle

        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
