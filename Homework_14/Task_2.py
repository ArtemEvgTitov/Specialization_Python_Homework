import unittest

def create_matrix(rows, columns):
    matrix = [[0] * columns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = num
            num += 1
    return matrix

class TestCreateMatrix(unittest.TestCase):
    def test_create_matrix(self):
        self.assertEqual(create_matrix(3, 4), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        self.assertEqual(create_matrix(2, 3), [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(create_matrix(1, 1), [[1]])

if __name__ == "__main__":
    unittest.main()
