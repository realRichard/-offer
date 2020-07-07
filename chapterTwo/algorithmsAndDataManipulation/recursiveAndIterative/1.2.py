# iterative
def fibonacci(n):
    if n < 0:
        print('invalid input')
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1
    n1 = 0
    n2 = 1
    result = 0
    for i in range(1, n):
        result = n1 + n2
        n1 = n2
        n2 = result
    return result


def test():
    for i in range(33):
        print(fibonacci(i))


if __name__ == '__main__':
    test()