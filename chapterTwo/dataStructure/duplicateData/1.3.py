from utils import (
    log,
    ensure,
)


# 交换原数组中的元素，时间 O(n) 空间 O(1)
def duplicate(arr):
    if not isinstance(arr, list):
        return (False,)

    length = len(arr)
    if length == 0:
        return (False,)
    for i in arr:
        if not isinstance(i, int) or i < 0 or i > length - 1:
            return (False,)

    for i, x in enumerate(arr):
        while i != arr[i]:
            log(i, arr)
            if arr[i] == arr[arr[i]]:
                return (True, arr[i])
            else:
                # write the following code, causing infinite loop
                # arr[i], arr[arr[i]] = arr[arr[i]], arr[i]
                temp = arr[i]
                # arr[i] = arr[temp]
                # arr[temp] = temp
                arr[i], arr[temp] = arr[temp], arr[i]
    return (False,)


def test():
    # test case,
    arr1 = [2, 3, 1, 0, 2, 5, 3]
    arr2 = [5, 4, 3, 2, 1, 0]
    arr3 = [12, 3]
    arr4 = []
    ensure((True, 2) == duplicate(arr1), 'arr1')
    ensure((False,) == duplicate(arr2), 'arr2')
    ensure((False,) == duplicate(arr3), 'arr3')
    ensure((False,) == duplicate(arr4), 'arr4')


if __name__ == '__main__':
    test()