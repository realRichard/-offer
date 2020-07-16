'''
题目：如果一个链表中包含环，如何找出环的入口节点？例如，在如图所示的链表中，环的入口节点是节点3
         ___________
        |           |
1-->2-->3-->4-->5-->6
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


def meeting_node(header):
    if not isinstance(header, Node):
        raise TypeError

    slow = header
    fast = header
    if slow.next is not None:
        fast = slow.next
    else:
        return None
    while fast is not None and fast is not slow:
        fast = fast.next
        if fast is not None:
            fast = fast.next
            slow = slow.next
    if fast is slow:
        return fast
    else:
        return None


def entry_node_of_loop(header):
    encounter_node = meeting_node(header)
    if encounter_node is None:
        return None
    temp = encounter_node.next
    loop_node_count = 1
    while temp is not encounter_node:
        temp = temp.next
        loop_node_count += 1
    # print('count', loop_node_count)
    front = header
    behind = header
    for i in range(loop_node_count):
        front = front.next
    while front is not behind:
        front = front.next
        behind = behind.next
    return front


def test():
    link = LinkedList()
    print(link, link.header)
    for i in range(1, 3):
        node = Node(i)
        link.insert(node)
    entry = Node(3)
    link.insert(entry)
    for i in range(4, 6):
        node = Node(i)
        link.insert(node)
    node6 = Node(6)
    node6.next = entry
    link.insert(node6)

    # print(meeting_node(link.header))
    print(entry_node_of_loop(link.header))

    # c_node = link.header
    # while c_node is not None:
    #     print(c_node.value)
    #     c_node = c_node.next


if __name__ == '__main__':
    test()