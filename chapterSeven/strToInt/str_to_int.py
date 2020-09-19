'''
题目：
    请你写一个函数StrToInt，实现把字符串转换成整数这个功能。
    当然，不能使用atoi或者其他类似的库函数。
'''


def str_to_int(s):
    valid = False
    num = 0
    # 判断空指针和空字符
    if isinstance(s, str) and s != '':
        valid = True
        minus = False
        # 判断符号， 这里如果是正数也必须带符号
        if s[0] == '-':
            minus = True
        elif s[0] == '+':
            minus = False
        else:
            valid = False
            return valid, num
        flag = -1 if minus else 1  
        zero = ord('0')
        nine = ord('9')
        for i in range(1, len(s)):
            digit = ord(s[i])
            if zero <= digit <= nine:
                num = 10 * num + flag * (digit - zero)
                # 溢出, 这里限制 int 32 位
                if (not minus and num > 0x7FFFFFFF) or (minus and num > 0x80000000):
                    num = 0
                    valid = False
                    break
            else:
                    num = 0
                    valid = False
                    break
    return valid, num


def test():
    s1 = '+123'
    print(str_to_int(s1))
    s2 = '-33'
    print(str_to_int(s2))
    s3 = '+0'
    print(str_to_int(s3))
    s4 = '+' + str(0x7FFFFFFF)
    print(str_to_int(s4))
    s5 = '-' + str(0x80000000)
    print(str_to_int(s5))
    s2 = None
    print(str_to_int(s2))
    s3 = ''
    print(str_to_int(s3))
    s4 = '+2j3'
    print(str_to_int(s4))


if __name__ == '__main__':
    test()