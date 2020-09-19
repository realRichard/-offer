'''
题目：
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''


def digital_sum(n):
    bit_sum = 0
    while n > 0:
        bit_sum += n % 10
        n = n // 10
    return bit_sum


def check(threshold, rows, cols, row, col, visited):
    if (row >= 0 and row < rows and col >= 0 and col < cols and visited[row][col] is False 
    and digital_sum(row) + digital_sum(col) <= threshold):
        return True
    else:
        return False


def move_count_core(threshold, rows, cols, row, col, visited):
    count = 0
    if check(threshold, rows, cols, row, col, visited):
        count += 1
        visited[row][col] = True
        count += (move_count_core(threshold, rows, cols, row - 1, col, visited)
        + move_count_core(threshold, rows, cols, row + 1, col, visited)
        + move_count_core(threshold, rows, cols, row, col - 1, visited)
        + move_count_core(threshold, rows, cols, row, col + 1, visited)
        )
    return count


def move_count(threshold, rows, cols):
    if not isinstance(threshold, int) or not isinstance(rows, int) or not isinstance(cols, int):
        raise TypeError
    if threshold < 0 or rows <= 0 or cols <= 0:
        return 0

    visited = [[False] * cols for row in range(rows)]
    return move_count_core(threshold, rows, cols, 0, 0, visited)


def test():
    # print(digital_sum(345))
    print(move_count(4, 4, 4))


if __name__ == '__main__':
    test()
