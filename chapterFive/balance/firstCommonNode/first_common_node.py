'''
题目：
    输入两个链表，找出它们的第一个公共节点。
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


def first_common_node(head1, head2):
    if not isinstance(head1, Node) or not isinstance(head2, Node):
        raise TypeError

    node1 = head1
    node2 = head2
    link1_length = 0
    link2_length = 0
    while node1 is not None:
        link1_length += 1
        node1 = node1.next
    while node2 is not None:
        link2_length += 1
        node2 = node2.next
    node1 = head1
    node2 = head2
    if link1_length > link2_length:
        length_difference = link1_length - link2_length
        for i in range(length_difference):
            node1 = node1.next
    if link2_length > link1_length:
        length_difference = link2_length - link1_length
        for i in range(length_difference):
            node2 = node2.next
    while node1 is not None and node1 is not node2:
        node1 = node1.next
        node2 = node2.next
    return node1


def test():
    link1 = LinkedList()
    link1.insert(Node(1))
    link1.insert(Node(2))
    link1.insert(Node(3))
    link2 = LinkedList()
    link2.insert(Node(4))
    link2.insert(Node(5))
    node6 = Node(6)
    node6.next = Node(7)
    link1.insert(node6)
    link2.insert(node6)
    print(first_common_node(link1.header, link2.header).value)


if __name__ == '__main__':
    test()