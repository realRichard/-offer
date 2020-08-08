'''
题目：
    输入一棵二叉树的根结点，判断该树是不是平衡二叉树。
    如果某二叉树中任意结点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
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


def tree_depth(root):
    if root is None:
        return 0
    # if root.right is None:
    #     return 1 + tree_depth(root.left)
    # if root.left is None:
    #     return 1 + tree_depth(root.right)
    # return 1 + max(tree_depth(root.left), tree_depth(root.right))
    return 1 + max(map(tree_depth, (root.left, root.right)))


# 需要重复遍历节点多次的解法
def is_balanced(root):
    if root is None:
        return True
    left = tree_depth(root.left)
    right = tree_depth(root.right)
    diff = left - right
    if diff < -1 or diff > 1:
        return False
    return is_balanced(root.right) and is_balanced(root.right)


def test():
    preorder = [1, 2, 4, 5, 7, 3, 6]
    inorder = [4, 2, 7, 5, 1, 3, 6]
    root = construct(preorder, inorder)
    tree = BinaryTree(root)
    pre_travesal(root)
    print()
    print(is_balanced(root))


if __name__ == '__main__':
    test()