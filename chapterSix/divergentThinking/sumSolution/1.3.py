'''
方法二：
    利用两个函数，一个函数充当递归函数的角色，另一个函数处理终止递归的情况。如果对n连续进行两次反运算，
    那么非零的n转换为True，0转换为False。利用这一特性终止递归。注意考虑测试用例为0的情况。
'''


def sum0(n):
    return 0


def sum_(n):
    func = {
        False: sum0,
        True: sum_,
    }
    return n + func[not not n](n - 1)


def sum_solution(n):
    return sum_(n)


def test():
    print(sum_solution(100))


if __name__ == '__main__':
    test()