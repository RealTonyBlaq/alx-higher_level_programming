#!/usr/bin/python3
""" Module for class Square that inherits class Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Define the class Square """

    def __init__(self, size):
        """
        Initializes the instances

        Parameter:
        size: Size of the Square
                private instance attribute
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns area of a square """
        return self.__size ** 2

    def __str__(self):
        """ Returns the string representation of Square class """
        return "[Square] {}/{}".format(self.__size, self.__size)
