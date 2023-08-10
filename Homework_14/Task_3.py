import pytest

from Homework_14.Task_2 import create_matrix


def test_create_matrix():
    assert create_matrix(3, 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert create_matrix(2, 3) == [[1, 2, 3], [4, 5, 6]]
    assert create_matrix(1, 1) == [[1]]

if __name__ == "__main__":
    pytest.main()