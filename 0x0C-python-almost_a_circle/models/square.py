#!/usr/bin/python3
""" Module for child class Square that inherits Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define a class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the attributes

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
