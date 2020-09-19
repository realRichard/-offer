'''
题目：
    输入两个树结点，求它们的最低公共祖先。
'''


class TreeNode:
    # 假设有三个节点
    def __init__(self, value=None, left=None, middle=None, right=None):
        self.value = value
        self.left = left
        self.middle = middle
        self.right = right


def get_path(root, node, path):
    path.append(root.value)
    if root is node:
        return True
    found = False
    if not found and root.left is not None:
        found = get_path(root.left, node, path)
        # important
        if not found:
            path.pop()
    if not found and root.middle is not None:
        found = get_path(root.middle, node, path)
        if not found:
            path.pop()
    if not found and root.right is not None:
        found = get_path(root.right, node, path)
        if not found:
            path.pop()
    return found


def last_common_node(path1, path2):
    length1 = len(path1)
    length2 = len(path2)
    for i in range(max(length1, length2)):
        if path1[i] != path2[i]:
            return path1[i - 1]


# time O(n), space 最差 O(n) 通常 O(logn)
def last_common_parent(root, node1, node2):
    if not isinstance(root, TreeNode) or not isinstance(node1, TreeNode) or not isinstance(node2, TreeNode):
        raise TypeError

    node1_path = []
    node1_exist = get_path(root, node1, node1_path)
    node2_path = []
    node2_exist = get_path(root, node2, node2_path)
    # print('node1_path', node1_path)
    # print('node2_path', node2_path)
    if node1_exist and node2_exist:
        return last_common_node(node1_path, node2_path)
    return None


def test():
    A = TreeNode('A')
    B = TreeNode('B')
    C = TreeNode('C')
    D = TreeNode('D')
    E = TreeNode('E')
    F = TreeNode('F')
    G = TreeNode('G')
    H = TreeNode('H')
    I = TreeNode('I')
    J = TreeNode('J')
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    D.left = F
    D.right = G
    E.left = H
    E.middle = I
    E.right = J
    root = A
    print(last_common_parent(root, F, H))
    print(last_common_parent(root, F, C))


if __name__ == '__main__':
    test()