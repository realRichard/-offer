'''
题目：
    字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
    请定义一个函数实现字符串左旋转操作的功能。比如输入字符串"abcdefg"和数字2，
    该函数将返回左旋转2位得到的结果"cdefgab"。
'''


# def left_rotate_string(string, n):
#     return string[n:] + string[:n]


def left_rotate_string(string, n):
    return (string + string)[n:n + len(string)]


def test():
    string = 'abcdefg'
    print(left_rotate_string(string, 2))


if __name__ == '__main__':
    test()