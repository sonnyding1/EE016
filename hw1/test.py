from solution import *


def test_base_q_to_decimal():
    assert base_q_to_decimal('101', 2) == 5
    assert base_q_to_decimal('114514', 6) == 10126
    assert base_q_to_decimal('114514', 10) == 114514


def test_base_q_to_p():
    assert base_q_to_p('101', 2, 10) == '5'
    assert base_q_to_p('114514', 6, 2) == '10011110001110'
    assert base_q_to_p('114514', 10, 7) == '654601'
    assert base_q_to_p('0', 2, 10) == '0'


def test_sorted_merge():
    assert sorted_merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert sorted_merge([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 3, 4, 5]


def test_multiple_sorted_merge():
    assert multiple_sorted_merge([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert multiple_sorted_merge([[1, 4, 7], [2, 5, 8], [3, 6, 9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert multiple_sorted_merge([]) == []
    assert multiple_sorted_merge([[]]) == []
    assert multiple_sorted_merge([[1]]) == [1]


def test_find_root():
    assert find_root(4) == (2, 2)
    assert find_root(16) == (2, 4)
    assert find_root(114514) is False
    assert find_root(729) == (9, 3)


def test_factorize():
    assert factorize(32) == [2, 2, 2, 2, 2]
    assert factorize(114514) == [2, 31, 1847]
    assert factorize(1) == []
    assert factorize(2) == [2]


def test_least_common_multiple():
    assert least_common_multiple(2, 4, 8, 16) == 16
    assert least_common_multiple(114514, 1919810) == 109922561170


def test_greatest_common_divisor():
    assert greatest_common_divisor(2, 4, 8, 16) == 2
    assert greatest_common_divisor(24, 30) == 6
    assert greatest_common_divisor(114514, 1919810) == 2


def test_unique_values():
    assert unique_values([[1, 2, 3], [3, 4, 5], [5, 6, 7]]) == [1, 2, 3, 4, 5, 6, 7]
