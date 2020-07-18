'''
题目：输入两颗二叉树A和B，判断B是不是A的子结构。
       1                3
      / \              /
A = 2   3      B =  4
        /
       4
'''


class BinaryTreeNode(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root


def pre_travesal(root):
    print(root, end=',')
    if root.left is not None:
        pre_travesal(root.left)
    if root.right is not None:
        pre_travesal(root.right)


def has_subtree_core(root1, root2):
    if root2 is None:
        return True
    if root1 is None:
        return False
    result = False
    if root1.value == root2.value:
        result = has_subtree_core(root1.left, root2.left) and has_subtree_core(root1.right, root2.right)
    return result


def has_subtree(root1, root2):
    if root1 is None or root2 is None:
        return False

    result = False
    if root1.value == root2.value:
        result = has_subtree_core(root1, root2)
    if not result:
        result = has_subtree(root1.left, root2)
    if not result:
        result = has_subtree(root1.right, root2)
    return result


def test():
    tree1 = BinaryTreeNode(8)
    tree1.left = BinaryTreeNode(8)
    tree1.right = BinaryTreeNode(7)
    tree1.left.left = BinaryTreeNode(9)
    tree1.left.right = BinaryTreeNode(2)
    tree1.left.right.left = BinaryTreeNode(4)
    tree1.left.right.right = BinaryTreeNode(7)
    # pre_travesal(tree1)

    tree2 = BinaryTreeNode(8)
    tree2.left = BinaryTreeNode(9)
    tree2.right = BinaryTreeNode(2)
    # pre_travesal(tree2)

    print(has_subtree(tree1, tree2))


if __name__ == '__main__':
    test()
