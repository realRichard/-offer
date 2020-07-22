'''
题目：
    从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
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
    current_level_node = 1
    next_level_node = 0
    while len(queue) != 0:
        node = queue.pop(0)
        print(node, end=' ')
        current_level_node -= 1
        if node.left is not None:
            queue.append(node.left)
            next_level_node += 1
        if node.right is not None:
            queue.append(node.right)
            next_level_node += 1
        if current_level_node == 0:
            print()
            current_level_node = next_level_node
            next_level_node = 0


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