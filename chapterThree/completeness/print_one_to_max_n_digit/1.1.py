'''
题目：
    输入数字n，按顺序打印出从1到最大的n位十进制数。比如输入3，则打印出1、2、3一直到最大的3位数999。
'''


'''
https://docs.python.org/3/library/exceptions.html#OverflowError

exception OverflowError
    Raised when the result of an arithmetic operation is too large to be represented. 
    This cannot occur for integers (which would rather raise MemoryError than give up). 
    However, for historical reasons, OverflowError is sometimes raised for integers that are outside a required range. 
    Because of the lack of standardization of floating point exception handling in C, 
    most floating point operations are not checked.
'''


def print_one_to_max_n_digit(n):
    if not isinstance(n, int):
        raise TypeError

    if n <= 0:
        raise ValueError

    num = pow(10, n)
    for i in range(1, num):
        print(i)


def test():
    print_one_to_n_digit(2)
    print_one_to_n_digit(1)


if __name__ == '__main__':
    test()