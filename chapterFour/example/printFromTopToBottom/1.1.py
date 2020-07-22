'''
题目：
    从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
'''


class BinaryTreeNode(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)


def print_from_top_to_bottom(root):
    if not isinstance(root, BinaryTreeNode):
        raise TypeError

    queue = []
    queue.append(root)
    while len(queue) != 0:
        node = queue.pop(0)
        print(node, end=' ')
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    print()


def test():
    root = BinaryTreeNode(8)
    root.left = BinaryTreeNode(6)
    root.right = BinaryTreeNode(10)
    root.left.left = BinaryTreeNode(5)
    root.left.right = BinaryTreeNode(7)
    root.right.left = BinaryTreeNode(9)
    root.right.right = BinaryTreeNode(11)
    print_from_top_to_bottom(root)


if __name__ == '__main__':
    test()