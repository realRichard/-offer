'''
说明：
数学思想，当n>=5时，2(n-2)>n并且3(n-3)>n，而且3(n-3) >= 2(n-2)，
所以尽可能多剪长度为3的绳子。如果长度为4的时候，2*2>3*1，所以4的时候就剪成2*2的两段。
'''


# 贪婪算法
def max_product_after_cutting(length):
    if not isinstance(length, int):
        raise TypeError

    if length < 2:
        return 0
    elif length == 2:
        return 1
    elif length == 3:
        return 2

    times_of_three = length // 3
    if length - times_of_three * 3 == 1:
        times_of_three -= 1
    times_of_two = (length - times_of_three * 3) // 2
    return (3 ** times_of_three) * (2 ** times_of_two)


def test():
    print('8', max_product_after_cutting(8))
    print('3', max_product_after_cutting(3))


if __name__ == '__main__':
    test()
