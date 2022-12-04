import math
import random


# Firstly, I split the string into many smaller parts. Then, I set the output as a char array, which is
# then modified as I analyze each substring with dictionaries. Finally, I join output together, and
# convert into int to remove the leading zeroes.
def string2int(s):
    """
    :param s: A string representing an integer that is positive and less than 1,000,000
    :return: s's integer representation
    """
    string2int_pwr0 = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    string2int_ten_to_nineteen = {
        'ten': '10',
        'eleven': '11',
        'twelve': '12',
        'thirteen': '13',
        'fourteen': '14',
        'fifteen': '15',
        'sixteen': '16',
        'seventeen': '17',
        'eighteen': '18',
        'nineteen': '19'
    }
    string2int_twenty_to_ninty = {
        'twenty': '2',
        'thirty': '3',
        'forty': '4',
        'fifty': '5',
        'sixty': '6',
        'seventy': '7',
        'eighty': '8',
        'ninty': '9'
    }

    output = ['0'] * 6  # 000000
    if 'thousand' in s:
        thousand_text, text = s.split('thousand')
    else:
        thousand_text = ''
        text = s

    if 'hundred' in thousand_text:
        thousand_hundred, thousand_tens = thousand_text.split('hundred')
    else:
        thousand_hundred = ''
        thousand_tens = thousand_text

    if 'hundred' in text:
        hundred, tens = text.split('hundred')
    else:
        hundred = ''
        tens = text

    for i in string2int_ten_to_nineteen:
        # translate thousand_tens
        if thousand_tens == i:
            output[1] = string2int_ten_to_nineteen[i]
            output[2] = ''  # empty string because 11-19 have 2 digits
            thousand_tens = ''  # empty string to avoid the following condition checks
        # translate tens
        if tens == i:
            output[4] = string2int_ten_to_nineteen[i]
            output[5] = ''
            tens = ''

    for i in string2int_twenty_to_ninty:
        # translate thousand_tens and process string
        if thousand_tens.find(i) == 0:
            output[1] = string2int_twenty_to_ninty[i]
            thousand_tens = thousand_tens[len(i):]
        # translate tens and process string
        if tens.find(i) == 0:
            output[4] = string2int_twenty_to_ninty[i]
            tens = tens[len(i):]

    for i in string2int_pwr0:
        # translate thousand_hundred
        if thousand_hundred == i:
            output[0] = string2int_pwr0[i]
        # translate thousand_tens
        if thousand_tens == i:
            output[2] = string2int_pwr0[i]
        # translate thousand_hundred
        if hundred == i:
            output[3] = string2int_pwr0[i]
        # translate tens
        if tens == i:
            output[5] = string2int_pwr0[i]

    output_string = ''.join(output)
    output_int = int(output_string)  # remove leading zeroes at the same time
    return output_int


# I used a helper function that accepts a list of characters to be used, and a work-in-progress permutation string.
# For each iteration, I call helper function that calls more helper functions, these functions only return when
# the permutation string is complete. I used many optimization methods, including using dictionary instead of
# list to reduce item search time, let each dp_list only store substrings from the same level to reduce memory usage.
def permutation(s):
    """
    :param s: A string
    :return: A list of all permutations of s
    """

    def permutation_helper(s, text, dp_dict):
        """
        :param s: The input string
        :param text: The permutation text in progress
        :param dp_dict: The dictionary used to store already completed items to prevent duplicate calculations
        :return: A list of palindromes
        """
        # prune the tree if already visited
        if text in dp_dict:
            return []
        else:
            dp_dict[text] = ''
        output = []
        # when the text is complete, return in a list
        if len(s) == 1:
            return [text + s]

        dp_dict_next_level = {}  # each dp_dict only stores occurred sequences of this level
        for i in range(len(s)):
            # call helper function with one char removed from chars, the same char is appended to s
            text_next_recursion = permutation_helper(s[:i]+s[i+1:], text + s[i], dp_dict_next_level)
            # text_next_recursion may be an empty list (pruned), in this case ignore
            if text_next_recursion:
                output.extend(text_next_recursion)
        return output

    return permutation_helper(s, '', {})


