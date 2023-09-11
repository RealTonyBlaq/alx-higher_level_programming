#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a >= 2:
        new1 = tuple_a[:2]
    elif len_a == 1:
        new1 = tuple_a[0], 0
    else:
        new1 = 0, 0
    if len_b >= 2:
        new2 = tuple_b[:2]
    elif len_b == 1:
        new2 = tuple_b[0], 0
    else:
        new2 = 0, 0
    tuple_c = new1[0] + new2[0], new1[1] + new2[1]
    return tuple_c
