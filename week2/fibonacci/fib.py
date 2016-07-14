# Uses python2
def calc_fib(n):
    """Return the nth number in the fibonacci numbers"""
    array = []

    array.append(0)
    array.append(1)

    for i in range(2, n + 1):
        array.append(array[i - 1] + array[i - 2])

    return array[n]


n = int(input())
print calc_fib(n)
