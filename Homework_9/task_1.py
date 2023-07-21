# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.

import csv
import json
import math
import random


def generate_random_csv(filename: str = 'random_numbers.csv', rows: int = 1000):
    """
    Генерация csv файла с тремя случайными числами в каждой строке
    """
    max_random_number = rows
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            row = [random.randint(1, max_random_number) for _ in range(3)]
            writer.writerow(row)


def quadratic_equation_decorator(func):
    """
    Декоратор, запускающий функцию нахождения корней квадратного
    уравнения с каждой тройкой чисел из csv файла, а также сохраняющий
    переданные параметры и результаты работы функции в json файл
    """
    def wrapper(filename: str = 'random_numbers.csv'):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                print(f"For {row } roots: {result}")
                data = {
                    'arguments': row,
                    'result': f'{result}'
                }
                with open('results.json', 'a') as json_file:
                    json.dump(data, json_file)
                    json_file.write('\n')
    return wrapper


@quadratic_equation_decorator
def solve_quadratic_equation(a, b, c):
    """
    Функция нахождения корней квадратного уравнения
    """
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        # Два вещественных корня
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        # Один вещественный корень (корни совпадают)
        root = -b / (2 * a)
        return root
    else:
        # Комплексные корни (нет вещественных корней)
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2


if __name__ == '__main__':
    generate_random_csv(rows=367)
    solve_quadratic_equation()
