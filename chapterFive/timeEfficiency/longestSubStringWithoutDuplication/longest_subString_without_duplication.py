'''
题目：
    请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
    假设字符串中只包含‘a’~‘z’的字符。例如，在字符串”arabcacfr“中，
    最长的不含重复字符的子字符串是“acfr”，长度为4。
'''


def longest_subString_without_duplication(string):
    if not isinstance(string, str):
        raise TypeError

    # position 用来更新每个字母在字符串中再次出现位置的索引, -1 表示还未出现
    # position = [-1] * 26
    position = [-1 for i in range(26)]
    max_lenght = 0
    current_length = 0
    for i, c in enumerate(string):
        # 计算字母在 position 中的索引
        index = ord(c) - ord('a')
        # 获得字母上次在字符串中出现的位置
        pre_index = position[index]
        # -1 表示还未出现, 当前子字符串长度可以加一
        if pre_index < 0:
            current_length += 1
        else:
            # 否则, 如果这个字符在当前子字符串之前出现, 也可以加一
            if i - pre_index > current_length:
                current_length += 1
            # 如果这个字符在当前子字符串中, 则应该从这个字符之前出现位置的后一个位置开始计算当前子字符串的长度
            else:
                current_length = i - pre_index
        # 更新字符的出现的位置
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