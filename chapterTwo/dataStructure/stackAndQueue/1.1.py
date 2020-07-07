'''
题目：用两个栈来实现一个队列，完成队列的 inqueue, dequeue操作。
'''


class MyQueue:
    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    def inqueue(self, element):
        self._stack1.append(element)

    def dequeue(self):
        if len(self._stack2) != 0:
            return self._stack2.pop()
        if len(self._stack1) == 0:
            print('empty')
            return None
        else:
            while len(self._stack1) != 0:
                self._stack2.append(self._stack1.pop())
            return self._stack2.pop()


def test():
    queue = MyQueue()
    for i in range(5):
        queue.inqueue(i)

    for i in range(7):
        print(queue.dequeue())


if __name__ == '__main__':
    test()
