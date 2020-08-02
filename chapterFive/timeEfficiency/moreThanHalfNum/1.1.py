'''
题目：
    数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
    例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
    由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
'''


'''
    如果数组是排好序的， 那么位于数组中间的元素就是超过数组长度一半的数字
'''
# time O(nlogn)
def more_than_half_num(arr):
    arr.sort()
    return arr[len(arr) // 2]


# time O(nlogn), space O(n)
# def more_than_half_num(arr):
#     a = sorted(arr)
#     return a[len(a) // 2]


def test():
    arr = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(more_than_half_num(arr))


if __name__ == '__main__':
    test()