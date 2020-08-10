'''
题目：
    输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。
    例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以结果打印出3个连续序列1～5、4～6和7～8。
'''


def print_continuous_sequence(small, big):
    for i in range(small, big + 1):
        print(i, end=', ')
    print()


def find_continuous_sequence(s):
    small = 1
    big = 2
    middle = (1 + s) // 2
    current_sum = small + big
    while small <= middle:
        if current_sum == s:
            print_continuous_sequence(small, big)
        if current_sum < s:
            big += 1
            current_sum += big
        else:
            current_sum -= small
            small += 1


def test():
    find_continuous_sequence(15)


if __name__ == '__main__':
    test()