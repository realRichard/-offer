'''
题目：
    删除链表中重复的节点。
    在一个排序的链表中，如何删除重复的节点？
    例如，链表1->2->3->3->4->4->5 处理后为 1->2->5。
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


def delete_duplicate(link):
    if not isinstance(link, LinkedList):
        raise TypeError
    if link.header is None:
        return 

    # 标记变量， 头结点或者前几个节点都重复
    is_header_and_duplicate = True
    pre_node = None
    temp = link.header
    while temp is not None:
        next_node = temp.next
        if next_node is not None and temp.value == next_node.value:
            n_node = next_node.next
            while n_node is not None and n_node.value == temp.value:
                n_node = n_node.next
            # 头结点重复, 设置头结点,
            if pre_node is None:
                link.header = n_node
                # 但不能保证原来的第二个节点是否也重复， 所以再加一个 if
                if not is_header_and_duplicate:
                    pre_node = link.header 
            else:
                pre_node.next = n_node
            temp = n_node
        else:
            # 头结点或者前几个节点都不重复， 第一次标记变量就会被设为 false, 并且 pre_node 也不为 None 了
            is_header_and_duplicate = False
            pre_node = temp
            temp = temp.next


def test():
    link = LinkedList()
    print(link, link.header)
    for i in range(3):
        # node1 = Node(i)
        # link.insert(node1)
        node2 = Node(i)
        link.insert(node2)

    for i in range(3, 5):
        node1 = Node(i)
        link.insert(node1)
        node2 = Node(i)
        link.insert(node2)

    for i in range(5, 7):
        # node1 = Node(i)
        # link.insert(node1)
        node2 = Node(i)
        link.insert(node2)

    delete_duplicate(link)

    c_node = link.header
    while c_node is not None:
        print(c_node.value)
        c_node = c_node.next


if __name__ == '__main__':
    test()