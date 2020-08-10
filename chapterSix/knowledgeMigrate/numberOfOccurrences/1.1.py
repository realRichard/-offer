'''
题目：
    一个整型数组里除了两个数字之外，其他的数字都出现了两次。
    请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
'''


def find_first_bit_is_one(n):
    index = 0
    while n & 1 == 0:
        n = n >> 1
        index += 1
    return index


def is_bit_one(i, index):
    i = i >> index
    return i & 1


def find_nums_appear_once(arr):
    result_exclusive_or = 0
    for i in arr:
        result_exclusive_or ^= i
    index_of_one = find_first_bit_is_one(result_exclusive_or)
    num1 = 0
    num2 = 0
    for i in arr:
        if is_bit_one(i, index_of_one):
            num1 ^= i
        else:
            num2 ^= i
    return (num1, num2)


def test():
    arr = [2, 4, 3, 6, 3, 2, 5, 5]
    print(find_nums_appear_once(arr))


if __name__ == '__main__':
    test()