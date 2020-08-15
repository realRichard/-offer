# 创新的解法
def last_remaining(n, m):
    if n < 1 or m < 1:
        return -1
    last = 0
    for i in range(2, n + 1):
        last = (last + m) % i
    return last


def test():
    print(last_remaining(5, 3))


if __name__ == '__main__':
    test()