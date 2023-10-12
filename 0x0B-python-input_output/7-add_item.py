#!/usr/bin/python3
""" Module for concatenating arguments to a list """
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
argv.pop(0)
try:
    my_list = load_from_json_file(filename)
    if my_list is None:
        save_to_json_file(argv, filename)
    else:
        my_list.extend(argv)
        save_to_json_file(my_list, filename)
except FileNotFoundError:
    save_to_json_file(argv, filename)
