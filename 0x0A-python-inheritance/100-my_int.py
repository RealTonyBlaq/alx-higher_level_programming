#!/usr/bin/python3
""" Module for class MyInt that inherits from 'int' """


class MyInt(int):
    """ Define the rebel class MyInt """

    def __eq__(self, other):
        """
        Return (inverted):
        --------
        True: if self != other
        False: if self == other
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        Return (inverted):
        --------
        True: if self == other
        False: if self != other
        """
        return not super().__ne__(other)