# I implemented a traditional merge sort, except that instead of comparing two numbers, I wrote a for loop for each
# string comparison that loops through each character and compare them and decide which string is larger.
# But merge sort is too slow, I implemented a bucket sort recursion method that sorts strings into their corresponding
# alphabet buckets for each iteration.
def sort_string(L):
    """
    :param L: A list of strings to be sorted alphabetically
    :return: The sorted list
    """
    # # chars are ASCII ints, so it is legal for me to directly compare chars
    # # I will use merge sort for my sorting algorithm
    # if len(L) <= 1:
    #     return L
    # half = int(len(L) / 2)
    # left = L[:half]
    # left = sort_string(left)
    # right = L[half:]
    # right = sort_string(right)
    #
    # left_ptr = 0
    # right_ptr = 0
    # wip_list = [''] * len(L)
    # cur = 0  # current index at wip_list
    # while left_ptr < len(left) and right_ptr < len(right):
    #     # Here, I compare character by character. chars are ASCII ints, so it is legal for me to directly compare chars.
    #     for i in range(min(len(left[left_ptr]), len(right[right_ptr]))):
    #         if left[left_ptr][i] < right[right_ptr][i]:
    #             wip_list[cur] = left[left_ptr]
    #             left_ptr += 1
    #             break  # break because no need to look at characters afterwards
    #         elif left[left_ptr][i] > right[right_ptr][i]:
    #             wip_list[cur] = right[right_ptr]
    #             right_ptr += 1
    #             break
    #         else:  # when two strings have the same character at the same position, do more comparisons
    #             # if at the end of comparison, choose the string that is shorter
    #             if i == min(len(left[left_ptr]), len(right[right_ptr])) - 1 and len(left[left_ptr]) > len(
    #                     right[right_ptr]):
    #                 wip_list[cur] = right[right_ptr]
    #                 right_ptr += 1
    #             elif i == min(len(left[left_ptr]), len(right[right_ptr])) - 1 \
    #                     and len(left[left_ptr]) <= len(right[right_ptr]):
    #                 wip_list[cur] = left[left_ptr]
    #                 left_ptr += 1
    #             # if not, nothing happens, next comparison will be executed
    #     cur += 1
    # # if left is not empty, add everything to the end
    # while left_ptr < len(left):
    #     wip_list[cur] = left[left_ptr]
    #     left_ptr += 1
    #     cur += 1
    # # if right is not empty, add everything to the end
    # while right_ptr < len(right):
    #     wip_list[cur] = right[right_ptr]
    #     right_ptr += 1
    #     cur += 1
    #
    # return wip_list

    # I will use a bucket sort like sorting method, sorting strings into their alphabet buckets
    def sort_string_helper(L):
        alphabet_buckets = {
            'a': [],
            'b': [],
            'c': [],
            'd': [],
            'e': [],
            'f': [],
            'g': [],
            'h': [],
            'i': [],
            'j': [],
            'k': [],
            'l': [],
            'm': [],
            'n': [],
            'o': [],
            'p': [],
            'q': [],
            'r': [],
            's': [],
            't': [],
            'u': [],
            'v': [],
            'w': [],
            'x': [],
            'y': [],
            'z': []
        }
        empty_string_count = L.count('')
        L = [i for i in L if i != '']
        output = [''] * empty_string_count
        if len(L) == 2:
            for i in range(min(len(L[0]), len(L[1]))):
                if L[0][i] < L[1][i]:
                    output.append(L[0])
                    output.append(L[1])
                    return output
                elif L[0][i] > L[1][i]:
                    output.append(L[1])
                    output.append(L[0])
                    return output
                else:
                    if i == min(len(L[0]), len(L[1])):
                        if len(L[0]) < len(L[1]):
                            output.append(L[0])
                            output.append(L[1])
                            return output
                        else:
                            output.append(L[1])
                            output.append(L[0])
                            return output
        for element in L:
            alphabet_buckets[element[0]].append(element)
        for strings_next_iter in alphabet_buckets.values():
            # if there are more than 1 string, and the strings don't contain duplicates only
            if len(strings_next_iter) > 1 and len(set(strings_next_iter)) != 1:
                first_alphabet = strings_next_iter[0][0]
                strings_next_iter = sort_string_helper([s[1:] for s in strings_next_iter])
                for i in range(len(strings_next_iter)):
                    strings_next_iter[i] = first_alphabet + strings_next_iter[i]
            output.extend(strings_next_iter)
        return output

    return sort_string_helper(L)


