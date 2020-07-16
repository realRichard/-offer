'''
    求链表的中间节点。 如果链表中的节点总数为奇数， 则返回中间节点， 
    如果节点总数是偶数， 则返回中间节点两个节点的任意一个
'''


'''
    一个指针一次走一步， 另一个指针一次走两步
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


def find_middle_node(header):
    if not isinstance(header, Node):
        raise TypeError

    fast = header
    slow = header
    while fast is not None:
        fast = fast.next
        if fast is not None:
            fast = fast.next
            slow = slow.next
    return slow


def test():
    link = LinkedList()
    print(link, link.header)
    for i in range(12):
        node = Node(i)
        link.insert(node)

    # c_node = link.header
    # while c_node is not None:
    #     print(c_node.value)
    #     c_node = c_node.next

    print(find_middle_node(link.header))


if __name__ == '__main__':
    test()