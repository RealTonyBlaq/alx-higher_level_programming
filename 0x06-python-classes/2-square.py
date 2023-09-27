#!/usr/bin/python3
""" Define a class Square """


class Square:
    """
    Defines a square class
    with an __init__ method

    """
    def __init__(self, size=0):
        """ Initializes a private attribute size of class Square """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
