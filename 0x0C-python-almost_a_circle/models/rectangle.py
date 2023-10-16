#!/usr/bin/python3
""" Module for Rectangle that inherits from Base """

from models.base import Base


class Rectangle(Base):
    """ Define a child class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the attributes

        parameters:
        -----------

        width (int): width of the Rectangle
        height (int): height of the Rectangle
        x (int)
        y (int)
        id (int): Super class attribute
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieves the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Retrieves x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x to value """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def id(self):
        """ Retrieves id """
        return self.__id

    @id.setter
    def id(self, value):
        """ Sets id to value """
        self.__id = value

    def area(self):
        """ Returns the area of a rectangle """
        return self.__height * self.__width

    def display(self):
        """ Prints the rectangle using '#' to stdout """
        [print() for i in range(self.__y)]
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width, end="")
            if i < self.__height:
                print()

    def __str__(self):
        """ Returns the string representation of Rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.__id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Updates the Rectangle attributes with *args """
        if args:
            for i, value in enumerate(args):
                if i == 0:
                    self.__id = value
                if i == 1:
                    self.__width = value
                if i == 2:
                    self.__height = value
                if i == 3:
                    self.__x = value
                if i == 4:
                    self.__y = value
        else:
            for name, val in kwargs.items():
                if name == "id":
                    self.__id = val
                if name == "width":
                    self.__width = val
                if name == "height":
                    self.__height = val
                if name == "x":
                    self.__x = val
                if name == "y":
                    self.__y = val

    def to_dictionary(self):
        """ Returns the dictionary representation of Rectangle """
        dic = {}
        for key in ["x", "y", "id", "height", "width"]:
            value = getattr(self, key)
            dic[key] = value
        return dic
