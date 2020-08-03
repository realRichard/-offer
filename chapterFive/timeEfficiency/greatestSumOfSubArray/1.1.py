'''
题目：
    输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。
    求所有子数组的和的最大值。要求时间复杂度为O(n)。
'''


def greatest_sum_of_subArray(arr):
    if not isinstance(arr, list):
        raise TypeError
    for i in arr:
        if not isinstance(i, int):
            raise ValueError

    greatest_sum = 0
    continuous_sum = 0
    for i in arr:
        continuous_sum += i
        if continuous_sum < 0:
            continuous_sum = 0
        if continuous_sum > greatest_sum:
            greatest_sum = continuous_sum
    return greatest_sum


def test():
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    print(greatest_sum_of_subArray(arr))


if __name__ == '__main__':
    test()