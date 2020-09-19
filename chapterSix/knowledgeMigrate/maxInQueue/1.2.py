import collections


def max_in_windows(arr, size):
    max_in_windows = []
    if arr is not None and 1 <= size <= len(arr):
        index = collections.deque()
        for i in range(size):
            while len(index) > 0 and arr[i] >= arr[index[-1]]:
                index.pop()
            index.append(i)
        for i in range(size, len(arr)):
            max_in_windows.append(arr[index[0]])
            while index and arr[i] >= arr[index[-1]]:
                index.pop()
            if index and index[0] <= i -size:
                index.popleft()
            index.append(i)
        max_in_windows.append(arr[index.popleft()])
    # 多余
    # else:
    #     return []
    return max_in_windows


def test():
    arr = [2, 3, 4, 2, 6, 2, 5, 1]
    print(max_in_windows(arr, 3))


if __name__ == '__main__':
    test()