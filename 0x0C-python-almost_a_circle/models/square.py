#!/usr/bin/python3
""" Module for child class Square that inherits Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define a class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the attributes based on Rectangle

        Parameters:
        -----------

        size (int): Size of the Square
        x (int): Position x-axis
        y (int): Position y-axis
        id (int): if id is not passed, it is inherited
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns the string representation of Square """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """ Returns the value for size """
        return self.width
    
    @size.setter
    def size(self, value):
        """ Sets size to value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
