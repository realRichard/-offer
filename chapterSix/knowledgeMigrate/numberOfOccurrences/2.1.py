'''
题目：
    在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。
    请找出那个只出现一次的数字。
'''


def number_appearing_once(arr):
    bit_sum = [0] * 32
    for i in arr:
        bit_mask = 1
        for j in range(32):
            bit = i & bit_mask
            if bit != 0:
                bit_sum[j] += 1
            bit_mask = bit_mask << 1
    once = 0
    for i, bit in enumerate(bit_sum):
        if bit % 3 != 0:
            once += 1 << i
    return once


def test():
    arr = [0, 1, 1, 1, 3, 3, 3]
    print(number_appearing_once(arr))
    arr1 = [1, 1, 1, 3, 3, 3, 8]
    print(number_appearing_once(arr1))


if __name__ == '__main__':
    test()