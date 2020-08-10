# 更简洁的写法
def find_nums_appear_once(arr):
    result_exclusive_or = 0
    for i in arr:
        result_exclusive_or ^= i
    index_of_one = result_exclusive_or & (-result_exclusive_or)
    num1 = 0
    num2 = 0
    for i in arr:
        if i & index_of_one:
            num1 ^= i
        else:
            num2 ^= i
    return (num1, num2)


def test():
    arr = [2, 4, 3, 6, 3, 2, 5, 5]
    print(find_nums_appear_once(arr))


if __name__ == '__main__':
    test()