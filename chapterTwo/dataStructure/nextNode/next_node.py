'''
题目：
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，
同时包含指向父结点的指针。
'''


class TreeNode(object):
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)


class Tree(object):
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
    root = TreeNode(preorder[0])
    root.left = construct_core(preorder_left_node, inorder_left_node, left_subTree_length)
    root.right = construct_core(preorder_right_node, inorder_right_node, right_subTree_length)
    if root.left is not None:
        root.left.parent = root
    if root.right is not None:
        root.right.parent = root
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
        if not isinstance(i, str):
            return None
    for i in inorder:
        if not isinstance(i, str):
            return None
    # print('-------')
    # fuck, forgot return, lead to root node is None all the time
    # for python, if a function don't return anything, None is returned by default
    # construct_core(preorder, inorder, preorder_length)
    return construct_core(preorder, inorder, preorder_length)

def in_travesal(root):
    if root.left is not None:
        in_travesal(root.left)
    print(root, end=',')
    if root.right is not None:
        in_travesal(root.right)


def next_node(node):
    if not isinstance(node, TreeNode):
        print('invalid input')
        return None
    # return value, by default
    next_node = None
    # 若该节点存在右子树, 则下一个节点为右子树最左子节点
    if node.right is not None:
        temp_node = node.right
        while temp_node.left is not None:
            temp_node = temp_node.left
        next_node = temp_node

    # 若该节点不存在右子树
    if node.right is None:
        # 当该节点是根节点时， 无下一个节点
        if node.parent is None:
            next_node = None
        # 该节点为父节点的左子节点，则下一个节点为其父节点
        if node is node.parent.left:
            next_node = node.parent
        # 该节点为父节点的右子节点
        if node is node.parent.right:
            parent_node = node
            temp_node = node
            # 则沿着父节点向上遍历
            while parent_node.parent is not None:
                temp_node = parent_node
                parent_node = parent_node.parent
            # 直到找到一个节点的父节点的左子节点为该节点
            # 则该节点的父节点为下一个节点
            if parent_node.left is temp_node:
                next_node = parent_node
            # 如果该节点不为其父节点的左子节点， 则此节点无下一个子节点
            else:
                # can not write, by default
                # if write, more clearly
                next_node = None

    return next_node


def test():
    # build manually is not good
    # a = TreeNode('a')
    # b = TreeNode('b')
    # c = TreeNode('c')
    # d = TreeNode('d')
    # e = TreeNode('e')
    # f = TreeNode('f')
    # g = TreeNode('g')
    # h = TreeNode('h')
    # i = TreeNode('i')

    # automatic build
    preorder = ['a', 'b', 'd', 'e', 'h', 'i', 'c', 'f', 'g']
    inorder = ['d', 'b', 'h', 'e', 'i', 'a', 'f', 'c', 'g']
    root = construct(preorder, inorder)
    print(root)
    tree = Tree(root)
    in_travesal(tree.root)
    print()
    node1 = next_node(root)
    print('a', node1)
    node2 = next_node(root.left.left)
    print('d', node2)
    node3 = next_node(root.left.right.right)
    print('i', node3)
    node4 = next_node(root.right.right)
    print('g', node4)


if __name__ == '__main__':
    test()