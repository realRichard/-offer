'''
    输入一个整数数组， 判断该数组是不是某二叉搜索树的前序遍历结果
'''


def verify_sequence_of_BST_core(sequence):
    l = len(sequence)
    if l == 0:
        return False
    root = sequence[0]
    left_nodes = 0
    for i in range(1, l):
        if sequence[i] < root:
            left_nodes += 1
        else:
            break
    for j in range(left_nodes + 1, l):
        if sequence[j] < root:
            return False
    left = True
    right = True
    if left_nodes > 0:
        left = verify_sequence_of_BST_core(sequence[1:left_nodes + 1])
    if l - 1 - left_nodes > 0:
        right = verify_sequence_of_BST_core(sequence[left_nodes + 1:])
    return left and right


def verify_sequence_of_BST(sequence):
    if not isinstance(sequence, list):
        raise TypeError
    for i in sequence:
        if not isinstance(i, int):
            raise ValueError

    return verify_sequence_of_BST_core(sequence)


def test():
    pre_order1 = [8, 6, 5, 7, 10, 9, 11]
    pre_order2 = [8, 10, 6]
    print(verify_sequence_of_BST(pre_order1))
    print(verify_sequence_of_BST(pre_order2))


if __name__ == '__main__':
    test()