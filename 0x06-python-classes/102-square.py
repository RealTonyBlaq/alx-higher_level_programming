#!/usr/bin/python3
""" Defines a class Square """


class Square:
    """
    Defines a square class
    with an __init__ method

    """
    def __init__(self, size=0):
        """ Initializes a private attribute (size) of class Square """
        self.__size = size

    def __lt__(self, other):
        """ Define behavior for the "<" operator """
        return len(self) < len(other)

    def __le__(self, other):
        """ Defines behavior for the "<=" operator """
        return len(self) <= len(other)

    def __gt__(self, other):
        """ Define behavior for the ">" operator """
        return len(self) > len(other)

    def __ge__(self, other):
        """ Defines behavior for the ">=" operator """
        return len(self) >= len(other)

    def __eq__(self, other):
        """ Define behavior for the "==" operator """
        return len(self) == len(other)

    def __ne__(self, other):
        """ Defines behavior for the "!=" operator """
        return len(self) != len(other)

    def __len__(self):
        """ Define the area of the area of the square in comparison """
        return self.__size ** 2

    def area(self):
        """ Returns the area of the square (size^2) """
        return self.__size ** 2

    @property
    def size(self):
        """ Gets the value size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets self.__size to equal size """
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
