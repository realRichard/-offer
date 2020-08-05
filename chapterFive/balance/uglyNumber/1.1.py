'''
题目：
    我们把只包含因子2、3和5的数称作丑数（Ugly Number）。求按从小到大的顺序的第N个丑数。
    例如6、8都是丑数，但14不是，因为它包含因子7。习惯上我们把1当做是第一个丑数。
'''


def is_ugly(n):
    while n % 2 == 0:
        n /= 2
    while n % 3 == 0:
        n /= 3
    while n % 5 == 0:
        n /= 5
    if n == 1:
        return True
    else:
        return False


# slow, can not stand
def ugly_number(n):
    num = 0
    count = 0
    while count < n:
        num += 1
        if is_ugly(num):
            count += 1
    return num


def test():
    # print(is_ugly(6))
    # print(is_ugly(8))
    # print(is_ugly(14))
    print(ugly_number(1000))


if __name__ == '__main__':
    test()