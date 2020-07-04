from utils import (
    log,
    ensure,
)


def count(arr, start, end):
    count = 0
    for i in arr:
        if i >= start and i <= end:
            count += 1
    return count


# 把从1~n的数字从中间的数字m分为两部分，前面一半为1~m，后面一半为m+1~n。如果1~m的数字的数目超过m，那么这一半的
# 区间里一定包含重复的数字：否则，另一半m+1~n的区间里一定包含重复的数字。
# 时间O（nlogn）空间O(1)
def duplicate(arr):
    if not isinstance(arr, list):
        return (False,)

    length = len(arr)
    if length == 0:
        return (False,)
    for i in arr:
        if not isinstance(i, int) or i < 1 or i > length - 1:
            return (False,)

    start = 1
    end = length - 1
    while end >= start:
        middle = (start + end) // 2
        c = count(arr, start, middle)
        log(c, start, middle, end)
        if start == end:
            if c > 1:
                return (True, start)
            else:
                break
        if c > middle - start + 1:
            end = middle
        else:
            start = middle + 1
    return (False,)


def test():
    # test case,
    # 此方法有缺陷，不能找出所有的重复的数字，
    # 因为在1~2的范围里有1和2两个数字，这个范围的数字也出现两次，
    # 不能确定是每个数字各出现一次还是某个数字出现了两次
    arr1 = [2, 3, 5, 4, 3, 2, 6, 7]
    arr2 = [5, 4, 3, 2, 1, 0]
    arr3 = [1, 2, 3, 4, 4]
    arr4 = []
    result1 = duplicate(arr1)
    ensure(result1[0] == True and result1[1] in (2, 3), 'arr1')
    result2 = duplicate(arr2)
    ensure(result2[0] == False, 'arr2')
    result3 = duplicate(arr3)
    ensure(result3[0] == True and result3[1] in (4,), 'arr3')
    result4 = duplicate(arr4)
    ensure(result4[0] == False, 'arr4')


if __name__ == '__main__':
    test()