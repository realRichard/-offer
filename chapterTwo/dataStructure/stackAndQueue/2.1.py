'''
题目：用两个队列实现一个栈，完成栈的 push, pop 操作。
'''


class MyStack:
    def __init__(self):
        self._queue1 = []
        self._queue2 = []

    def push(self, element):
        queue1_length = len(self._queue1)
        queue2_length = len(self._queue2)
        if queue1_length == 0:
            self._queue2.append(element)
        else:
            self._queue1.append(element)

    def pop(self):
        queue1_length = len(self._queue1)
        queue2_length = len(self._queue2)
        if queue1_length == 0 and queue2_length == 0:
            print('empty')
            return None

        if queue1_length == 0:
            while len(self._queue2) > 1:
                self._queue1.append(self._queue2.pop(0))
            return self._queue2.pop()
        else:
            while len(self._queue1) > 1:
                self._queue2.append(self._queue1.pop(0))
            return self._queue1.pop()


def test():
    stack = MyStack()
    for i in range(5):
        stack.push(i)

    for i in range(6):
        print(stack.pop())


if __name__ == '__main__':
    test()