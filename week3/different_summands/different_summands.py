# Uses python2
import sys


def optimal_summands_brute(n):
    """Return"""
    if n == 1 or n == 2:
        return [n]

    summands = []
    total = 0

    for i in range(1, n):
        if total + i == n:
            summands.append(i)
            total += i
            break
        elif total + (i * 2) < n:
            summands.append(i)
            total += i

    return summands


def optimal_summands_recursive(n):
    """Return"""
    if n == 1 or n == 2:
        return [n]

    summands = []
    helper(n, 1, summands)

    return summands


def helper(k, l, summands):
    """Return"""
    # k as a sum of as many pairwise distinct integers
    # l - constrain/ignore guesses
    if l > k:
        return

    if k <= (l * 2):
        #return k
        summands.append(k)
    elif k >= (l * 2):
        # Safe to add l to summands as it doesnt overflow
        #return l
        summands.append(l)

    helper(k - l, l + 1, summands)


def optimal_summands_with_comments(n):
    """Return"""
    if n == 1 or n == 2:
        return [n]

    summands = []
    k = n
    l = 1

    while l <= k:
        if k <= (l * 2):
            summands.append(k)
        elif k >= (l * 2):
            # Safe to add l to summands as it doesnt overflow k
            summands.append(l)
        # Set iterators
        k = k - l
        l = l + 1

    return summands


def optimal_summands(n):
    """Return"""
    if n == 1 or n == 2:
        return [n]

    summands = []
    k = n
    l = 1

    while l <= k:
        if k <= (l * 2):
            summands.append(k)
        elif k >= (l * 2):
            summands.append(l)
        k = k - l
        l = l + 1

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print str(x) + ' '
