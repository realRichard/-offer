'''
题目：
    在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
    输入一个数组,求出这个数组中的逆序对的总数。
    例如，在数组{7,5,6,4}中，一共存在5个逆序对，
    分别是{7，6}、{7,5}、{7,4}、{6,4}和{5，4}。
'''
import copy


def inverse_pairs_core(arr, auxiliary_arr, start, end):
    if start == end:
        auxiliary_arr[start] = arr[start]
        return 0
    length = (end - start) // 2
    left = inverse_pairs_core(arr, auxiliary_arr, start, start + length)
    right = inverse_pairs_core(arr, auxiliary_arr, start + length + 1, end)
    # 不这样的话， arr 就不是部分排序的， 就没有维持上一次更改的状态，之后就不会对了, auxiliary_arr 最后也不是排序的
    arr = copy.deepcopy(auxiliary_arr)
    count = 0
    i = start + length
    j = end
    index_copy = end
    while i >= start and j >= start + length + 1:
        if arr[i] > arr[j]:
            auxiliary_arr[index_copy] = arr[i]
            # print(arr, auxiliary_arr)
            i -= 1
            count += j - (start + length)
        else:
            auxiliary_arr[index_copy] = arr[j]
            j -= 1
        index_copy -= 1
    while i >= start:
        auxiliary_arr[index_copy] = arr[i]
        i -= 1
        index_copy -= 1
    while j >= start + length + 1:
        auxiliary_arr[index_copy] = arr[j]
        j -= 1
        index_copy -= 1
    # print(arr, auxiliary_arr)
    # print(count, right, left)
    return count + left + right


def inverse_pairs(arr):
    if not isinstance(arr, list):
        raise TypeError
    for i in arr:
        if not isinstance(i, int):
            raise ValueError

    length = len(arr)
    auxiliary_arr = copy.deepcopy(arr)
    count = inverse_pairs_core(arr, auxiliary_arr, 0, length - 1)
    return count


def test():
    arr1 = [7, 5, 6, 4]
    print(inverse_pairs(arr1))
    arr2 = [7, 5, 6, 6]
    print(inverse_pairs(arr2))


if __name__ == '__main__':
    test()