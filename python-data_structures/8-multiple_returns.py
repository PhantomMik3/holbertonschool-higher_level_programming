#!/usr/bin/python3

def multiple_returns(sentence):

    if sentence == "":
        length = len(sentence)
        char = None
        return length, char

    length = len(sentence)
    char = sentence[0]

    return length, char
