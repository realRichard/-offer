'''
题目：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减排序的数组的一个旋转，输出旋转数组的
最小元素。例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
'''


def my_min(arr):
    if not isinstance(arr, list):
        print('invalid input')
        return None
    for i in arr:
        if not isinstance(i, int):
            print('invalid input')
            return None
    if len(arr) == 0:
        return None
    # if the first < the last, means arr already sorted, return the first directly 
    if arr[0] < arr[-1]:
        return arr[0]
    start = 0
    end = len(arr) - 1
    middle = (start + end) // 2
    while end - start > 1:
        # if the first the midlle, the last are equal
        # we can not determine the middle 
        # but to sequential search
        if arr[start] == arr[end] and arr[middle] == arr[start]:
            return min(arr)
        if arr[middle] >= arr[start]:
            start = middle
        else:
            end = middle
        middle = (start + end) // 2
    return arr[end]


def test():
    l = [1]
    print(my_min(l))
    a = [8, 9, 100, 4, 5]
    print(my_min(a))
    b = [1, 0, 1, 1, 1]
    print(my_min(b))


if __name__ == '__main__':
    test()
