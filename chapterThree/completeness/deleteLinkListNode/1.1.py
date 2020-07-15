'''
题目：
    在O(1)时间内删除链表节点。给定单向链表的头指针和一个节点指针，
    定义一个函数在O(1)时间内删除该节点。
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


def delete_node(link, node):
    header = link.header
    if header is None or node is None:
        raise ValueError

    # 只有头结点， 并且删除头结点
    if header.next is None and node is header:
        link.header = None
    # 删除尾节点, 只能循环找前一个
    elif node.next is None:
        temp = header
        while temp.next is not node:
            temp = temp.next
        temp.next = node.next
    # 用后一个节点填充被删除节点， 然后删除后一个节点， 其效果就是删了, o(1)
    else:
        node_next = node.next
        node.value = node_next.value
        node.next = node_next.next


def test():
    link = LinkedList()
    print(link, link.header)
    for i in range(3):
        node = Node(i)
        link.insert(node)

    delete_node(link, link.header.next)
    # delete_node(link, link.header.next.next)
    # delete_node(link, link.header)

    c_node = link.header
    while c_node is not None:
        print(c_node.value)
        c_node = c_node.next


if __name__ == '__main__':
    test()
