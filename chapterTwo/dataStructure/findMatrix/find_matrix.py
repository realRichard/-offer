'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序，请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''


'''
解题思路：
首先选取数组中右上角的数字。如果该数字。如果该数字等于要查找的数字，则查找过程结束；如果该数字大于要查找的数字，则剔除
这个数字所在的列；如果该数字小于要查找的数字，则剔除这个数字所在的行。也就是说，如果要查找的数字不在数组的右上角，则每
一次都在数组的查找范围中剔除一行或者一列，这样每一步都可以缩小查找的范围，直到找到要查找的数字，或者查找范围为空。
'''
def find_matrix(matrix, integer):
    if not isinstance(integer, int):
        return False
    if not isinstance(matrix, list):
        return False
    for i in matrix:
        if not isinstance(i, list):
            return False
    for i in matrix:
        for j in i:
            if not isinstance(j, int):
                return False

    column = len(matrix[0])
    row = len(matrix)
    current_column = column - 1
    current_row = 0
    while current_column >= 0 and current_row <= row - 1:
        if matrix[current_row][current_column] == integer:
            return True
        elif matrix[current_row][current_column] > integer:
            current_column -= 1
        else:
            current_row += 1
    return False


def test():
    two_dimension = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15],
    ]
    # print(len(two_dimension), len(two_dimension[1]))
    print(find_matrix(two_dimension, 7))
    print(find_matrix(two_dimension, 1))
    print(find_matrix(None, 10))
    print(find_matrix(two_dimension, None))


if __name__ == '__main__':
    test()