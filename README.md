# Веб-разработка на Python. Технологическая специализация

---
## Погружение в Python (лекции)

---
### Урок 1. Основы Python

1. Решить задачи, которые не успели решить на семинаре.

2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

---
### Урок 2. Простые типы данных

1. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

---
### Урок 3. Коллекции

1. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

2. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

3. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

---
### Урок 4. Функции

1. Напишите функцию для транспонирования матрицы
2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

---
### Урок 5. Интераторы и генераторы

1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии
3. Создайте функцию генератор чисел Фибоначчи.

---
### Урок 6. Модули

1. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
2. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
3. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

---
### Урок 7. Файлы и файловая система

1. Напишите функцию группового переименования файлов. Она должна:
2. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
3. принимать параметр количество цифр в порядковом номере.
4. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
5. принимать параметр расширение конечного файла.
6. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

---
### Урок 8. Сериализация

Решить задачи, которые не успели решить на семинаре.

Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.

* Для дочерних объектов указывайте родительскую директорию.
* Для каждого объекта укажите файл это или директория.
* Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.

Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов.

---
### Урок 9. Декораторы

Напишите следующие функции:
* Нахождение корней квадратного уравнения
* Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
* Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
* Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл.

---
### Урок 10. ООП. Начало

Доработать задачи 5-6. Создайте класс-фабрику.
* Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
* Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.

Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра.

---
### Урок 11. ООП. Особенности Python

Создайте класс Матрица. Добавьте методы для:
* вывода на печать,
* сравнения,
* сложения,
* *умножения матриц

---
### Урок 12. ООП. Финал

Создайте класс студента.
* Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
* Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
* Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
* Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых.

---
### Урок 13. Исключения

Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях. Напишите к ним
классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например
нельзя создавать прямоугольник со сторонами
отрицательной длины.

---
### Урок 14. Основы тестирования

Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях.
Напишите к ним тесты.
2-5 тестов на задачу в трёх вариантах:
* doctest,
* unittest,
* pytest.

---
### Урок 15. Обзор стандартной библиотеки Python

Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной
информации. Также реализуйте возможность запуска из
командной строки с передачей параметров.