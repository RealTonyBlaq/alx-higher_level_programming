#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    list_division - Functions divides element by element in two lists
    ---------------
    Parameters:

    my_list_1: First list
    my_list_2: Second list
    list_length: len of the new list
    ----------------

    Return: A new list
    """
    new = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new.append(result)
        except IndexError:
            print("out of range")
            new.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new.append(0)
        except TypeError:
            print("wrong type")
            new.append(0)
    return new
