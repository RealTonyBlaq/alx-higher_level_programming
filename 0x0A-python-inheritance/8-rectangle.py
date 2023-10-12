#!/usr/bin/python3

"""
Module for class Rectangle which inherits
from the BaseGeometry class

"""


class Rectangle(BaseGeometry):
    """ Define the class Rectangle """

    def __init__(self, width, height):
        """ Initializes the private attributes """
        self.__width = width
        self.__height = height
        super().__init__()
