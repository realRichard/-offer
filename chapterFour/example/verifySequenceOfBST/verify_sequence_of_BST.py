'''
题目：
    输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
    如果是则返回true,否则返回false。假设输入的数组的任意两个数字都互不相同。
    例如，输入数组{5,7,6,9,11,10,8},则返回true，因为这个整数序列是二叉搜索树的后序遍历结果。
    如果输入的数组是{7,4,6,5,}，则由于没有哪颗二叉搜索树的后序遍历结果是这个序列，因此返回false。
'''


def verify_sequence_of_BST_core(sequence):
    l = len(sequence)
    if l == 0:
        return False
    root = sequence[-1]
    left_nodes = 0
    for i in sequence:
        if i < root:
            left_nodes += 1
        else:
            break
    for j in range(left_nodes, l - 1):
        if sequence[j] < root:
            return False
    left = True
    right = True
    if left_nodes > 0:
        left = verify_sequence_of_BST_core(sequence[:left_nodes])
    if l - 1 - left_nodes > 0:
        right = verify_sequence_of_BST_core(sequence[left_nodes:l - 1])
    return left and right


def verify_sequence_of_BST(sequence):
    if not isinstance(sequence, list):
        raise TypeError
    for i in sequence:
        if not isinstance(i, int):
            raise ValueError

    return verify_sequence_of_BST_core(sequence)


def test():
    post_order1 = [5, 7, 6, 9, 11, 10, 8]
    post_order2 = [7, 4, 6, 5]
    print(verify_sequence_of_BST(post_order1))
    print(verify_sequence_of_BST(post_order2))


if __name__ == '__main__':
    test()