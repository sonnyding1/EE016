def find_max(L):
    max = L[0]
    for i in L:
        if i > max:
            max = i
    return max


def find_even(*args):
    output = []
    for i in args:
        if i % 2 == 0:
            output.append(i)
    return output