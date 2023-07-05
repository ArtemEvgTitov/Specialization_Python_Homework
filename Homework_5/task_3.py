# Создайте функцию генератор чисел Фибоначчи

def fibonacci_numbers(n):
    fib1, fib2 = 0, 1
    if n in (1, 2):
        yield 1
    for i in range(1, n + 1):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


for number in fibonacci_numbers(1):
    print(number)
