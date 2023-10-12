#!/usr/bin/python3

""" Module contains an class """


class BaseGeometry:
    """ Define a class """

    def area(self):
        """ Public instance method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0". format(name))
