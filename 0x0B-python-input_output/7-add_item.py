#!/usr/bin/python3

""" Module for concatenating arguments to a list """


if __name__ == "__main__":
    from sys import argv as av
    loader = __import__('6-load_from_json_file').load_from_json_file
    saver = __import__('5-save_to_json_file').save_to_json_file

    filename = "add_item.json"
    av.pop(0)
    try:
        my_list = loader(filename)
        if my_list is None:
            saver(av, filename)
        else:
            my_list.extend(av)
            saver(my_list, filename)
    except FileNotFoundError:
        saver(av, filename)
