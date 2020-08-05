'''
题目：
    请实现一个函数，用来找出字符流中第一个只出现一次的字符。
    例如，当从字符流中只读出前两个字符“go”时，第一个只出现一次的字符是‘g'：
    当从该字符流中读出前6个字符“google”，第一个只出现一次的字符是’l'。
'''
import sys


class CharStatistics:
    def __init__(self):
        self._index = 0
        self._occurrence = [-1 for i in range(256)]

    def insert(self, c):
        if self._occurrence[ord(c)] == -1:
            self._occurrence[ord(c)] = self._index
        elif self._occurrence[ord(c)] >= 0:
            self._occurrence[ord(c)] = -2
        self._index += 1

    def first_appearing_once(self):
        min_index = sys.maxsize
        c = None
        for i in range(256):
            if 0 <= self._occurrence[i] < min_index:
                min_index = self._occurrence[i]
                c = chr(i)
        return c


def test():
    statistics = CharStatistics()
    statistics.insert('g')
    statistics.insert('o')
    print('(' + statistics.first_appearing_once() + ')')
    statistics.insert('o')
    statistics.insert('g')
    statistics.insert(' ')
    statistics.insert('e')
    print('(' + statistics.first_appearing_once() + ')')


if __name__ == '__main__':
    test()