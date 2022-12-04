# I traverse through the string, starting with the most significant digit.
# When I move to the next digit, I first multiply the existing value with base value,
# then add new digit value to the existing value.
def base_q_to_decimal(s, q):
    """
    :param s: string s is a base q representation of an integer
    :param q: an integer obeying 1<q<=10 representing input base value
    :return: the corresponding decimal integer
    """
    output = 0
    for digit in s:
        output *= q
        output += int(digit)
    return output


# I first convert a base q number into a decimal number using base_q_to_decimal(s, q),
# then dividing the decimal number with p, find the remainder and store into list, finally
# reverse a list once to get the base p number.
def base_q_to_p(s, q, p):
    """
    :param s: string s is a base q representation of an integer
    :param q: an integer obeying 1<q<=10 representing input base value
    :param p: an integer obeying 1<q<=10 representing output base value
    :return: the corresponding string representation of the base p integer
    """
    if s == '0':
        return s
    output = []
    decimal = base_q_to_decimal(s, q)
    while decimal > 0:
        output.append(str(decimal % p))
        decimal = decimal // p
    return "".join(output[::-1])


# I ran the loop that compares the first element in each list and adds to output and move the pointer of the
# added item's list by 1. I then append l1 if there are elements in l1 left, and append l2 if there are elements
# in l2 left.
def sorted_merge(l1, l2):
    """
    :param l1: A list that is sorted in non-decreasing order
    :param l2: A list that is sorted in non-decreasing order
    :return: A sorted list joining l1 and l2
    """
    output = []
    l1_ptr = 0
    l2_ptr = 0
    # run the loop until one loop reaches the end
    while l1_ptr < len(l1) and l2_ptr < len(l2):
        if l1[l1_ptr] >= l2[l2_ptr]:
            output.append(l2[l2_ptr])
            l2_ptr += 1
        else:
            output.append(l1[l1_ptr])
            l1_ptr += 1
    # append l1 at the end if l1 is not empty
    while l1_ptr < len(l1):
        output.append(l1[l1_ptr])
        l1_ptr += 1
    # append l2 at the end if l2 is not empty
    while l2_ptr < len(l2):
        output.append(l2[l2_ptr])
        l2_ptr += 1
    return output


# I first copied l_multiple into a list of lists, in preparation to modify elements within the lists.
# For each loop, I find out the minimum number at the front of each list, remove from list and add to output.
# While loop ends when there is no element left in all lists.
def multiple_sorted_merge(l_multiple):
    """
    :param l_multiple: A list of sorted lists
    :return: A sorted list joining all lists in args
    """
    output = []
    lists = l_multiple  # I copied a list here to avoid modifying inputs. Because of this, I don't have to use pointers
    # Remove empty lists beforehand
    for ints in lists:
        if not ints:
            lists.remove(ints)
    # The loop exits when all elements within a list are sorted
    while lists:
        min_this_iteration = lists[0][0]
        min_index = 0
        for i in range(len(lists)):
            if lists[i][0] < min_this_iteration:
                min_this_iteration = lists[i][0]
                min_index = i
        output.append(lists[min_index].pop(0))  # Append the smallest element while also removing it from original list

        if not lists[min_index]:
            lists.remove(lists[min_index])
    return output


# I ran a while loop that searches for root starting from 0, stopping at square root of x.
# For each iteration, I seek if the element is a root of power from 2 to 5.
def find_root(x):
    """
    :param x: An integer to be found what is its root with the largest power
    :return: A tuple (root, pwr) that describes the root with the largest power of x, 1 < pwr < 6.
             If there is no root, return False.
    """
    i = 0
    while i * i <= x:
        # The following loop tests for powers from 2 to 5,
        # I reversed it to ensure solution with largest power is returned
        for j in range(2, 6)[::-1]:
            if i ** j == x:
                return i, j
        i += 1
    return False


# This is a helper function
def factorize(num):
    """
    :param num: The integer to be factorized
    :return: A list of factors of num
    """
    output = []
    running_num = num
    i = 2
    # first while loop iterates through integers smaller than or equal to running_num
    while i <= running_num:
        # inner while loop divides until num cannot be divided anymore
        while running_num % i == 0:
            running_num /= i
            output.append(i)
        i += 1
    return output


# I first generated a list of factors, then for each iteration, I determine the factor to remove from lists' fronts,
# and multiply to output. When all factors are processed, the function ends.
def least_common_multiple(*args):
    """
    :param args: Numbers to have their lcm.py being found
    :return: An integer representing the lcm.py of all inputs
    """
    output = 1
    lists_of_factors = [factorize(i) for i in args]
    # Get factor_this_iteration, which is the smallest of all front elements, then remove all front elements with
    # the same factor
    while lists_of_factors:
        factor_this_iteration = lists_of_factors[0][0]
        # Determine the factor of this iteration
        for i in range(len(lists_of_factors)):
            if lists_of_factors[i][0] < factor_this_iteration:
                factor_this_iteration = lists_of_factors[i][0]
        # Remove elements containing factor_this_iteration at front
        # I use while loop here because I need to remove elements within the loop
        i = 0
        while i < len(lists_of_factors):
            if lists_of_factors[i][0] == factor_this_iteration:
                lists_of_factors[i].pop(0)
                # Removes list if list is empty
                if not lists_of_factors[i]:
                    lists_of_factors.pop(i)
                    continue
            i += 1

        output *= factor_this_iteration
    return output


# This function is almost identical to the lcm.py function, except that I have added a counter to ensure that
# only when all lists of factors contain the same factor, the output will be multiplied by the factor
def greatest_common_divisor(*args):
    """
    :param args: Numbers to have their gcd being found
    :return: An integer representing the gcd of all inputs
    """
    output = 1
    lists_of_factors = [factorize(i) for i in args]
    # Get factor_this_iteration, which is the smallest of all front elements, then remove all front elements with
    # the same factor
    while lists_of_factors:
        factor_this_iteration = lists_of_factors[0][0]
        # Determine the factor of this iteration
        for i in range(len(lists_of_factors)):
            if lists_of_factors[i][0] < factor_this_iteration:
                factor_this_iteration = lists_of_factors[i][0]
        # Remove elements containing factor_this_iteration at front
        # I use while loop here because I need to remove elements within the loop
        i = 0
        count = 0
        while i < len(lists_of_factors):
            if lists_of_factors[i][0] == factor_this_iteration:
                lists_of_factors[i].pop(0)
                count += 1
                # Removes list if list is empty
                if not lists_of_factors[i]:
                    lists_of_factors.pop(i)
                    continue
            i += 1

        # Only if all lists contain the same factor will the output be multiplied by factor
        if count == len(args):
            output *= factor_this_iteration
    return output


# I added all elements into a set, then output the converted list version of the set
def unique_values(L):
    """
    :param L: A list of lists containing unordered integers
    :return: A list of unique integers from L
    """
    output = set()
    for ints in L:
        for i in ints:
            output.add(i)
    return list(output)
