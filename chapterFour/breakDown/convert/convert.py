'''
题目：
    输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
    要求不能创建任何新的结点，只能调整树中结点指针的指向。
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


'''
    根节点， 左子树， 右子树。 在把左，右子树都转换成排序双向链表之后再和根节点链接起来， 
整颗二叉搜索树也就转换成了排序双向链表.

    把左子树中最大的节点， 根节点， 和右子树的最小节点连接起来。 
至于如何把左子树， 右子树内部的节点链接成链表， 那和原来问题的实质是一样的， 
因此可以递归解决

解决这个问题的关键在于把一个大的问题分解成几个小问题， 并递归地解决小问题
'''
def convert_core(root, last):
    if root is None:
        return 
    node = root
    if node.left is not None:
        last = convert_core(node.left, last)
    node.left = last
    if last is not None:
        last.right = node
    last = node
    if node.right is not None:
        last = convert_core(node.right, last)
    return last


def convert(root):
    last = None
    last_in_linkedList = convert_core(root, last)
    head = last_in_linkedList
    while head.left is not None:
        head = head.left
    return head


def test():
    preorder = [10, 6, 4, 8, 14, 12, 16]
    inorder = [4, 6, 8, 10, 12, 14, 16]
    root = construct(preorder, inorder)
    # pre_travesal(root)
    # print()
    linkedList_head = convert(root)
    print(linkedList_head)
    while linkedList_head is not None:
        print(linkedList_head, end=' ')
        linkedList_head = linkedList_head.right
    print()


if __name__ == '__main__':
    test()