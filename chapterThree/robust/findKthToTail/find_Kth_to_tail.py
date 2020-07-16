'''
题目：链表中倒数第k个节点
    输入一个链表，输出该链表中倒数第K的结点，为了符合大多数人的习惯，本题从1开始计数，即链表的尾结点是倒数第1个节点。
    例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6，这个链表的倒数第3个节点是指为4的节点。
'''


class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList(object):
    def __init__(self):
        self.header = None

    def insert(self, node):
        if self.header is None:
            self.header = node
        else:
            current_node = self.header
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node


def find_Kth_to_tail(header, k):
    if not isinstance(header, Node) or not isinstance(k, int):
        raise TypeError
    if k <= 0:
        raise ValueError

    front = header
    behind = None
    n = k - 1
    i = 0
    while front is not None and i <= n:
        front = front.next
        i += 1
    if i == k:
        behind = header
        while front is not None:
            front = front.next
            behind = behind.next
        return behind
    else:
        print('invalid input, k > linkList nodes')
        return None


def test():
    link = LinkedList()
    print(link, link.header)
    for i in range(10):
        node = Node(i)
        link.insert(node)

    # c_node = link.header
    # while c_node is not None:
    #     print(c_node.value)
    #     c_node = c_node.next

    print('1', find_Kth_to_tail(link.header, 1))
    print('2', find_Kth_to_tail(link.header, 2))
    print('9', find_Kth_to_tail(link.header, 9))
    print('10', find_Kth_to_tail(link.header, 10))
    print('11', find_Kth_to_tail(link.header, 11))


if __name__ == '__main__':
    test()