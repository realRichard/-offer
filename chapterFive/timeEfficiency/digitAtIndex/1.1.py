'''
题目：
    数字以0123456789101112131415……的格式序列化到一个字符串序列中。
    在这个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。
    请写一个函数，求任意第n位对应的数字。
'''


def count_bit(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


def digit_bit(num, index):
    count = count_bit(num)
    b = count - index
    while b >= 0:
        b -= 1
        num %= 10
    return num


def digit_at_index(n):
    count = 0
    i = 0
    while count < n:
        i += 1
        count += count_bit(i)
    index = count - n
    return digit_bit(i, index)


def test():
    print(digit_at_index(0))
    print(digit_at_index(5))
    print(digit_at_index(13))
    print(digit_at_index(19))


if __name__ == '__main__':
    test()