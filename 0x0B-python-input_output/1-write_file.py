#!/usr/bin/python3

""" Module for writing/appending text to a file"""


def write_file(filename="", text=""):
    """
    write_file - Writes a string to a text file
    ----------

    Parameters:

    filename: The file to be written
    text: The string
    ----------

    Return: Number of bytes written
    """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        n_bytes = my_file.write(text)
    return n_bytes
