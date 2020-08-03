def total_numbers_of_digit(digit):
    if digit == 1:
        return 10
    return 9 * pow(10, digit - 1)


def begin_number(digit):
    if digit == 1:
        return 0
    return pow(10, digit - 1)


def digit_bit(num, index):
    while index > 1:
        num //= 10
        index -= 1
    return num % 10


def number_at_index(index, digit):
    # print(index, digit)
    number = begin_number(digit) + index // digit
    offset_from_right = digit - index % digit
    # print(number, offset_from_right)
    return digit_bit(number, offset_from_right)


def digit_at_index(n):
    if not isinstance(n, int):
        raise TypeError
    if n < 0:
        raise ValueError

    digit = 1
    while True:
        numbers = total_numbers_of_digit(digit)
        if n < numbers:
            return number_at_index(n, digit)
        n -= numbers
        digit +=1


def test():
    print(digit_at_index(0))
    print(digit_at_index(5))
    print(digit_at_index(13))
    print(digit_at_index(19))
    # print(total_numbers_of_digit(1))
    # print(total_numbers_of_digit(2))
    # print(total_numbers_of_digit(3))
    # print(total_numbers_of_digit(4))
    # print(digit_bit(12, 0))


if __name__ == '__main__':
    test()