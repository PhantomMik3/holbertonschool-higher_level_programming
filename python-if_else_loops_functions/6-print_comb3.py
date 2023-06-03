#!/usr/bin/python3

for st_digit in range(10):
    for nd_digit in range(st_digit + 1, 10):
        if st_digit == 8 and nd_digit == 9:
            print("{:d}{:d}".format(st_digit, nd_digit), end="")
        else:
            print("{:d}{:d}".format(st_digit, nd_digit), end=", ")
print()
