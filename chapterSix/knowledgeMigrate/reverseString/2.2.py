def my_reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def left_rotate_string(string, n):
    length = len(string)
    arr = list(string)
    start = 0
    end = length - 1
    my_reverse(arr, start, end)
    my_reverse(arr, start, end - n)
    my_reverse(arr, end - n + 1, end)
    return ''.join(arr)


def test():
    string = 'abcdefg'
    print(left_rotate_string(string, 2))


if __name__ == '__main__':
    test()