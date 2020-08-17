'''
题目：
    不使用新的变量， 交换两个变量的值。 比如有两个变量 a， b， 我们希望交换他们的值。
'''


# 基于加减法
def swap1(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


# 基于加异或
def swap2(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


def test():
    print(swap1(1, 4))
    print(swap1(0, -1))
    print(swap1(-3, -2))
    print(swap1(200, 100))


if __name__ == '__main__':
    test()