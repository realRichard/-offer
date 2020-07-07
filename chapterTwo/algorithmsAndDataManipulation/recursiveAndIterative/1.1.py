'''
题目：求斐波那契数列的第n项
'''


# recursive
def fibonacci(n):
    if n < 0:
        print('invalid input')
        return None
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def test():
    for i in range(33):
        print(fibonacci(i))


if __name__ == '__main__':
    test()