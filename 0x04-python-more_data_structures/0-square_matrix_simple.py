#!/usr/bin/python3
def square_matrix_simple(matrix):
    matrix_new = []
    for row in matrix:
        row_new = []
        for n in row:
            row_new.append(n ** 2)
        matrix_new.append(row_new)
    return matrix_new
