#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    if matrix is None or len(matrix) == 0:
        return None

    newmatrix = []

    for row in matrix:
        newrow = []

        for digit in row:
            newrow.append(digit ** 2)

        newmatrix.append(newrow)

    return newmatrix
