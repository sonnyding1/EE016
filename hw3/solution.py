import numpy as np


def modify_array(arr):
    """
    :param arr: A NumPy array
    :return: A NumPy array that: 1. rounds all elements to integers. 2. multiply even integers by 2. 3. multiply odd
             integers by 3.
    """
    # Doesn't work because it is not in place
    # dimensions = np.shape(arr)
    # print(arr)
    # arr = np.rint(arr)
    # print(arr)
    # arr = arr.flatten()#.astype('int32')
    #
    # # for i in range(len(arr)):
    # #     if arr[i] % 1 >= 0.5:
    # #         arr[i] = int(arr[i]) + 1
    # #     else:
    # #         arr[i] = int(arr[i])
    # for i in range(len(arr)):
    #     if arr[i] % 2 == 1:
    #         arr[i] *= 3
    #     else:
    #         arr[i] *= 2
    # arr = arr.reshape(dimensions)
    # print(arr)
    # # return arr

    # this works, but hard coded
    # dimensions = np.shape(arr)
    # if len(dimensions) == 1:  # if it is a list
    #     for i in range(len(arr)):
    #         # to int
    #         if arr[i] % 1 >= 0.5:
    #             arr[i] = int(arr[i]) + 1
    #         else:
    #             arr[i] = int(arr[i])
    #         # multiply
    #         if arr[i] % 2 == 1:
    #             arr[i] *= 3
    #         else:
    #             arr[i] *= 2
    # else:
    #     for i in range(len(arr)):
    #         for j in range(len(arr[0])):
    #             # to int
    #             if arr[i][j] % 1 >= 0.5:
    #                 arr[i][j] = int(arr[i][j]) + 1
    #             else:
    #                 arr[i][j] = int(arr[i][j])
    #             # multiply
    #             if arr[i][j] % 2 == 1:
    #                 arr[i][j] *= 3
    #             else:
    #                 arr[i][j] *= 2

    # WHY IN PLACE?? JUST TO TORTURE ME? I used strange boolean indexing to figure out in-place modification
    arr[arr%1!=0] = np.rint(arr[arr%1!=0])
    arr[arr%2==0] *= 2
    arr[arr%2!=0] *= 3


def multiply_tensors(arr1, arr2):
    """
    :param arr1: A 3-dimensional tensor that is (a1, a2, d)
    :param arr2: A 3-dimensional tensor that is (b1, b2, d)
    :return: A 3-dimensional tensor that is the product of two inputs, and is (a1, b2, d), or False if cannot multiply
    """
    # dimension matching
    # column count of the first matrix should equate row count of second matrix, that is, a2 == b1
    a1, a2, d1 = np.shape(arr1)
    b1, b2, d2 = np.shape(arr2)
    # print('arr1: ')
    # print(arr1)
    # print('arr2: ')
    # print(arr2)
    if a2 != b1:
        return False

    output = np.array([])
    # each matrix in arr1 is multiplied with each matrix in arr2
    for d_1 in range(d1):
        for d_2 in range(d2):
            np.append(output, multiply_matrices(arr1[..., d_1], arr2[..., d_2]))  # should be fine?
            # sub_arr1 = np.zeros((a1, a2))
            # for i in range(a1):
            #     for j in range(a2):
            #         sub_arr1[i, j] = arr1[i, j, d_1]
            # sub_arr2 = np.zeros((b1, b2))
            # for i in range(b1):
            #     for j in range(b2):
            #         sub_arr2[i, j] = arr2[i, j, d_2]
            # np.append(output, multiply_matrices(sub_arr1, sub_arr2))
    print('output: ')
    print(output)
    return output


def multiply_matrices(arr1, arr2):
    """
    :param arr1: A matrix that is (a1, a2)
    :param arr2: A matrix that is (b1, b2)
    :return: The matrix product that is (a1, b2)
    """
    # dimension matching
    a1, a2 = np.shape(arr1)
    b1, b2 = np.shape(arr2)
    if a2 != b1:
        return False

    # construct output matrix
    output = np.zeros((a1, b2))

    # matrix multiplication
    for i in range(a1):
        for j in range(b2):
            for k in range(a2):
                output[i, j] += arr1[i, k] * arr2[k, j]
    return output


def knapsack_topdown(V, W, C, dp):
    """
    :param V: Value list
    :param W: Weight list
    :param C: Weight limit as an integer
    :param dp: A matrix that stores the sub problems
    :return: The maximum value I can pack within C
    """
    # initialize dp
    # for dp, there are number of items rows and C columns
    if type(dp) != list:
        dp = [[-1]*(C+1) for _ in range(len(V)+1)]
        dp[0] = [0]*(C+1)  # when capacity equals 0, value is 0
    # base conditions
    if len(V) == 0:
        return 0
    # memoization
    if dp[len(V)][C] != -1:
        return dp[len(V)][C]
    # for each level of recursion, I have the choice of picking an item and not picking an item, return the max
    # I will pick the first item in V and W every time
    if C-W[0] >= 0:
        if len(V) == 1:
            dp[len(V)][C] = V[0]
            return dp[len(V)][C]
        else:
            value_if_choose = V[0] + knapsack_topdown(V[1:], W[1:], C-W[0], dp)
    else:
        value_if_choose = 0
    value_if_not_choose = knapsack_topdown(V[1:], W[1:], C, dp)
    dp[len(V)][C] = max(value_if_not_choose, value_if_choose)
    return dp[len(V)][C]


