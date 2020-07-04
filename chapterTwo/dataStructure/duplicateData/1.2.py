from utils import (
    log,
    ensure,
)


# 利用哈希表解决，无需修改原数组，时间 O(n) 空间 O(n)
def duplicate(arr):
    if not isinstance(arr, list):
        return (False,)

    length = len(arr)
    for i in arr:
        if not isinstance(i, int) or i < 0 or i > length - 1:
            return (False,)

    div = {}
    for i in arr:
        if div.get(i) is None:
            div[i] = 1
        else:
            return (True, i)
    return (False,)


def test():
    arr1 = [2, 3, 1, 0, 2, 5, 3]
    ensure((True, 2) == duplicate(arr1), 'arr1')


if __name__ == '__main__':
    test()