# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

def entering_number(letter):
    number = int(input(f"Введите {letter}: "))
    return number

def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a != b and a != c and b != c:
            return "Разносторонний треугольник"
        elif a == b and a == c:
            return "Равносторонний треугольник"
        else:
            return "Равнобедренный треугольник"
    else:
        return "Треугольник с такими сторонами не существует"

start = True
while start:
    try:
        a = entering_number('a')
        b = entering_number('b')
        c = entering_number('c')
        print(check_triangle(a, b, c))
    except:
        start = False
