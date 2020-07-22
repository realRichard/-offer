'''
题目：
    输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列{1,2，3，4,5}是
    某栈的压栈序列，序列{4,5,3,2,1}是该压栈序列对应的一个弹出序列，但{4,3,5,1,2}就不可能是该压栈序列的弹出序列。
'''


def is_pop_order(push_order, pop_order):
    if not isinstance(push_order, list) or not isinstance(pop_order, list):
        raise TypeError
    for i in push_order:
        if not isinstance(i, int):
            raise ValueError
    for i in pop_order:
        if not isinstance(i, int):
            raise ValueError

    result = False
    if len(push_order) != len(pop_order):
        return result
    assist_stack = []
    while len(pop_order) != 0:
        top = pop_order[0]
        if len(assist_stack) != 0 and top == assist_stack[-1]:
            pop_order.pop(0)
            assist_stack.pop(-1)
        else:
            if len(push_order) == 0:
                return result
            else:
                assist_stack.append(push_order.pop(0))
    result = True
    return result


def test():
    p1 = [1, 2, 3, 4, 5]
    p2 = [4, 5, 3, 2, 1]
    p3 = [4, 3, 5, 1, 2]
    print(is_pop_order(p1, p2))
    print(is_pop_order(p1, p3))


if __name__ == '__main__':
    test()
