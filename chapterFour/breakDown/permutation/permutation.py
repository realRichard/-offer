'''
题目:
    输入一个字符串，打印出该字符串中字符的所有排列顺序。例如:输入字符串abc，
    则打印出字符a、b、c所能排列出的所有字符串abc、acb、bac、bca、cab和cba。
'''


def permutation_core(string, start, end):
    if start >= end:
        print(string)
    else:
        for i in range(start, end):
            s = list(string)
            s[start], s[i] = s[i], s[start]
            string = ''.join(s)
            permutation_core(string, start + 1, end)


def permutation(string):
    if not isinstance(string, str):
        raise TypeError

    start = 0
    end = len(string)
    permutation_core(string, start, end)


def test():
    string = 'abcd'
    permutation(string)


if __name__ == '__main__':
    test()