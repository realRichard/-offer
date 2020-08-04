'''
题目：
    在一个 m x n 的期盼的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0)。
    你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或向下移动一格，
    直到到达棋盘的右下角。给定要给棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？
'''


def max_value(checkerboard, rows, cols):
    if not isinstance(checkerboard, list) or not isinstance(rows, int) or not isinstance(cols, int):
        raise TypeError
    if rows <= 0 or cols <= 0:
        raise ValueError
    for i in checkerboard:
        if not isinstance(i, int):
            raise TypeError
        if i <= 0:
            raise ValueError

    values = [0] * cols
    for i in range(rows):
        for j in range(cols):
            up = 0
            left = 0
            if i > 0:
                up = values[j]
            if j > 0:
                left = values[j - 1]
            values[j] = max(up, left) + checkerboard[i * cols + j]
    return values[-1]


def test():
    checkerboard = [1, 10, 3, 8, 12, 2, 9, 6, 5, 7, 4, 11, 3, 7, 16, 5]
    print(max_value(checkerboard, 4, 4))


if __name__ == '__main__':
    test()