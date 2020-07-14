'''
题目：
    给定一个double类型的浮点数base和int类型的整数exponent。
    求base的exponent次方。不得使用库函数，同时不需要考虑最大数问题。
'''


def power(base, exponent):
    if not isinstance(base, float):
        raise TypeError
    if not isinstance(exponent, int):
        raise TypeError

    if exponent == 0:
        return 1
    elif base == 0:
        return base

    result = 1
    for i in range(abs(exponent)):
        result *= base
    if exponent > 0:
        return result
    else:
        return 1 / result


def test():
    print(pow(0, 0))
    print(power(0.0, 1))
    print(power(10.0, -1))
    print(power(2.0, 10))


if __name__ == '__main__':
    test()