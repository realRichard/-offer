'''
题目：
    假设一个单调递增的数组里的每个元素都是整数并且是唯一的。
    请编程实现一个函数，找出数组中任意一个数值等于其下标的元素。
    例如，在数组{-3，-1，1,3,5}中，数字3和它的下标相等。
'''


def number_same_as_index(arr):
    length = len(arr)
    left = 0
    right = length - 1
    while left <= right:
        # middle = (left + right) >> 1
        middle = left + ((right - left) >> 1)
        middle_data = arr[middle]
        if middle_data == middle:
            return middle
        elif middle_data > middle:
            right = middle - 1
        else:
            left = middle + 1
    return None


def test():
    arr = [-3, -1, 1, 3, 5]
    print(number_same_as_index(arr))


if __name__ == '__main__':
    test()