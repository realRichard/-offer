'''
题目：
请设计一个函数，用来判断在一个矩阵中是否存在一条包含其字符串所有字符的路径。路径可以从矩阵中的任意一格开始，
每一步可以在矩阵中向左、右、上、下移动一格，如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3x4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用下划线标出）。但矩阵中不包含字符串“abfb”的路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
'''


def has_path_core(matrix, rows, cols, row, col, string, string_index, visited):
    # 不能像下面这样写递归结束的条件,  是错的
    # 否则， 每次到达字符串的最后一个字符时， 直接 return True, 不会对其进行检查了
    # string_index 为每次检查的字符在字符串中的下标
    # if len(string) - 1 == string_index:
    #     return True

    # 应改成下面, 下标等于 string_length, 这样的话，相当于全部合理的下标都检查完了, 刚好下标越界
    if len(string) == string_index:
        return True
    has = False
    if (row >= 0 and row < rows and col >= 0 and col < cols 
    and visited[row][col] == False and matrix[row][col] == string[string_index]):
        string_index += 1
        visited[row][col] = True
        has = (
        has_path_core(matrix, rows, cols, row - 1, col, string, string_index, visited) 
        or has_path_core(matrix, rows, cols, row + 1, col, string, string_index, visited)
        or has_path_core(matrix, rows, cols, row, col - 1, string, string_index, visited)
        or has_path_core(matrix, rows, cols, row, col + 1, string, string_index, visited)
        ) 
        if not has:
            visited[row][col] = False
            # string_index -= 1
    return has


def has_path(matrix, string):
    if not isinstance(matrix, list):
        raise TypeError
    for i in matrix:
        if not isinstance(i, list):
            raise ValueError

    rows = len(matrix)
    cols = len(matrix[0])
    string_length = len(string)
    if rows == 0 or cols == 0 or string_length == 0:
        return False
    visited = [[False] * cols for i in range(rows)]
    string_index = 0
    for row in range(rows):
        for col in range(cols):
            # print('row', 'col', row, col)
            if has_path_core(matrix, rows, cols, row, col, string, string_index, visited):
                return True
    return False


def test():
    s1 = 'bfce'
    s2 = 'abfb'
    s3 = 'aaa'
    s4 = 'A'
    matrix = [
        ['a', 'b', 't', 'g'],
        ['c', 'f', 'c', 's'],
        ['j', 'd', 'e', 'h'],
    ]
    print('s1', has_path(matrix, s1))
    print('s2', has_path(matrix, s2))
    print('s3', has_path(matrix, s3))
    print('s4', has_path(matrix, s4))


if __name__ == '__main__':
    test()
