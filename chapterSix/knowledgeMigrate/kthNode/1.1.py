'''
题目：
    给定一棵二叉搜索树，请找出其中的第k小的结点。
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


def construct_core(preorder, inorder, length):
    if length == 0:
        return None
    try:
        root_index_in_inorder = inorder.index(preorder[0])
    except ValueError as identifier:
        print('invalid input')
        return None

    # print('root index', root_index_in_inorder)

    inorder_left_node = inorder[0:root_index_in_inorder]
    inorder_right_node = inorder[root_index_in_inorder + 1:]
    preorder_left_node = preorder[1:len(inorder_left_node) + 1]
    preorder_right_node = preorder[1 + len(preorder_left_node):]
    left_subTree_length = len(inorder_left_node)
    right_subTree_length = len(inorder_right_node)
    root = BinaryTreeNode(preorder[0])
    root.left = construct_core(preorder_left_node, inorder_left_node, left_subTree_length)
    root.right = construct_core(preorder_right_node, inorder_right_node, right_subTree_length)
    # print('root', root)
    return root


def construct(preorder, inorder):
    if not isinstance(preorder, list) or not isinstance(inorder, list):
        return None
    preorder_length = len(preorder)
    inorder_length = len(inorder)
    if preorder_length != inorder_length:
        return None
    for i in preorder:
        if not isinstance(i, int):
            return None
    for i in inorder:
        if not isinstance(i, int):
            return None
    # print('-------')
    # fuck, forgot return, lead to root node is None all the time
    # for python, if a function don't return anything, None is returned by default
    # construct_core(preorder, inorder, preorder_length)
    return construct_core(preorder, inorder, preorder_length)


def pre_travesal(root):
    print(root, end=',')
    if root.left is not None:
        pre_travesal(root.left)
    if root.right is not None:
        pre_travesal(root.right)


def kth_node_core(root, k):
    result = None
    if root.left is not None:
        result = kth_node_core(root.left, k)
    if result is None:
        if k[0] == 1:
            result = root
        k[0] -= 1
    if result is None:
        if root.right is not None:
            result = kth_node_core(root.right, k)
    return result


def kth_node(root, k):
    if not isinstance(root, BinaryTreeNode) or not isinstance(k, int):
        raise TypeError
    if k <= 0:
        raise ValueError

    '''
    Python 不允许程序员选择采用传值还是传引用。
    Python 参数传递采用的肯定是“传对象引用”的方式。 
    这种方式相当于传值和传引用的一种综合。
    如果函数收到的是一个可变对象（比如字典或者列表）的引用，
    就能修改对象的原始值－－相当于通过“传引用”来传递对象。
    如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，
    就不能直接修改原始对象－－相当于通过“传值’来传递对象
    '''
    # 不过强行把整型变量变成列表，也挺奇怪的。
    n = [k]
    return kth_node_core(root, n)


def test():
    preorder = [5, 3, 2, 4, 7, 6, 8]
    inorder = [2, 3, 4, 5, 6, 7, 8]
    root = construct(preorder, inorder)
    tree = BinaryTree(root)
    # print(tree.root, tree.root.left)
    pre_travesal(root)
    print()
    print(kth_node(root, 1))
    print(kth_node(root, 2))
    print(kth_node(root, 3))


if __name__ == '__main__':
    test()