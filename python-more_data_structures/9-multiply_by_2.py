#!/usr/bin/python3


def multiply_by_2(a_dictionary):

    Newdictionary = {}

    for keys, value in a_dictionary.items():
        Newdictionary[keys] = value * 2

    return Newdictionary
