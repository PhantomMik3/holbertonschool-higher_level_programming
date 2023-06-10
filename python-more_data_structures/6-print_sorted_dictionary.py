#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    order_Keys = sorted(a_dictionary.keys())

    for a in order_Keys:
        print("{}: {}".format(a, a_dictionary[a]))
