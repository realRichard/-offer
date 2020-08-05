# time O(n), space O(n)
def first_not_repeating_char(string):
    if not isinstance(string, str):
        raise TypeError

    # counter = {}
    counter = dict()
    for i in string:
        counter[i] = counter.get(i, 0) + 1
    for i in string:
        if counter[i] == 1:
            return i
    return None


def test():
    string1 = 'abaccdeff'
    print(first_not_repeating_char(string1))
    string2 = 'aabbcc'
    print(first_not_repeating_char(string2))


if __name__ == '__main__':
    test()