# Uses python2


import sys


def get_fibonacci_last_digit(n):
    """Return the last digit of the nth number in the fibonacci numbers"""
    array = []

    array.append(0)
    array.append(1)

    for i in range(2, n + 1):
        last_digit = (array[i - 1] + array[i - 2]) % 10
        array.append(last_digit)

    return array[n]


if __name__ == '__main__':
    n = int(input())
    print get_fibonacci_last_digit(n)
