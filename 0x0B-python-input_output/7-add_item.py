#!/usr/bin/python3

""" Module for concatenating arguments to a list """


from sys import argv as av
loader = __import__('6-load_from_json_file').load_from_json_file
saver = __import__('5-save_to_json_file').save_to_json_file

def main():
    """ main - check the code """
    if len(av) < 2:
        raise ValueError("Usage: ./file <text>")
    filename = "add_item.json"
    try:
        my_list = loader(filename)
    except FileNotFoundError:
        my_list = []
    finally:
        for i in range(1, len(av)):
            my_list.append(av[i])
        saver(my_list, filename)


main()
