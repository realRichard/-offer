'''
题目：
    从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
    2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王可以看成任意数字。
'''


def is_continuous(arr):
    if not isinstance(arr, list):
        raise TypeError
    if len(arr) != 5:
        raise ValueError

    arr.sort()
    number_of_zero = 0
    for i in arr:
        if i == 0:
            number_of_zero += 1
    number_of_gap = 0
    small = number_of_zero
    big = small + 1
    while big < len(arr):
        if arr[small] == arr[big]:
            return False
        number_of_gap += arr[big] - arr[small] - 1
        small = big
        big += 1
    return False if number_of_gap > number_of_zero else True


def test():
    arr = [1, 2, 4, 5, 0]
    print(is_continuous(arr))
    arr1 = [1, 2, 4, 5, 5]
    print(is_continuous(arr1))


if __name__ == '__main__':
    test()