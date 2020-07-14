import sys
print('recursionlimit', sys.getrecursionlimit())


def power_core(base, exponent):
    if exponent == 1:
        return base

    result = 1
    # if exponent % 2 == 0:
    #     result = power_core(base, exponent >> 1)
    #     return result * result
    # else:
    #     result = power_core(base, (exponent - 1) >> 1)
    #     return base * result * result
    result = power_core(base, exponent >> 1)
    result *= result
    # 判断奇偶
    if exponent & 0x1 == 1:
        result *= base
    return result


def power(base, exponent):
    if not isinstance(base, float):
        raise TypeError
    if not isinstance(exponent, int):
        raise TypeError

    if exponent == 0:
        return 1
    elif base == 0:
        return base

    result = power_core(base, abs(exponent))
    if exponent > 0:
        return result
    else:
        return 1 / result


def test():
    print(pow(0, 0))
    print(power(0.0, 1))
    print(power(10.0, -1))
    print(power(2.0, 2))
    print(power(2.0, 10))


if __name__ == '__main__':
    test()