# I traverse through L using a cur index, for each iteration, I compare integer at cur and integer at cur-1,
# if not strictly increasing, replace the indices of historically highest subsequence with a newer one.
# If at the end of list, perform a same condition check.
def longest_increasing_subseq(L):
    """
    :param L: A list of integers
    :return: The longest strictly increasing sequence of L as a list
    """
    streak = [0] * len(L)
    max_streak_index = 0
    max_streak_begin_index = 0
    streak_break_index = 0
    for i in range(1, len(L)):
        if L[i-1] < L[i]:
            streak[i] = streak[i-1] + 1
            if streak[i] > streak[max_streak_index]:
                max_streak_index = i
                max_streak_begin_index = streak_break_index
        else:
            streak_break_index = i
    return L[max_streak_begin_index:max_streak_index+1]


# Bisection search but returns rank when x is found
def rank_in_sorted_list(L, x):
    """
    :param L: A sorted list of integers
    :param x: The integer value to be evaluated
    :return: The rank of x, which is the number of integers in L that are strictly greater than x
    """
    if not L:
        return 0
    # I will use bisection search for this problem, calculating the rank while searching
    start = 0
    end = len(L)
    mid = 0
    while end > start:
        mid = (start + end) // 2  # if L has odd elements, mid is true middle point; else mid leans slightly to right
        # the fact that mid is floor division also implies mid is strictly less than end, so end changes every iteration
        if x > L[mid]:
            start = mid + 1
        elif x < L[mid]:
            end = mid
        else:
            return len(L)-mid-1  # TODO: flaw, what if [1, 2, 3, 3, 3, 3, 4, 5], x=3? + or - a very small delta value
    if end == 0:
        return len(L)
    else:
        return 0
    # return len(L)-mid-1


# Firstly I tried BFS, but that is too time consuming. I tried to prevent branching by limiting actions to take when
# x is smaller than value at a point and when x is larger than value at a point each to only 1 operation, I do this
# by starting at top right corner. When we want to go beyond edges, we know x is not in L.
def search_sorted_matrix(L, x):
    """
    :param L: A sorted matrix of integers. By sorted, we mean that L[i1][i_2] <= L[j1][j2] for j1 >= i1 and j2 >= i2.
    :param x: The number to be found
    :return: A list [i, j] representing coordinate of the number x. If there are multiple, return any index.
             If there are none, return [1, 1].
    """
    # this is like a gradient diagonally... Which means that binary search probably won't work.

    # # if empty list, return [-1, -1]
    # if not L:
    #     return [-1, -1]
    # if not L[0]:
    #     return [-1, -1]
    # # finds middle point
    # i = len(L) // 2
    # j = len(L[0]) // 2
    #
    # # matrix records if the square is already checked
    # is_checked = [[False for j in range(len(L[0]))] for i in range(len(L))]
    #
    # # BFS, it was fun coding it, but slow af
    # queue = [[i, j]]
    # while queue:
    #     i, j = queue.pop(0)
    #     is_checked[i][j] = True
    #     if x == L[i][j]:
    #         return [i, j]
    #     elif x < L[i][j]:
    #         if i > 0 and j > 0 and not is_checked[i-1][j-1]:
    #             queue.append([i-1, j-1])  # top left
    #         if i > 0 and not is_checked[i-1][j]:
    #             queue.append([i-1, j])  # top
    #         if j > 0 and not is_checked[i][j-1]:
    #             queue.append([i, j-1])  # left
    #     elif x > L[i][j]:
    #         if i < len(L)-1 and j < len(L[0])-1 and not is_checked[i+1][j+1]:
    #             queue.append([i+1, j+1])  # bottom right
    #         if i < len(L)-1 and not is_checked[i+1][j]:
    #             queue.append([i+1, j])  # bottom
    #         if j < len(L[0])-1 and not is_checked[i][j+1]:
    #             queue.append([i, j+1])  # right
    # return [-1, -1]

    # This time, I will start searching from top right corner. The main advantage is there is NO BRANCHING.
    # def search_sorted_matrix_helper(L, x, i, j):
    #     if L[i][j] == x:  # if equal, return coordinate
    #         return [i, j]
    #     elif L[i][j] > x:  # if x is smaller, go left
    #         if j == 0:  # if we cannot go left, x not in L
    #             return [-1, -1]
    #         else:
    #             return search_sorted_matrix_helper(L, x, i, j-1)
    #     elif L[i][j] < x:  # if x is larger, go down
    #         if i == len(L)-1:  # if we cannot go down, x not in L
    #             return [-1, -1]
    #         else:
    #             return search_sorted_matrix_helper(L, x, i+1, j)
    #
    # return search_sorted_matrix_helper(L, x, 0, len(L[0])-1)

    # there is no need to use recursion if there is no branching at all
    i = 0
    j = len(L[0])-1
    while i <= len(L) - 1 and j >= 0:
        if L[i][j] == x:
            return [i, j]
        elif L[i][j] > x:
            j -= 1
        elif L[i][j] < x:
            i += 1
    return [-1, -1]  # when we try to go beyond the edge, we know x not in L


