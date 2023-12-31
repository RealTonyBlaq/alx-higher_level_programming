#!/usr/bin/python3
"""
    This is the ``say_my_name`` module.
    The say_my_name module supplies one function, say_my_name().

"""


def say_my_name(first_name, last_name=""):
    """
        this functions prints a string:
        e.g: My name is <first name> <last name>

        Args:
            first_name (str): The first name
            last_name (str): The last name (Optional)
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
