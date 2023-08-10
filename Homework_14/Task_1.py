# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.

def create_matrix():
    """
    Создает и возвращает матрицу заданных размеров, заполненную последовательно возрастающими числами.

    >>> create_matrix()
    Введите размер матрицы через пробел. Например, "3 8": 3 4
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    >>> create_matrix()
    Введите размер матрицы через пробел. Например, "3 8": 2 3
    [[1, 2, 3], [4, 5, 6]]

    >>> create_matrix()
    Введите размер матрицы через пробел. Например, "3 8": a b
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for int() with base 10: 'a'
    """
    rows, columns = map(int, input('Введите размер матрицы через пробел. Например, "3 8": ').split(' '))
    num = 1
    matrix = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = num
            num += 1
    return matrix

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
