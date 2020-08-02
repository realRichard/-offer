# time O(n)
def more_than_half_num(arr):
    if not isinstance(arr, list):
        raise TypeError
    for i in arr:
        if not isinstance(i, int):
            raise ValueError

    num = None
    times = 0
    for i in arr:
        if i == num:
            times += 1
        else:
            if times == 0:
                num = i
                times = 1
            else:
                times -= 1

    count = 0
    for i in arr:
        if i == num:
            count += 1

    if not count > len(arr) // 2:
        return None

    return num


def test():
    arr = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(more_than_half_num(arr))


if __name__ == '__main__':
    test()