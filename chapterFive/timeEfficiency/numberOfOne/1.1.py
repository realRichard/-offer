'''
题目：
    输入一个整数n，求1~n这n个整数的十进制表示中1出现的次数。
    例如，输入12，1~12这些整数中包含1的数字有1、10、11和12，1一共出现了5次。
'''


def number_of_one(n):
    number = 0
    while n > 0:
        if n % 10 == 1:
            number += 1
        n = n // 10
    return number


# time O(nlogn)
def number_of_one_between_one_and_n(n):
    if not isinstance(n, int):
        raise TypeError

    number = 0
    for i in range(1, n + 1):
        number += number_of_one(i)
    return number


def test():
    print(number_of_one_between_one_and_n(12))
    print(number_of_one_between_one_and_n(1))


if __name__ == '__main__':
    test()