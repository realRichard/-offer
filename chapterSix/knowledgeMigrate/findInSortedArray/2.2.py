# time O(logn)
def missing_number(arr):
    length = len(arr)
    left = 0
    right = length - 1
    while left <= right:
        middle = (left + right) // 2
        middle_data = arr[middle]
        if middle_data == middle:
            left = middle + 1
        elif middle == 0 or middle - 1 == arr[middle - 1]:
            return middle
        else:
            right = middle - 1
    # print(left, right, middle)
    if left == length:
        return length
    return -1


def test():
    arr1 = [0, 1, 2, 3, 4, 5, 6]
    print(missing_number(arr1))
    arr2 = [1, 2, 3, 4, 5, 6]
    print(missing_number(arr2))
    arr2 = [0, 1, 2, 4, 5, 6]
    print(missing_number(arr2))
    arr3 = [0]
    print(missing_number(arr3))


if __name__ == '__main__':
    test()