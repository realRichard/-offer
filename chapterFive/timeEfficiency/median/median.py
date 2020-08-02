'''
题目：
    如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
    那么中位数就是所有数值排序之后位于中间的数值。
    如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''
import heapq


class Solution:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def insert(self, num):
        if not isinstance(num, int):
            raise TypeError

        if len(self.max_heap) <= len(self.min_heap):
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        if len(self.min_heap) > 0 and len(self.max_heap) > 0:
            if -self.max_heap[0] > self.min_heap[0]:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def median(self):
        if len(self.max_heap) > len(self.min_heap):
            median = -heapq.heappop(self.max_heap)
        else:
            median = (-heapq.heappop(self.max_heap) + heapq.heappop(self.min_heap)) / 2
        return median


def test():
    s = Solution()
    s.insert(1)
    s.insert(2)
    s.insert(3)
    s.insert(4)
    s.insert(5)
    s.insert(6)
    print(s.median())


if __name__ == '__main__':
    test()