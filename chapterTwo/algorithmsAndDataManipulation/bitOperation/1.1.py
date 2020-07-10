'''
题目：
请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如，把9表示成二进制是1001，有2位是1,。因此，如果输入9，
则该函数输出2。
'''


# def number_of_one(n):
#     if not isinstance(n, int):
#         raise TypeError

#     count = 0
#     i = 0
#     temp = 2 ** i
#     while temp <= n:
#         if n & temp:
#             count += 1
#         i += 1
#         temp = 2 ** i
#     return count


def number_of_one(n):
    if not isinstance(n, int):
        raise TypeError

    count = 0
    temp = 1
    while temp <= n:
        if n & temp:
            count += 1
        temp = temp << 1
    return count


def test():
    print('9', number_of_one(9))
    print('7', number_of_one(7))
    print('15', number_of_one(15))
    print('31', number_of_one(31))
    print('0x7FFFFFFF', number_of_one(0x7FFFFFFF))
    print('0xFFFFFFFF', number_of_one(0xFFFFFFFF))


if __name__ == '__main__':
    test()