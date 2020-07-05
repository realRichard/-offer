'''
题目：请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy
'''


def test():
    foo = 'We are happy.'

    # good
    result1 = foo.replace(' ', '%20')
    print(foo, result1)

    # good
    result2 = ''.join(c if c != ' ' else '%20' for c in foo)
    print(foo, result2)


if __name__ == '__main__':
    test()