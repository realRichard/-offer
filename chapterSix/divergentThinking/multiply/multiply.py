'''
题目：
    给定一个数组A[0, 1, …, n-1]，请构建一个数组B[0, 1, …, n-1]，
    其中B中的元素B[i] =A[0]×A[1]×… ×A[i-1]×A[i+1]×…×A[n-1]。
    不能使用除法。
'''


'''
思路：
    不能使用除法。以i为分割点，将B拆成C，D两部分，
    左边是A[0] x A[1] x...x A[i-1]右边则为A[i+1] x ...x A[n-1]，
    C[i] = C[i-1] * A[i-1]
'''


# time O(n)
def multiply(a):
    length = len(a)
    b = [1] * length
    for i in range(1, length):
        b[i] = a[i - 1] * b[i - 1]
    temp = 1
    for i in range(length - 2, -1, -1):
        temp *= a[i + 1]
        b[i] *= temp
    return b


def test():
    a1 = [1, 2, 3]
    print(multiply(a1))
    a2 = [1, 0, 3]
    print(multiply(a2))


if __name__ == '__main__':
    test()