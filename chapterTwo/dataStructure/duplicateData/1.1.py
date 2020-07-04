'''
在一个长度为 n 的数组里有所有数字都在 0 ~ n - 1 的范围内，数组中某些数字是重复的，但不知道有几个数字重复了,
也不知道每个数字重复了几次，请找出数组中任意一个重复的数字，例如，如果输入长度为 7 的数组 [ 2, 3, 1, 0, 2, 5, 3 ]，
那么对应的输出是重复的数字 2 或者 3
'''


from utils import (
    log,
    ensure,
)


# 对原数组进行排序然后顺序查找，时间 O(nlogn) 空间 O(1)
def duplicate(arr):
    if not isinstance(arr, list):
        return (False,)

    length = len(arr)
    for i in arr:
        if not isinstance(i, int) or i < 0 or i > length - 1:
            return (False,)

    # log('sort before', arr)
    arr.sort()
    # log('sort after', arr)
    for i, x in enumerate(arr):
        if arr[i] == arr[i + 1]:
            return (True, arr[i])
    return (False)


def test():
    arr1 = [2, 3, 1, 0, 2, 5, 3]
    ensure((True, 2) == duplicate(arr1), 'arr1')


if __name__ == '__main__':
    test()