# Напишите функцию для транспонирования матрицы

import numpy
import random


def create_matrix():
    rows, columns = map(int, input('Введите размер матрицы через пробел. Например, "3 8": ').split(' '))
    matrix = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = random.randint(1, 9)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def matrix_transposition(matrix):
    matrix = numpy.array(matrix)
    data = matrix.transpose()
    return data


def start_matrix():
    while True:
        try:
            matrix = create_matrix()
            print('\nСоздана матрица:\n')
            print_matrix(matrix)
            transpose_matrix = matrix_transposition(matrix)
            print('\nМатрица транспонированна:\n')
            print_matrix(transpose_matrix)
        except:
            print("Работа завершена")
            break


start_matrix()
