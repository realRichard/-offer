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


def clone_nodes(head, table):
    if not isinstance(head, ComplexLinkedListNode):
        raise TypeError

    clone_head = ComplexLinkedListNode(head.value)
    table[head] = clone_head
    clone_node = clone_head
    node = head.next
    while node is not None:
        clone_node.next = ComplexLinkedListNode(node.value)
        clone_node = clone_node.next
        table[node] = clone_node
        node = node.next
    return clone_head


def clone_sibling(head, clone_head, table):
    node = head
    clone_node = clone_head
    while node is not None:
        if node.sibling is not None:
            clone_node.sibling = table[node.sibling]
        clone_node = clone_node.next
        node = node.next


# time O(n), space O(n)
def complex_linkedList_clone(head):
    pair_table = dict()
    # step one, clone every node
    clone_head = clone_nodes(head, pair_table)
    # step two, set sibling
    clone_sibling(head, clone_head, pair_table)
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
    # head = linked_list.header
    # print(head.sibling)
    # while head is not None:
    #     print(head)
    #     head = head.next
    clone_head = complex_linkedList_clone(linked_list.header)
    print('sibling', id(clone_head.sibling), clone_head.sibling)
    print('sibling', id(clone_head.next.sibling), clone_head.next.sibling)
    # while clone_head is not None:
    #     print(clone_head)
    #     clone_head =clone_head.next


if __name__ == '__main__':
    test()