# I first calculated all coordinates' distances from origin, then added coordinates that are less than kth closest
# to the origin using quick select.
def closest_k_points(L, k):
    """
    :param L: A list of lists [i, j] representing coordinates
    :param k: The k the closest points to origin to return
    :return: A list of k lists [i, j] representing coordinates closest to the origin
    """
    if not L:
        return []

    output = []

    distances: list = [0] * len(L)
    for i in range(len(L)):
        distances[i] = math.sqrt(L[i][0] ** 2 + L[i][1] ** 2)

    # selects the ith most small distance
    for i in range(1, min(k + 1, len(L) + 1)):
        output.append(L[distances.index(quick_select(distances, i))])
    return output


# This is just a helper function of closest_k_points(), finds the kth smallest element in list
def quick_select(L, k):
    pivot = L[random.randrange(len(L))]
    l_large, l_small, l_equal = [], [], []
    for element in L:
        if element > pivot:
            l_large.append(element)
        elif element < pivot:
            l_small.append(element)
        else:
            l_equal.append(element)

    # if there are more than or equal to k elements in l_small, search in l_small
    if k <= len(l_small):
        return quick_select(l_small, k)
    # if there are exactly k - 1 numbers smaller than pivot, then pivot must be the kth smallest number
    elif k - len(l_small) <= len(l_equal):
        return pivot
    # if there are less than k elements in l_small, and
    else:
        return quick_select(l_large, k - len(l_small) - len(l_equal))


# I have tried using quick select, but it turned out the function still took too long to run.
# That's why I used bucket sort. I run a for loop that records the amount of occurrences of numbers according
# to their indices, such that I don't have to actually search for each specific elements' indices.
# If I were to use quick select, assuming quick select is O(n), the worst run time of h_index() is O(n^2). Terrible.
def h_index(L):
    """
    :param L: An unsorted list of non-negative integers
    :return: An integer h such that there are at least h elements in L that are larger than or equal to h
    """
    # if not L:
    #     return 0
    # h = min(max(L), len(L))  # start with largest h index, all the way to 0
    # while h > 0:
    #     if quick_select(L, len(L) - h + 1) >= h:  # quick_select hth biggest element, if >= h, return h index
    #         return h
    #     h -= 1
    # return 0

    buckets = [0] * (len(L) + 1)
    for element in L:
        if element > len(L):
            buckets[len(L)] += 1
        elif element < 0:
            buckets[0] += 1
        else:
            buckets[element] += 1

    count = 0
    for i in range(len(buckets)-1, -1, -1):  # start from the largest index for the highest h index possible
        count += buckets[i]
        if count >= i:
            return i
