import random
import numpy


class Matrix:
    """
    Принимает количество строк и столбцов. Создаёт матрицу,
    заполненную случайными значениями от 0 до 9.
    """

    def __init__(self, rows: int, columns: int):
        """
        :param rows: количество строк
        :param columns: количество столбцов
        """
        self.matrix = self.__create_matrix(rows, columns)

    def __create_matrix(self, rows, columns):
        self.matrix = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                self.matrix[i][j] = random.randint(0, 9)
        return self.matrix

    def __str__(self):
        """
        Печать матрицы выполнена построчно.
        :return: Возвращает строку для вывода через print
        """
        string_matrix = ''
        for row in self.matrix:
            string_matrix += f"\n{row}"
        return string_matrix

    def __eq__(self, other):
        """
        Сравнение выполнено по количеству строк и столбцов.
        :return: Возвращает True или False
        """
        return numpy.shape(self.matrix) == numpy.shape(other.matrix)

    def __add__(self, other):
        """
        Сложение по каждому элементу двух матриц.
        :return: Возвращает строку, содержащую либо результат сложения,
            либо сообщение для пользователя о некорректности переданных матриц
        """
        if self == other:
            rows, columns = numpy.shape(self.matrix)
            result_matrix = [[0] * columns for _ in range(rows)]
            for i in range(rows):
                for j in range(columns):
                    result_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return f'Результат сложения матриц {result_matrix}'
        else:
            return 'Матрицы не равны. ' \
                   'Cкладывать можно только матрицы с одинаковым количеством строк и столбцов'

    def __mul__(self, other):
        """
        Умножение матриц выполнено при помощи numpy.dot
        :return: Возвращает строку, содержащую либо результат умножения,
            либо сообщение для пользователя о некорректности переданных матриц
        """
        if self == other:
            result_matrix = numpy.dot(self.matrix, other.matrix)
            return f'Результат умножения матриц \n{result_matrix}'
        else:
            return 'Матрицы не равны. ' \
                   'Умножать можно только матрицы с одинаковым количеством строк и столбцов'
