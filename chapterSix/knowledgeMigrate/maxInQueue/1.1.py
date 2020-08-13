'''
题目：
    给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。
    例如，如果输入数组{2, 3, 4, 2, 6, 2, 5, 1}及滑动窗口的大小3，
    那么一共存在6个滑动窗口，它们的最大值分别为{4, 4, 6, 6, 6, 5}，
'''


# 蛮力法, time O(n * k)
def max_in_windows(arr, size):
    return [max(arr[i:i + size]) for i in range(len(arr) - size + 1)]


def test():
    arr = [2, 3, 4, 2, 6, 2, 5, 1]
    print(max_in_windows(arr, 3))


if __name__ == '__main__':
    test()