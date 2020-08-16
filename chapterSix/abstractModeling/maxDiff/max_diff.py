'''
题目：
    假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖交易该股票可能获得的利润是多少？
    例如一只股票在某些时间节点的价格为{9, 11, 8, 5, 7, 12, 16, 14}。
    如果我们能在价格为5的时候买入并在价格为16时卖出，则能收获最大的利润11。
'''


def max_diff(arr):
    if not isinstance(arr, list):
        raise TypeError
    for i in arr:
        if not isinstance(i, int):
            raise ValueError
    if len(arr) < 2:
        return 0

    buy_in = arr[0]
    max_diff = arr[1] - buy_in
    for i in range(2, len(arr)):
        if arr[i - 1] < buy_in:
            buy_in = arr[i - 1]
        diff = arr[i] - buy_in
        if diff > max_diff:
            max_diff = diff
    return max_diff


def test():
    arr = [9, 11, 8, 5, 7, 12, 16, 14]
    print(max_diff(arr))


if __name__ == '__main__':
    test()