'''
题目：
    请实现两个函数，分别用来序列化和反序列化二叉树。
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


def serialize(root, stream=''):
    if root is None:
        return stream + '$,'
    stream += str(root.value) + ','
    stream = serialize(root.left, stream)
    stream = serialize(root.right, stream)
    return stream


def deserialize(stream):
    if not isinstance(stream, str):
        raise TypeError

    data = iter(stream.split(','))

    def deserialize_core(data):
        val = next(data)
        if val == '$':
            return None
        node = BinaryTreeNode(val)
        node.left = deserialize_core(data)
        node.right = deserialize_core(data)
        return node

    return deserialize_core(data)


def test():
    preorder = [1, 2, 4, 3, 5, 6]
    inorder = [4, 2, 1, 5, 3, 6]
    root = construct(preorder, inorder)
    pre_travesal(root)
    print()
    sequence = serialize(root)
    print(sequence)
    root1 = deserialize(sequence)
    pre_travesal(root1)
    print()
    print('root id: ', id(root))
    print('root1 id: ', id(root1))


if __name__ == '__main__':
    test()