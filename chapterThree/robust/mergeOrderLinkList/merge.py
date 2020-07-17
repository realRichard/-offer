'''
题目：输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。例如，输入如下的链表1和链表2，则合并之后的升序链表如链表3所示。
    链表1：1-->3-->5-->7
    链表2：2-->4-->6-->8
    链表3：1-->2-->3-->4-->5-->6-->7-->8
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


def merge(head1, head2):
    if head1 is None:
        if not isinstance(head2, Node):
            raise TypeError
        return head2
    elif head2 is None:
        if not isinstance(head1, Node):
            raise TypeError
        return head1
    merge_head = None
    if head1.value < head2.value:
        merge_head = head1
        merge_head.next = merge(head1.next, head2)
    else:
        merge_head = head2
        merge_head.next = merge(head1, head2.next)
    return merge_head


def test():
    link1 = LinkedList()
    link2 = LinkedList()
    for i in range(1, 9):
        node = Node(i)
        if i & 0x1 == 1:
            link1.insert(node)
        else:
            link2.insert(node)

    result = merge(link1.header, link2.header)

    c_node = result
    while c_node is not None:
        print(c_node)
        c_node = c_node.next


if __name__ == '__main__':
    test()