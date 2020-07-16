'''
题目：
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
    使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
'''


def reorder_odd_even(arr):
    if not isinstance(arr, list):
        raise TypeError
    for i in arr:
        if not isinstance(i, int):
            raise ValueError

    length = len(arr)
    if length == 0:
        return 
    begin = 0
    end = length - 1
    while begin < end:
        while arr[begin] & 0x1 == 1:
            begin += 1
        while arr[end] & 0x1 != 1:
            end -= 1
        if begin < end:
            arr[begin], arr[end] = arr[end], arr[begin]


def test():
    arr = [1, 3, 2, 4, 5, 11]
    reorder_odd_even(arr)
    print(arr)


if __name__ == '__main__':
    test()