from collections import Counter


# time O(n), space O(n)
def first_not_repeating_char(string):
    if not isinstance(string, str):
        raise TypeError

    c = Counter(string)
    for i in string:
        if c[i] == 1:
            return i
    return None


def test():
    string1 = 'abaccdeff'
    print(first_not_repeating_char(string1))
    string2 = 'aabbcc'
    print(first_not_repeating_char(string2))


if __name__ == '__main__':
    test()