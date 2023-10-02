#!/usr/bin/python3

""" Defining a class Rectangle """


class Rectangle:
    """
    class: Rectangle

    Definition of instances:
    ----------

    number_of_instances (public): initialized to 0, counts the number of
                        instances created.
                        increments by 1 during each new instantiation
                        decrements by 1 during each instance deletion
    print_symbol (public): initialized to "#", used as a symbol for string
                        representation

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializing the instance attributes

        width: width of the rectangle (type: int)
        height: height of the rectangle (type: int)

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Defines a static method that compares two rectangles and
        returns the biggest rectangle based on area

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Defines a class method that represents:

        width = height = size
        which turns a rectangle into a square

        """
        return cls(size, size)

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
            string += str(self.print_symbol) * self.__width
            if i + 1 != self.__height:
                string += "\n"
        return string

    def __repr__(self):
        """ Returns a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ prints message when an instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
