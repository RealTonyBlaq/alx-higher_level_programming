#!/usr/bin/python3

""" Module for concatenating arguments to a list """

from sys import argv as av
loader = __import__('6-load_from_json_file').load_from_json_file
saver = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
my_list = []
try:
    my_list = loader(filename)
    for i in range(1, len(av)):
        my_list.append(av[i])
    saver(my_list, filename)
except FileNotFoundError:
    saver(my_list, filename)
