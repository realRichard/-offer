'''
题目：
    请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
    假设字符串中只包含‘a’~‘z’的字符。例如，在字符串”arabcacfr“中，
    最长的不含重复字符的子字符串是“acfr”，长度为4。
'''


def longest_subString_without_duplication(string):
    if not isinstance(string, str):
        raise TypeError

    # position = [-1] * 26
    position = [-1 for i in range(26)]
    max_lenght = 0
    current_length = 0
    for i, c in enumerate(string):
        index = ord(c) - ord('a')
        pre_index = position[index]
        if pre_index < 0:
            current_length += 1
        else:
            if i - pre_index > current_length:
                current_length += 1
            else:
                current_length = i - pre_index
        position[index] = i
        if current_length > max_lenght:
            max_lenght = current_length
    return max_lenght


def test():
    print(longest_subString_without_duplication('arabcacfr'))
    print(longest_subString_without_duplication('a'))
    print(longest_subString_without_duplication('abcde'))
    print(longest_subString_without_duplication('aaa'))


if __name__ == '__main__':
    test()