#!/usr/bin/python3
""" Module for concatenating arguments to a list """

from sys import argv


if __name__ == "__main__":
    loader = __import__('6-load_from_json_file').load_from_json_file
    saver = __import__('5-save_to_json_file').save_to_json_file

    filename = "add_item.json"
    try:
        my_list = loader(filename)
    except FileNotFoundError:
        my_list = []
    my_list.extend(argv[1:])
    saver(my_list, filename)
