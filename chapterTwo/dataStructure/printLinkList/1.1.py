'''
题目：
输入一个链表的头节点，从尾到头反过来打印出每个节点的值
'''


class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


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


# use stack
def print_linkList_reversingly(header):
    stack = []
    c_node = header
    while c_node is not None:
        stack.append(c_node)
        c_node = c_node.next
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i].value)


def test():
    link = LinkedList()
    print(link, link.header)
    for i in range(10):
        node = Node(i)
        link.insert(node)

    c_node = link.header
    while c_node is not None:
        print(c_node.value)
        c_node = c_node.next
    print('c_node', c_node)
    print('header', link.header.value)

    print_linkList_reversingly(link.header)
    print('header', link.header.value)


if __name__ == '__main__':
    test()