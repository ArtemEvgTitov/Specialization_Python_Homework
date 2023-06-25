# Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def hexadecimal(number):
    HEX = 16
    HEXADEMIKAL_NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    result = ''
    sign = ''

    if HEX > number >= 0:
        return HEXADEMIKAL_NUMBERS[number]
    else:
        if number < 0:
            number *= -1
            sign = '-'
        while number >= HEX:
            remains = number % HEX
            number = number // HEX
            if result == '':
                result += str(HEXADEMIKAL_NUMBERS[remains])
            else:
                result = str(HEXADEMIKAL_NUMBERS[remains]) + result
        return sign + '0x' + HEXADEMIKAL_NUMBERS[number] + result


num: int = int(input('Введите число: '))
print(hexadecimal(num))
print(hex(num))
