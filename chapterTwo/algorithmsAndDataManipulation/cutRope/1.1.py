'''
题目：剪绳子
给你一根长度为n的绳子，请把绳子剪成m段（m、n都是整数，n>1,m>1），  每段绳子的长度记为 k[0], k[1], k[2], …, k[m]。
请问 k[0] * k[1] * k[2] * … * k[m] 可能的最大乘积是多少？例如，当绳子的长度为8时，我们把它剪成长度分别为2、3、3的三段，
此时得到的最大乘积是18。
'''


# 动态规划
def max_product_after_cutting(length):
    if not isinstance(length, int):
        raise TypeError

    if length < 2:
        return 0
    elif length == 2:
        return 1
    elif length == 3:
        return 2

    products = [0] * (length + 1)
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3
    max_product = 0
    for i in range(4, length + 1):
        max_product = 0
        for j in range(1, i // 2 + 1):
            product = products[j] * products[i - j]
            if product > max_product:
                max_product = product
            products[i] = max_product
    max_product = products[length]
    return max_product


def test():
    print('8', max_product_after_cutting(8))
    print('3', max_product_after_cutting(3))


if __name__ == '__main__':
    test()
