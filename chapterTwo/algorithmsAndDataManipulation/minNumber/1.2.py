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

    start = 0
    end = len(arr) - 1
    middle = start
    # if the first < the last, means arr already sorted, return the first directly 
    while arr[start] >= arr[end]:
        if end - start == 1:
            middle = end
            break
        middle = (start + end) // 2
        # if the first the midlle, the last are equal
        # we can not determine the middle 
        # but to sequential search
        if arr[start] == arr[end] and arr[middle] == arr[start]:
            return min(arr)
        if arr[middle] >= arr[start]:
            start = middle
        else:
            end = middle
    return arr[middle]


def test():
    l = [3, 4, 5, 6, 1]
    print(my_min(l))
    a = [8, 9, 100, 2, 3, 4, 5]
    print(my_min(a))
    # spercial test case
    b = [1, 1, 1, 0, 1]
    print(my_min(b))


if __name__ == '__main__':
    test()