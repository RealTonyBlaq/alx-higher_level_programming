#!/usr/bin/python3

""" Defining a class LockedClass """


class LockedClass:
    """
    LockedClass does not allow the user to create any
    apart from "first_name"

    """
    __slots__ = "first_name"
