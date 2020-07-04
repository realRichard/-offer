'''
在一个长度为n+1的数组里的所有数字都在1-n的范围内，所以数组中至少有一个数字是重复的，请找出数组中任意一个重复的数字，
但不能修改输入的数组，例如，如果输入长度为 8 的数组 [ 2, 3, 5, 4, 3, 2, 6, 7 ] 那么对应的输出是重复的数字2或者3
'''


from utils import (
    log,
    ensure,
)


# 创建一个长度为n+1的辅助数组，然后逐一把原数组的每个数字复制到辅助数组。如果原数组中被复制的数字是m，则把它复制
# 到辅助数组中下标为m的位置。这样很容易发现哪个数字是重复的。
# 空间O(n)
def duplicate(arr):
    if not isinstance(arr, list):
        return (False,)

    length = len(arr)
    if length == 0:
        return (False,)
    for i in arr:
        if not isinstance(i, int) or i < 1 or i > length - 1:
            return (False,)
    auxiliary_arr = [0 for i in range(length)]
    for i, x in enumerate(arr):
        if auxiliary_arr[arr[i]] == arr[i]:
            return (True, arr[i])
        else:
            auxiliary_arr[arr[i]] = arr[i]
        log(auxiliary_arr)
    return (False,)


def test():
    # test case,
    arr1 = [2, 3, 5, 4, 3, 2, 6, 7]
    arr2 = [5, 4, 3, 2, 1, 0]
    arr3 = [1, 2, 3, 4, 3]
    arr4 = []
    result1 = duplicate(arr1)
    ensure(result1[0] == True and result1[1] in (2, 3), 'arr1')
    result2 = duplicate(arr2)
    ensure(result2[0] == False, 'arr2')
    result3 = duplicate(arr3)
    ensure(result3[0] == True and result3[1] in (3,), 'arr3')
    result4 = duplicate(arr4)
    ensure(result4[0] == False, 'arr4')


if __name__ == '__main__':
    test()