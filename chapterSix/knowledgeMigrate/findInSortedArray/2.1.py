'''
题目:
    一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0~n-1之内。
    在范围0~n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
'''


# time O(n), sum
def missing_number(arr):
    n = len(arr)
    expected_sum = n * (1 + n) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


def test():
    arr1 = [0, 1, 2, 3, 4, 5, 6]
    print(missing_number(arr1))
    arr2 = [1, 2, 3, 4, 5, 6]
    print(missing_number(arr2))
    arr2 = [0, 1, 2, 4, 5, 6]
    print(missing_number(arr2))


if __name__ == '__main__':
    test()