def ugly_number(n):
    if not isinstance(n, int):
        raise TypeError
    if n <= 0:
        raise ValueError

    ugly_numbers = [1] * n
    index = 1
    multiple_2 = 0
    multiple_3 = 0
    multiple_5 = 0
    while index < n:
        ugly_numbers[index] = min(ugly_numbers[multiple_2] * 2, ugly_numbers[multiple_3] * 3, ugly_numbers[multiple_5] * 5)
        while ugly_numbers[multiple_2] * 2 <= ugly_numbers[index]:
            multiple_2 += 1
        while ugly_numbers[multiple_3] * 3 <= ugly_numbers[index]:
            multiple_3 += 1
        while ugly_numbers[multiple_5] * 5 <= ugly_numbers[index]:
            multiple_5 += 1
        index += 1
    return ugly_numbers[-1]


def test():
    print(ugly_number(1))
    print(ugly_number(2))
    print(ugly_number(10))
    print(ugly_number(20))
    print(ugly_number(1000))
    print(ugly_number(1500))


if __name__ == '__main__':
    test()