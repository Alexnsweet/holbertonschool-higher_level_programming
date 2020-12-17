#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_square = list(map(list, matrix))

    for i in new_square:
        for j in range(len(i)):
            i[j] = i[j] ** 2
    return new_square
