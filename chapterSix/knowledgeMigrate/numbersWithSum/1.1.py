'''
题目：
    输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
    如果有多对数字的和等于s，输出任意一对即可。
'''


# time O(n)
def numbers_with_sum(arr, s):
    left = 0
    right = len(arr) - 1
    while left < right:
        two_sum = arr[left] + arr[right]
        if two_sum == s:
            return arr[left], arr[right]
        elif two_sum < s:
            left += 1
        else:
            right -= 1
    return None


def test():
    arr = [1, 2, 4, 7, 11, 15]
    print(numbers_with_sum(arr, 15))
    print(numbers_with_sum(arr, 50))


if __name__ == '__main__':
    test()