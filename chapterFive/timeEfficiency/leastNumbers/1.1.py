'''
题目：
    输入n个整数，找出其中最小的K个数。
    例如输入4,5,1,6,2,7,3,8这8个数字， 则最小的4个数字是1,2,3,4,。
'''


'''
    最简单的思路把输入的 n 个整数排序， 
    排序之后位于最前面的 k 个数就是最小的 k 个数
'''
# time O(nlogn)
def least_numbers(arr, k):
    arr.sort()
    return arr[:k]


def test():
    arr = [4, 5, 1, 6, 2, 7, 3, 8]
    least = least_numbers(arr, 4)
    print(least)


if __name__ == '__main__':
    test()