'''
题目：
    输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
    从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''


class BinaryTreeNode(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)


def print_path(stack):
    for i in stack:
        print(i, end=' ')
    print()


def find_path_core(root, n, path, my_sum):
    path.append(root)
    if len(path) == 0:
        return 
    my_sum += root.value
    if my_sum == n:
        print_path(path)
    elif my_sum < n:
        if root.left is not None:
            find_path_core(root.left, n, path, my_sum)
        if root.right is not None:
            find_path_core(root.right, n, path, my_sum)
    # 不要也行， 这句
    # my_sum -= root.value
    path.pop(-1)


def find_path(root, n):
    if not isinstance(root, BinaryTreeNode):
        raise TypeError
    if not isinstance(n, int):
        raise TypeError

    path = []
    my_sum = 0
    find_path_core(root, n, path, my_sum)


def test():
    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(5)
    root.right = BinaryTreeNode(12)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(7)
    find_path(root, 22)


if __name__ == '__main__':
    test()
