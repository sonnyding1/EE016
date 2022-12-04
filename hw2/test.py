from solution import *


def test_string2int():
    # assert string2int('two') == 2
    # assert string2int('nintytwo') == 92
    # assert string2int('threehundredsixtyfour') == 364
    # assert string2int('eightyfourthousandonehundredtwenty') == 84120
    # assert string2int('fivehundredseventythousandtwohundred') == 570200
    # assert string2int('onehundred') == 100
    # assert string2int('onehundredthousandone') == 100001
    # assert string2int('onethousand') == 1000
    # assert string2int('onethousandtwo') == 1002
    # assert string2int('threethousandfortysix') == 3046
    # assert string2int('onehundredonethousandone') == 101001
    # assert string2int('tenthousandone') == 10001
    # assert string2int('onehundredfiftysixthousandthreehundredtwentyseven') == 156327
    assert string2int('nineteenthousandeighteen') == 19018


def test_permutation():
    # It's hard to write test cases for this problem...
    # assert permutation('ABCDEFGHIJ') == []
    assert permutation('ABDCABDABC') == []


def test_sort_string():
    # assert sort_string(['d', 'c', 'b', 'a']) == ['a', 'b', 'c', 'd']
    # assert sort_string(['y', 'o', 'u', 't', 'u', 'b', 'e']) == ['b', 'e', 'o', 't', 'u', 'u', 'y']
    assert sort_string(['str', 's', 'string', 'apple']) == ['apple', 's', 'str', 'string']


def test_longest_increasing_subseq():
    assert longest_increasing_subseq([1, 2, 1, 2, 3]) == [1, 2, 3]
    assert longest_increasing_subseq([1, 1, 4, 5, 1, 4]) == [1, 4, 5]
    assert longest_increasing_subseq([-1]) == [-1]
    assert longest_increasing_subseq([1, 2]) == [1, 2]
    assert longest_increasing_subseq([-1, 0, 1, 2, 1, 0]) == [-1, 0, 1, 2]


def test_rank_in_sorted_list():
    assert rank_in_sorted_list([1, 2, 3, 4, 5], 2) == 3
    assert rank_in_sorted_list([1, 2, 3, 4, 5], 5) == 0
    assert rank_in_sorted_list([1, 2, 3, 4, 5], 1) == 4
    assert rank_in_sorted_list([1, 2, 3, 4, 5], 6) == 0
    assert rank_in_sorted_list([2, 5, 6, 7, 9, 11, 13], 6) == 4
    assert rank_in_sorted_list([2, 5, 6, 7, 9, 11, 13], 10) == 0


def test_search_sorted_matrix():
    assert search_sorted_matrix([[1, 3, 5], [3, 5, 7]], 3) == [0, 1]
    assert search_sorted_matrix([[1, 3, 5], [3, 6, 7]], 5) == [0, 2]


def test_closest_k_points():
    assert closest_k_points([[1, 1], [0, 2]], 1) == [[1, 1]]
    assert closest_k_points([[-2, 3], [1, 6], [0, 3], [-1, -1], [7, 2]], 3) == [[-1, -1], [0, 3], [-2, 3]]
    assert closest_k_points([[-1, -2], [2, 2], [3, 1]], 5) == [[-1, -2], [2, 2], [3, 1]]


def test_quick_select():
    assert quick_select([1, 9, 3, 8, 11, 23, 9, 2, 4], 1) == 1
    assert quick_select([1, 9, 3, 8, 11, 23, 9, 2, 4], 4) == 4
    assert quick_select([1, 9, 3, 8, 11, 23, 9, 2, 4], 6) == 9


def test_h_index():
    assert h_index([2, 3, 4, 5]) == 3
    assert h_index([6, 7, 8, 9]) == 4
