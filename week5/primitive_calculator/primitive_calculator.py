# Uses python2
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

    return create_optimal_sequence(N, min_num_ops)


def create_optimal_sequence(N, min_num_ops):
    sequence = [N]
    cur_val = N
    i = 1

    while cur_val > 0:
        min_op = min_num_ops[cur_val - 1]

        sequence.append(cur_val - 1)
        updated_val = cur_val - 1

        if cur_val % 2 == 0:
            if min_num_ops[cur_val / 2] < min_op:
                sequence[i] = cur_val / 2
                updated_val = cur_val / 2

        if cur_val % 3 == 0:
            if min_num_ops[cur_val / 3] < min_op:
                sequence[i] = cur_val / 3
                updated_val = cur_val / 3

        cur_val = updated_val
        i += 1

    sequence.reverse()
    return sequence[1:]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print str(x) + " "
