# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
from fractions import Fraction
from math import gcd


def fraction_sum_and_mult(fraction1, fraction2):
    num1, den1 = map(int, fraction1.split('/'))
    num2, den2 = map(int, fraction2.split('/'))
    DEN1 = den1
    DEN2 = den2

    # Модуль fractions
    f1 = Fraction(num1, den1)
    f2 = Fraction(num2, den2)
    result = f"\nМодуль fractions:\nПроизведение = {f1 * f2}\nСумма = {f1 + f2}\n"

    # Произведение
    num_mult = num1 * num2
    den_mult = den1 * den2
    if num_mult == den_mult:
        mult_fractions = '1'
    else:
        general_gcd = gcd(num_mult, den_mult)
        num_mult /= general_gcd
        den_mult /= general_gcd
        mult_fractions = str(int(num_mult)) + '/' + str(int(den_mult))
    result = result + f"\nМетод: \nПроизведение равно: {mult_fractions}."

    # Сумма
    if den1 != den2:
        num1 *= DEN2
        den1 *= DEN2
        num2 *= DEN1
    num_sum = num1 + num2
    den_sum = den1
    if den_sum == num_sum:
        sum_fractions = '1'
    else:
        general_gcd = gcd(num_sum, den_sum)
        num_sum /= general_gcd
        den_sum /= general_gcd
        sum_fractions = str(int(num_sum)) + '/' + str(int(den_sum))
    result = result + f"\nСумма равна: {sum_fractions}."

    return result



while True:
    fraction1: str = str(input('Введите первую дробь в формате “a/b”: '))
    fraction2: str = str(input('Введите вторую дробь в формате “a/b”: '))
    print(fraction_sum_and_mult(fraction1, fraction2))