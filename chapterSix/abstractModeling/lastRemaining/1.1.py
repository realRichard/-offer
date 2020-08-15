'''
题目：
    0, 1, …, n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈里删除第m个数字。
    求出这个圆圈里剩下的最后一个数字。
'''


class LinkedNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


# 经典的解法，用环形链表模拟圆圈
def last_remaining(n, m):
    if not isinstance(n, int) or not isinstance(m, int):
        raise TypeError
    if n <= 0 or m <= 0:
        raise ValueError

    head = LinkedNode(0)
    node = head
    for i in range(1, n):
        temp = LinkedNode(i)
        node.next = temp
        node = temp
    node.next = head
    # while node is not None:
    #     print(node.value)
    #     node = node.next

    # while head.next is not head:
    #     node = head
    #     for i in range(m - 1):
    #         node = node.next
    #     if node is head:
    #         tail = node
    #         while tail.next is not head:
    #             tail = tail.next
    #         head = head.next
    #         tail.next = head
    #     else:
    #         temp = node.next
    #         node.next = temp.next

    while head.next is not head:
        own = head
        # note, m - 2
        for i in range(m - 2):
            head = head.next
        if head is own:
            tail = own
            print('own', own.value)
            while tail.next is not own:
                tail = tail.next
            head = head.next
            tail.next = head
        else:
            temp = head.next
            print('will be deleted', temp.value)
            head.next = temp.next
            # 一定要有下面这句
            head = head.next
    return head.value


def test():
    print(last_remaining(5, 3))


if __name__ == '__main__':
    test()