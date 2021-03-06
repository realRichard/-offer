'''
题目：
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
'''


def print_matrix_clock_wisely(matrix, rows, cols):
    if not isinstance(matrix, list) or not isinstance(rows, int) or not isinstance(cols, int):
        raise TypeError
    if rows <= 0 or cols <= 0:
        raise ValueError
    for i in matrix:
        if not isinstance(i, int):
            raise ValueError

    up = 0
    down = rows - 1
    left = 0
    right = cols - 1
    # down + 1, right + 1, 不然无法处理一行或者一列的情况
    while up < down + 1 and left < right + 1:
        for u in range(left, right + 1):
            print(matrix[cols * up + u], end=', ')
        up += 1
        for r in range(up, down + 1):
            print(matrix[r * cols + right], end=', ')
        right -= 1
        # 处理一行的情况
        if rows != 1:
            for d in range(right,  left - 1, -1):
                print(matrix[cols * down + d], end=', ')
            down -= 1
        # 处理一列的情况
        if cols != 1:
            for l in range(down, up - 1, -1):
                print(matrix[l * cols + left], end=', ')
            left += 1
    print()


def test():
    matrix = [i for i in range(1, 17)]
    print(matrix)
    print_matrix_clock_wisely(matrix, 4, 4)


if __name__ == '__main__':
    test()