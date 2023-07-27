from Homework_11.Matrix import Matrix

if __name__ == '__main__':
    help(Matrix)
    matrix1 = Matrix(4, 4)
    print(matrix1)
    matrix2 = Matrix(4, 4)
    print(matrix2)
    print(matrix1 == matrix2)
    print(matrix1 + matrix2)
    print(matrix1 * matrix2)
