#!/usr/bin/python3
""" Defines a class Square """


class Square:
    """
    Defines a square class with:

    An __init__ method
    area - public instance method
    size - private instance method
    position - private instance method

    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes two private instance attributes (size & position) """
        self.__size = size
        self.__position = position

    def area(self):
        """ Returns the area of the square (size^2) """
        return self.__size ** 2

    def my_print(self):
        """ Prints a square with the letter # of square size (size) """
        if self.__size == 0:
            print()
        else:
            [print() for k in range(0, self.__position[1])]
            i = self.__size
            while i > 0:
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
                i -= 1

    @property
    def size(self):
        """ Gets the value size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets self.__size to equal size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Gets the value of the tuple (position) """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(data, int) for data in value) or
                not all(data >= 0 for data in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
