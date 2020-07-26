'''
题目：
    复制一个复杂链表。在复杂链表中，每个节点除了有一个指针指向下一个节点，
    还有一个指针指向链表中的任一节点或空节点。
'''


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

    clone_head = ComplexLinkedListNode(head.value)
    clone_node = clone_head
    node = head.next
    while node is not None:
        clone_node.next = ComplexLinkedListNode(node.value)
        clone_node = clone_node.next
        node = node.next
    return clone_head


# def clone_sibling(head, clone_head):
#     node = head
#     clone_node = clone_head
#     while node is not None:
#         if node.sibling is not None:
#             # 只能在链表中没有重复元素时有效工作, 如有重复元素， 应该采用计数定位来寻找
#             value = node.sibling.value
#             # 每次从头开始找
#             sibling_node = clone_head
#             while sibling_node is not None:
#                 if sibling_node.value == value:
#                     # print('value', value)
#                     clone_node.sibling = sibling_node
#                     break
#                 sibling_node = sibling_node.next
#         node = node.next
#         clone_node = clone_node.next


# 计数定位， 可在有重复元素时工作
def clone_sibling(head, clone_head):
    node = head
    clone_node = clone_head
    while node is not None:
        sibling = node.sibling
        if sibling is not None:
            count = 0
            temp_head = head
            while temp_head is not None:
                if temp_head is sibling:
                    break
                count +=1
                temp_head = temp_head.next
            temp_clone = clone_head
            for i in range(count):
                temp_clone = temp_clone.next
            clone_node.sibling = temp_clone
        node = node.next
        clone_node = clone_node.next


# time O(n * n)
def complex_linkedList_clone(head):
    # step one, clone every node
    clone_head = clone_nodes(head)
    # step two, set sibling
    clone_sibling(head, clone_head)
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