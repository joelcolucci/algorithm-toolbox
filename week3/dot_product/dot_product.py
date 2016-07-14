#Uses python3

import sys

def min_dot_product(a, b):
    # Sort a ascending
    a.sort()
    # Sort b descending
    b.sort(reverse=True)

    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    data = [int(i) for i in sys.stdin.read().split()]
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(min_dot_product(a, b))
