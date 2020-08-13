def my_reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def reverse_sentence(string):
    length = len(string)
    start = 0
    end = length - 1
    arr = list(string)
    my_reverse(arr, start, end)
    start = 0
    end = 0
    while end < length:
        if arr[start] == ' ':
            start += 1
            end += 1
        elif arr[end] == ' ':
            end -= 1
            my_reverse(arr, start, end)
            end += 1
            start = end
        else:
            end += 1
    return ''.join(arr)


def test():
    string = 'I am a student.'
    print(reverse_sentence(string))


if __name__ == '__main__':
    test()