#!/usr/bin/python3

def max_integer(my_list=[]):

    if my_list is None:
        return None

    if len(my_list) == 0:
        return None

    Maxed_Integer = sorted(my_list, reverse=True)

    return Maxed_Integer[0]
