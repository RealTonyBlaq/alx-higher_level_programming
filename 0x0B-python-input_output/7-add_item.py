#!/usr/bin/python3
""" Module for concatenating arguments to a list """

from sys import argv
loader = __import__('6-load_from_json_file').load_from_json_file
saver = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
argv.pop(0)
try:
    my_list = loader(filename)
    if my_list is None:
        saver(argv, filename)
    else:
        my_list.extend(argv)
        saver(my_list, filename)
except FileNotFoundError:
    saver(argv, filename)
