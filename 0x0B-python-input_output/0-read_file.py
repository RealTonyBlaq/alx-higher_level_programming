#!/usr/bin/python3

""" Module for file reading (UTF-8) """


def read_file(filename=""):
    """
    read_file - Reads bytes from a file
    ---------

    Parameter:

    filename: The file to be read
    ---------

    Return: Nothing
    """
    with open(filename) as myFile:
        print(myFile.read())
