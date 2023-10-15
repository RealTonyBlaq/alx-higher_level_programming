#!/usr/bin/python3
""" Module for Rectangle that inherits from Base """

from models.base import Base

class Rectangle(Base):
    """ Define a child class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the attributes """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__id = id
        if id is None:
            super().__init__()
            self.__id = self.id

    @property
    def width(self):
        """ Retrieves the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the value for width """
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieves the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height """
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """ Retrieves x """
        return self.__x
    
    @x.setter
    def x(self, value):
        """ Sets x to value """
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Retrieves y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets y to value """
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def id(self):
        """ Retrieves id """
        return self.__id

    @id.setter
    def id(self, value):
        """ Sets id to value """
        if value < 0:
            raise ValueError("id must be >= 0")
        self.__id = value
