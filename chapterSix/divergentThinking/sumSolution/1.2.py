def sum_solution(n):
    return n and n + sum_solution(n - 1)


def test():
    print(sum_solution(100))


if __name__ == '__main__':
    test()