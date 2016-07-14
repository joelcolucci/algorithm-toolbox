# Uses python2
import sys


def lcm(a, b):
    """Return LCM of a,b"""
    #write your code here
    gcd_val = gcd(a, b)

    product = a * b

    return product / gcd_val


def gcd(a, b):
    """Calculate GCD for input a,b"""
    if b == 0:
        return a

    a = a % b

    return gcd(b, a)


if __name__ == '__main__':
    a, b = [int(i) for i in raw_input().split()]

    print lcm(a, b)
