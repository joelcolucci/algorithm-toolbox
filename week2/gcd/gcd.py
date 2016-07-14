# Uses python2


def gcd(a, b):
    """Calculate GCD for input a,b"""
    if b == 0:
        return a

    a = a % b

    return gcd(b, a)


if __name__ == "__main__":
    a, b = [int(i) for i in raw_input().split()]

    print gcd(a, b)