def LIS(L):
    """
    :param L: A not ordered list of integers
    :return: A list of longest non-decreasing subsequence
    """
    # # I will use DP to solve this problem. When there is only 1 element in list, then we know the LIS is the element
    # # itself. If there are 2 elements, if current ending integer is greater than the LIS's ending integer, then
    # # LIS of the 2 elements list is that if the ending integer is greater than LIS(1)'s ending integer, append ending
    # # integer.
    # # For LIS(3), look for LIS(2), compare ending digits. If it satisfies, append.
    # # I will inevitably need to check for less than O(n^2) times for each level of recursion
    # def helper(L, dp_dict):
    #     # memoization
    #     if tuple(L) in dp_dict:
    #         return dp_dict[tuple(L)]
    #     # base case
    #     if len(L) == 1:
    #         dp_dict[tuple(L)] = L
    #         return dp_dict[tuple(L)]
    #
    #     potential_LIS_this_level = []
    #     max_length_this_level = 0
    #     for i in range(len(L)):
    #         for j in range(i):
    #             # we only compare two ints each time, then call helper() on the list after i and j, extend
    #             if L[j] <= L[i]:
    #                 dummy_list = [j, i]
    #                 dummy_list.extend(helper(L[i+1:], dp_dict))
    #                 if len(dummy_list) > max_length_this_level:
    #                     potential_LIS_this_level = [].append(dummy_list)
    #                     max_length_this_level = len(dummy_list)
    #                 elif len(dummy_list) == max_length_this_level:
    #                     potential_LIS_this_level.append(dummy_list)
    #                 else:
    #                     dummy_list = [j]

    def helper(L, sub, dp):
        # base case

        # memoization
        # all L with the same length should end up with the same sub value
        if dp[len(L)]:
            return dp[len(L)]

        max_sub = sub
        for i in range(len(L)):
            potential_max = []
            if (sub and L[i] >= sub[-1]) or not sub:  # only when the element is greater than or equal to the ending sub digit
                if i == len(L)-1:
                    potential_max = sub + [L[i]]
                else:
                    potential_max = helper(L[i+1:], sub+[L[i]], dp)  # each time, I add an element to the end, if applicable
            if len(potential_max) > len(max_sub):
                max_sub = potential_max
        dp[len(L)] = max_sub
        return max_sub

    dp = [None] * (len(L)+1)

    return helper(L, [], dp)


def LCS(s1, s2):
    """
    :param s1: A string
    :param s2: A string
    :return: Their longest common substring
    """

    def helper(s1, s2, dp):
        # Have two pointers, compare every single possible pair of characters. If equal, recursion starts for the two lists
        # after the two pointers.

        if not s1 or not s2:
            return ''

        # memoization
        if dp[len(s1)][len(s2)]:
            return dp[len(s1)][len(s2)]

        # base cases

        if len(s1) == 1:
            if s1 == s2[0]:
                return s1
            else:
                return ''
        elif len(s2) == 1:
            if s2 == s1[0]:
                return s2
            else:
                return ''

        if s1[0] == s2[0]:
            # if there are multiple matches, it is always a good idea to record the front match first
            # AND I should disregard all later options
            return s1[0] + helper(s1[1:], s2[1:], dp)  # no need to memoize this, as we'll never revisit this
        move_first = helper(s1[1:], s2, dp)
        move_second = helper(s1, s2[1:], dp)
        if len(move_first) > len(move_second):
            dp[len(s1)][len(s2)] = move_first
            return move_first
        else:
            dp[len(s1)][len(s2)] = move_second
            return move_second

    dp = [[None]*(len(s2)+1) for _ in range(len(s1)+1)]
    return helper(s1, s2, dp)


def rotate90(mat):
    """
    :param mat: A matrix
    :return: A matrix turned by 90 degrees in the clockwise direction
    """
    # return np.rot90(mat, 3)  # jk this is just for testing if the test cases are correct
    dimensions = np.shape(mat)
    output = np.zeros((dimensions[1], dimensions[0]))
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            # first row becomes last column, last row becomes first column
            output[j, dimensions[0]-i-1] = mat[i, j]
    return output


def chain_multiply(arr):
    """
    :param arr: A tensor with dimensions (n, n, d)
    :return: None, but arr should have in-place modification where each element is a multiplication of itself with all
             previous matrices
    """
    dimensions = np.shape(arr)
    for i in range(dimensions[2]):
        if i != 0:  # omit the first matrix
            arr[..., i] = multiply_matrices(arr[..., i-1], arr[..., i])


def num_stair_climbing(n, s):
    """
    :param n: The number of stairs to be climbed
    :param s: A list of step sizes, sorted
    :return: The number of different ways one could return for the given n and s
    """

    def helper(n, s, dp):
        # base case
        if n < 0:
            return 0
        # memoization
        if dp[n][len(s)]:
            return dp[n][len(s)]
        output = 0
        for i in range(1, len(s)+1):
            output += helper(n-i, s, dp)
        dp[n][len(s)] = output
        return output

    dp = [[None]*(len(s)+1) for _ in range(n+1)]
    dp[0] = [1] * (len(s)+1)
    return helper(n, s, dp)





if __name__ == "__main__":
    # print(LIS([-5, 2, 3, 6, 19, 2, 3, 9, 18, 21]))
    print(LIS([1, -1, 1, 0, 3]))