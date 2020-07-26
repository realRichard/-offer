class ComplexLinkedListNode(object):
    def __init__(self, value=None, next=None, sibling=None):
        self.value = value
        self.next = next
        self.sibling = sibling

    def __str__(self):
        return str(self.value)


class LinkedList(object):
    def __init__(self, header=None):
        self.header = header


def clone_nodes(head):
    if not isinstance(head, ComplexLinkedListNode):
        raise TypeError

    node = head
    while node is not None:
        clone_node = ComplexLinkedListNode(node.value)
        clone_node.next = node.next
        node.next = clone_node
        node = clone_node.next


def clone_sibling(head):
    node = head
    while node is not None:
        clone_node = node.next
        if node.sibling is not None:
            clone_node.sibling = node.sibling.next
        node = clone_node.next


def split_linkedList(head):
    clone_head = head.next
    node = head
    clone_node = clone_head
    while node is not None:
        node.next = clone_node.next
        node = node.next
        if node is not None:
            clone_node.next = node.next
            clone_node = clone_node.next
    return clone_head


# time O(n)
def complex_linkedList_clone(head):
    # step one, clone every node
    clone_nodes(head)
    # step two, set sibling
    clone_sibling(head)
    # step three, split linkedList
    clone_head = split_linkedList(head)
    return clone_head


def test():
    a = ComplexLinkedListNode('a')
    b = ComplexLinkedListNode('b')
    c = ComplexLinkedListNode('c')
    d = ComplexLinkedListNode('d')
    e = ComplexLinkedListNode('e')
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    a.sibling = c
    b.sibling = e
    d.sibling = b
    linked_list = LinkedList(a)
    head = linked_list.header
    print('raw', id(head.sibling), head.sibling)
    print('raw', id(head.next.sibling), head.next.sibling)
    # while head is not None:
    #     print(head)
    #     head = head.next
    clone_head = complex_linkedList_clone(linked_list.header)
    print('sibling', id(clone_head.sibling), clone_head.sibling)
    print('sibling', id(clone_head.next.sibling), clone_head.next.sibling)
    while clone_head is not None:
        print(clone_head)
        clone_head =clone_head.next


if __name__ == '__main__':
    test()