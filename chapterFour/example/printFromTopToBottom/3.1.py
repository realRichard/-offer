'''
题目：
    请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
    第二行按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
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

    stack1 = []
    stack2 = []
    stack1.append(root)
    current_level_node = 1
    next_level_node = 0
    reverse = True
    while len(stack1) != 0:
        node = stack1.pop()
        print(node, end=' ')
        current_level_node -= 1
        if reverse:
            if node.left is not None:
                # 下一层的节点先用另外一个栈保存
                stack2.append(node.left)
                next_level_node += 1
            if node.right is not None:
                stack2.append(node.right)
                next_level_node += 1
        else:
            if node.right is not None:
                stack2.append(node.right)
                next_level_node += 1
            if node.left is not None:
                stack2.append(node.left)
                next_level_node += 1
        if current_level_node == 0:
            print()
            current_level_node = next_level_node
            next_level_node = 0
            reverse = not reverse
            # 打印完之后在交换两个栈, 继续打印
            stack1, stack2 = stack2, stack1


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