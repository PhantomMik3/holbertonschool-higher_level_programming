#!/usr/bin/python3

def delete_at(my_list=[], indx=0):

    if indx < 0 or indx >= len(my_list):
        return my_list

    del my_list[indx]
    return my_list
