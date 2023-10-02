#!/usr/bin/python3

""" Defining a class Rectangle """


class Rectangle:
    """ class Rectangle definition """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializing the instance attributes

        width: width of the rectangle (type: int)
        height: height of the rectangle (type: int)

        """
        self.width = width
        self.height = height
        self.number_of_instances += 1

    @property
    def width(self):
        """ gets the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width to value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height to value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of a rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ Returns the perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ Returns a string with a printable """
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for i in range(self.__height):
            string += "#" * self.__width
            if i + 1 != self.__height:
                string += "\n"
        return string

    def __repr__(self):
        """ Returns a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ prints message when an instance is deleted """
        print("Bye rectangle...")
        self.number_of_instances -= 1
