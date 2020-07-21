'''
题目：
    定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
    在该栈中，调用min、push及pop的时间复杂度都是O(1)。
'''


class Stack(object):
    def __init__(self):
        self._stack = []
        self._assist = []

    def push(self, n):
        if self.empty():
            self._assist.append(n)
        else:
            minimal = self._assist[-1]
            if minimal > n:
                self._assist.append(n)
            else:
                self._assist.append(minimal)
        self._stack.append(n)

    def pop(self):
        if self.empty():
            return None
        else:
            self._assist.pop()
            return self._stack.pop()

    def min(self):
        if self.empty():
            return None
        else:
            return self._assist[-1]

    def top(self):
        if self.empty():
            return None
        else:
            return self._stack[-1]

    def empty(self):
        if len(self._stack) == 0:
            return True
        else:
            return False


def test():
    stack = Stack()
    stack.push(10)
    stack.push(1)
    stack.push(10)
    print(stack.min())
    # print(stack.top())


if __name__ == '__main__':
    test()