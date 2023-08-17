import random
import logging
import argparse


FORMAT = '{levelname:<8} - {asctime}. {funcName} -> {lineno}. {msg}'
logging.basicConfig(filename='log.', encoding='utf-8', format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger()


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
            logger.info(f'Создана матрица размером {rows}x{columns}')
        except TypeError as e:
            self.__print_error(e, rows, columns)
        else:
            for i in range(rows):
                for j in range(columns):
                    self.matrix[i][j] = random.randint(0, 9)
            logger.info(f'Матрица заполнена значениями: '
                        f'{self.matrix}')
            return self.matrix

    def __str__(self):
        """
        Печать матрицы выполнена построчно.
        :return: Возвращает строку для вывода
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
            logger.info(f'Выполнена проверка аргумента со значением: {number}')
            return number
        except ValueError as e:
            self.__print_error(e, number)

    def __print_error(self, e, *args):
        text = f'Попытка создания матрицы закончилась с ошибкой: {e}. '\
               f'\nБыли введены в качестве аргументов: "{args}"'
        print(text)
        logger.error(text)


class MyException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Размер матрицы не может быть отрицательным или равным нулю. Вы ввели {self.value}'


def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Matrix Creation")

    parser.add_argument("rows", type=int, help="Number of rows")
    parser.add_argument("columns", type=int, help="Number of columns")
    parser.add_argument("--log", type=str, default="matrix.log", help="Log file path")

    args = parser.parse_args()

    setup_logging(args.log)

    try:
        matrix = Matrix(args.rows, args.columns)
        print(matrix)
    except MyException as e:
        logger.error(str(e))



