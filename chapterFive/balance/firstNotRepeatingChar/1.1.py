'''
题目：
    在字符串中找出第一个只出现一次的字符。如输入“abaccdeff”，则输出‘b’。
'''


# time O(n), space O(1)
def first_not_repeating_char(string):
    if not isinstance(string, str):
        raise TypeError

    # 用 8 位可表示 256 个字符
    hash_table = [0] * 256
    for i in string:
        hash_table[ord(i)] += 1
    for i in string:
        if hash_table[ord(i)] == 1:
            return i
    return None


def test():
    string1 = 'abaccdeff'
    print(first_not_repeating_char(string1))
    string2 = 'aabbcc'
    print(first_not_repeating_char(string2))


if __name__ == '__main__':
    test()