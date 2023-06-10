#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None

    Maxvalue = float('-inf')
    A_Key = None

    for key, value in a_dictionary.items():
        if value > Maxvalue:
            Maxvalue = value
            A_Key = key

    return A_Key
