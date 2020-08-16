'''
题目：
    求1+2+…+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字
    及条件判断语句（A?B:C）。
'''


def sum_solution(n):
    return sum(range(1, n + 1))


def test():
    print(sum_solution(100))


if __name__ == '__main__':
    test()