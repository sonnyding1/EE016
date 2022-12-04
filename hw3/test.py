from solution import *
import numpy as np


def test_modify_array():
    # hard to write unit tests
    # assert modify_array(np.arange(0, 15, 0.5))
    pass


def test_multiply_matrices():
    assert (multiply_matrices(np.array([[1, 2], [3, 4]]), np.array([[6, 7], [8, 9]]))
            == np.array([[22, 25], [50, 57]])).all()


def test_knapsack_topdown():
    assert knapsack_topdown([1, 4, 5, 7], [1, 3, 4, 5], 7, None) == 9


def test_LCS():
    assert LCS('hello world', 'owo') == 'owo'


def test_rotate90():
    # 1 2 3   7 4 1
    # 4 5 6   8 5 2
    # 7 8 9   9 6 3
    assert (rotate90(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) == np.array([[7, 4, 1], [8, 5, 2], [9, 6, 3]])).all()
