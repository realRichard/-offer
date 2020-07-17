'''
题目：
    定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
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


def reverse_linkList(head):
    if not isinstance(head, Node):
        raise TypeError

    behind = head
    current = None
    front = None
    if behind.next is not None:
        current = behind.next
        behind.next = None
        if current.next is not None:
            front = current.next
            while front is not None:
                # print('behind', behind)
                # print('current', current)
                # print('front', front)
                current.next = behind
                behind = current
                current = front
                front = front.next
                # 这一步是需要的, 不然连不上
                current.next = behind
            return current
        else:
            current.next = behind
            return current
    else:
        return behind


def test():
    link = LinkedList()
    print(link, link.header)
    for i in range(4):
        node = Node(i)
        link.insert(node)

    result = reverse_linkList(link.header)
    print(result)

    c_node = result
    while c_node is not None:
        print(c_node.value)
        c_node = c_node.next


if __name__ == '__main__':
    test()