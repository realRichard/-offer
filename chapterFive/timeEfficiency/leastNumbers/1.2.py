'''
解法二：
    时间复杂度为O(nlogk)的算法，特别适合处理海量数据
'''
import heapq


def least_numbers(arr, k):
    if not isinstance(arr, list) or not isinstance(k, int):
        raise TypeError
    if k <= 0 or k > len(arr):
        raise ValueError
    for i in arr:
        if not isinstance(i, int):
            raise ValueError

    heaps = []
    result = []
    for i in arr:
        heapq.heappush(heaps, i)
    for i in range(k):
        result.append(heapq.heappop(heaps))
    return result


def test():
    arr = [4, 5, 1, 6, 2, 7, 3, 8]
    least = least_numbers(arr, 4)
    print(least)


if __name__ == '__main__':
    test()