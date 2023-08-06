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
        rows = self.__digit_check(rows)
        columns = self.__digit_check(columns)
        try:
            self.matrix = [[0] * columns for _ in range(rows)]
        except TypeError as e:
            self.__print_error(e, rows, columns)
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
        try:
            for row in self.matrix:
                string_matrix += f"\n{row}"
        except TypeError as e:
            self.__print_error(e, self.matrix)
        finally:
            return string_matrix

    def __digit_check(self, number):
        try:
            number = int(number)
            if number < 1:
                raise MyException(number)
            return number
        except ValueError as e:
            self.__print_error(e, number)

    def __print_error(self, e, *args):
        print(f'Попытка создания матрицы закончилась с ошибкой: {e}. '
              f'\nДля создания матрицы необходимо использовать целые числа.'
              f'\nВы ввели: "{args}"')


class MyException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Размер матрицы не может быть отрицательным или равным нулю. Вы ввели {self.value}'


if __name__ == '__main__':
    matrix = Matrix('a', '3')
    print(matrix)
