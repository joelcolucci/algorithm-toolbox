# Uses python3
import sys

"""
A natural subproblem in this case is the following:
C(n) is the minimum number of operations
required to obtain n from 1 (using the three primitive operations).

How to express C(n) through C(n/3), C(n/2), C(n - 1)?

QUESTION How many operations required to go from C(n - 1) to C(n)?
ANSWER 1 more operation because we can use the +1 op

http://d.pr/i/4r7V
"""
"""
DPChange(money, coins)
MinNumCoins(0) <- 0

for m from 1 to money:
    MinNumCoins(m) <- infinity
    for i from 1 to |coins|:
        if m >= coin:
            NumCoins <- MinNumCoins(m - coin) + 1
            if NumCoins < MinNumCoins(m):
                MinNumCoins(m) <- NumCoins

return MinNumCoins(money)
"""

n = 3
t = [1, 2, 3, 4, 5, 6, 7, 8]
o = [0, 1, 1, 2, 3, 2, 3, 3]

# SEPARATE index AND value were calculating for

def optimal_sequence(N):
    """return optimal sequence"""
    min_num_ops = [0, 0]

    for i in range(2, N + 1):
        min_num_ops.append(min_num_ops[i - 1] + 1)

        if i % 2 == 0:
            num_ops = min_num_ops[(i / 2)] + 1
            if num_ops < min_num_ops[i]:
                min_num_ops[i] = num_ops

        if i % 3 == 0:
            num_ops = min_num_ops[(i / 3)] + 1
            if num_ops < min_num_ops[i]:
                min_num_ops[i] = num_ops

    return min_num_ops[N]



if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print optimal_sequence(n)
    #sequence = list(optimal_sequence(n))
    # print(len(sequence) - 1)
    # for x in sequence:
    #     print str(x) + " "
