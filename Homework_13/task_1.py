# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.

import random


# Взял за пример 11 ДЗ
class Matrix:
    """
    Принимает количество строк и столбцов. Создаёт матрицу,
    заполненную случайными значениями от 0 до 9.
    """

    def __init__(self, rows, columns):
        """
        :param rows: количество строк
        :param columns: количество столбцов
        """
        self.matrix = self.__create_matrix(rows, columns)

    def __create_matrix(self, rows, columns):
        try:
            self.matrix = [[0] * columns for _ in range(rows)]
        except TypeError as e:
            print(f'Попыткаа создания матрицы закончилась с ошибкой: {e}. '
                  f'\nДля создания матрицы необходимо использовать целые числа.'
                  f'\nВы ввели "{rows}" в качестве количества строк, '
                  f'и "{columns}" в качестве количества столбцов')
        else:
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


class MyException(Exception):


    pass


if __name__ == '__main__':
    matrix = Matrix('3', '3')
