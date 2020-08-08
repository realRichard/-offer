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


def kth_node_core(root, nodes):
    if root.left is not None:
        kth_node_core(root.left, nodes)
    nodes.append(root)
    if root.right is not None:
        kth_node_core(root.right, nodes)


def kth_node(root, k):
    if not isinstance(root, BinaryTreeNode) or not isinstance(k, int):
        raise TypeError
    if k <= 0:
        raise ValueError

    nodes = []
    kth_node_core(root, nodes)
    if len(nodes) < k:
        return None
    else:
        return nodes[k - 1]


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
    print(kth_node(root, 8))


if __name__ == '__main__':
    test()