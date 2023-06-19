# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки:
# “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = True
while start:
    try:
        num = int(input("Введите число (от 0 до 100000): "))
        if num == 0 or num == 1:
            print("Числа меньше 2 не являются простыми")
        elif num < 0 or num > 100000:
            print("Введите число от 0 до 100000.")
        elif is_prime(num):
            print(f"Число {num} является простым.")
        else:
            print(f"Число {num} является составным.")

    except:
        start = False

