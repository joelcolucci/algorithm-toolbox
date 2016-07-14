# Uses python2


def get_fibonaccihuge(n, m):
    # Determine periodic segment
    period = [0, 1, 1, 2, 0, 2, 2, 1]

    # Determine length of the periodic segment is
    period_len = len(period)

    # Determine remainder/place in sequence
    remainder = n % period_len

    # Return value
    return remainder % m


if __name__ == '__main__':
    a, b = [int(i) for i in raw_input().split()]

    print get_fibonaccihuge(a, b)


"""
I used 2 facts about the Fibonacci modulus (I've found online):

1) The Fibonacci sequence mod m is periodic, with period less than m^2;

2) Each Pisano period starts with 01 and then does not have 01 repeated (you can rely on the fact that when you see next 01, it means the next period has started.)

3) The fact from the instructions: Fn mod m = Fr mod m, where r = n % pisanoPeriodLength; (Ex.: F2015 mod 3 = F7 mod 3 = 1)

So the algorithm:

Step 1: Find pisanoPeriodLength by iterating from 0 to m^2-1 and calculating Fi % m without calculating the Fi itself ( F(i+2) mod m = F(i) mod m + F(i+1) mod m );

As soon as you get F(i) mod m = 0 and F(i+1) mod m = 1, exit the loop (you've started the new Pisano Period).

Step 2: You know the pisanoPeriodLength now so you can use the fact 3) from above to calculate Fn mod m.
"""
