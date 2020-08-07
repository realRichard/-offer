'''
题目：
    统计一个数字在排序数组中出现的次数。
    例如，输入排序数组{1,2,3,3,3,3,4,5,}和数字3，由于3在这个数组中出现了4次，因此输出4。
'''


def first_k(sorted_arr, length, k, start, end):
    if start > end:
        return -1
    middle = (start + end) // 2
    middle_data = sorted_arr[middle]
    if middle_data == k:
        if middle == 0 or sorted_arr[middle - 1] != k:
            return middle
        else:
            end = middle - 1
    elif middle_data > k:
        end = middle - 1
    else:
        start = middle + 1
    return first_k(sorted_arr, length, k, start, end)


def last_k(sorted_arr, length, k, start, end):
    if start > end:
        return -1
    middle = (start + end) // 2
    middle_data = sorted_arr[middle]
    if middle_data == k:
        if middle == length - 1 or sorted_arr[middle + 1] != k:
            return middle
        else:
            start = middle + 1
    elif middle_data > k:
        end = middle - 1
    else:
        start = middle + 1
    return last_k(sorted_arr, length, k, start, end)


def number_of_k(sorted_arr, k):
    if not isinstance(sorted_arr, list) or not isinstance(k, int):
        raise TypeError
    for i in sorted_arr:
        if not isinstance(i, int):
            raise ValueError

    length = len(sorted_arr)
    end = length - 1
    first = first_k(sorted_arr, length, k, 0, end)
    last = last_k(sorted_arr, length, k, 0, end)
    number = 0
    # print(first, last)
    if first != -1 and last != -1:
        number = last - first + 1
    return number


def test():
    sorted_arr = [1, 2, 3, 3, 3, 3, 4, 5]
    print(number_of_k(sorted_arr, 3))


if __name__ == '__main__':
    test()