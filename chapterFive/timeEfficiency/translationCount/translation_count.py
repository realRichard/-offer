'''
题目：
    给定一个数字，我们按照如下规则把它翻译为字符串：0翻译成“a“，1翻译成”b“，……，……25翻译成”z“。
    一个数字可能有多少个翻译。例如，12258有5种不同的翻译，分别是“bccfi”、“bwfi”、“bczi“、”mcfi“和”mzi“。
    请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
'''


def translation_count(n):
    if not isinstance(n, int):
        raise TypeError
    if n < 0:
        raise ValueError

    num = str(n)
    length = len(num)
    # counts = [0 for i in range(length)]
    counts = [0] * length
    for i in range(length - 1, -1, -1):
        if i < length - 1:
            count = counts[i + 1]
        else:
            count = 1
        if i < length - 1:
            converted = int(num[i]) * 10 + int(num[i + 1])
            if 10 <= converted <= 25:
                if i < length - 2:
                    count += counts[i + 2]
                else:
                    count += 1
        counts[i] = count
    # print(counts)
    return counts[0]


def test():
    print(translation_count(12258))
    print(translation_count(0))
    print(translation_count(25))
    print(translation_count(26))
    print(translation_count(411311))


if __name__ == '__main__':
    test()