def least_common_multiple(*args):
    nums = []
    lcm = 1
    for i in args:
        nums.append(i)

    master_list = []
    for i in range(len(nums)):
        x = []
        for j in range(2, nums[i]):
            while nums[i] % j == 0:
                if nums[i] % j == 0:
                    x.append(j)
                    nums[i] = nums[i]//j
            if nums[i] == 1:
                break
        master_list.append(x)
    #return master_list

    while master_list:
        num = 0
        x=0
        for i in master_list:
            if x > i[0]:
                x = i[0]

        for i in master_list:
            if num < i.count(x):
                num = i.count(x)

        lcm *= x ** num

        for i in master_list:
            for j in i:
                if j == x:
                    i.remove(j)
                    if not i:
                        master_list.remove(i)
    return lcm


def test_lcm():
    assert least_common_multiple(2, 4, 6) == 12