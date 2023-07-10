# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

from random import randint as rd
from task_2 import is_valid_queens

def generate_random_queens():
    queens = [(i, rd(1, 8)) for i in range(1, 9)]
    return queens


if __name__ == '__main__':
    successful_count = 0
    while successful_count < 4:
        queens = generate_random_queens()
        if is_valid_queens(queens):
            print("Успешные расстановки:", queens)
            successful_count += 1