# Uses python3
import sys


def greedy_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def reverse_greedy_sequence(n):
    """return optimal sequence"""
    sequence = [1]

    for i in range(1, n + 1):
        prev_val = sequence[i - 1]

        if prev_val == n:
            break
        elif prev_val * 3 <= n:
            sequence.append(prev_val * 3)
            i = prev_val * 3
        elif prev_val * 2 <= n:
            sequence.append(prev_val * 2)
            i = prev_val * 2
        else:
            sequence.append(prev_val + 1)
            i = prev_val + 1

    return sequence

"""
Your goal is given a positive integer n,
find the minimum number of operations needed to obtain
the number n starting from the number 1.
"""

# What is the minimum number of coins to form n -1 1 and adding 1 coins

# Only one possibility to arrive at this number from the previous number

# OUTPUT:
    # In the first line, output the minimum number k of operations needed to get n from 1.
    # In the second line output a sequence of intermediate numbers.

"""
A natural subproblem in this case is the following:
C(n) is the minimum number of operations
required to obtain n from 1 (using the three primitive operations).

How to express C(n) through C(n/3), C(n/2), C(n - 1)?

QUESTION How many operations required to go from C(n - 1) to C(n)?
ANSWER 1 more operation because we can use the +1 op
"""

n = 3
t = [1, 2, 3, 4, 5, 6]
o = [1, 1, 1, 2, 3, 2]

# SEPARATE index AND value were calculating for

# Compute

def optimal_sequence(n):
    """return optimal sequence"""
    # Parallel arrays
    sequence = [1]
    min_ops = [0]

    index = 0
    current_value = 2

    while current_value <= n:
        # Calculate three possible step values

        # Possibility #1 - Add one
        c1_ops = min_ops[index] + 1
        min_operation = (1, c1_ops)

        # Possibility #2 - Multiply by 2
        if current_value % 2 == 0:
            c2_ops = min_ops[(current_value / 2) - 1] + 1

            if c2_ops < min_operation[1]:
                min_operation = (2, c2_ops)

        # Possibility #3 - Multiply by 3
        if current_value % 3 == 0:
            c3_ops = min_ops[(current_value / 3) - 1] + 1

            if c3_ops < min_operation[1]:
                min_operation = (3, c3_ops)

        # Write minimum operation
        if min_operation[0] == 1:
            sequence.append(current_value)
            min_ops.append(c1_ops)

        elif min_operation[0] == 2:
            sequence = sequence[:(current_value / 2)]
            sequence.append(current_value)
            min_ops.append(c2_ops)

        elif min_operation[0] == 3:
            sequence = sequence[:(current_value / 3)]
            sequence.append(current_value)
            min_ops.append(c3_ops)

        current_value += 1
        index += 1

    # print "index: " + str(index)
    print min_ops[index]
    # print sequence

    #print "\n"
    return sequence



def optimal_sequence_operations(n):
    """return optimal sequence"""
    # Parallel arrays
    sequence = [1]
    min_ops = [0]

    index = 0
    current_value = 2

    while current_value <= n:
        # Calculate three possible step values

        # Possibility #1 - Add one
        c1_ops = min_ops[index] + 1
        min_operation = (1, c1_ops)

        # Possibility #2 - Multiply by 2
        if current_value % 2 == 0:
            c2_ops = min_ops[(current_value / 2) - 1] + 1

            if c2_ops < min_operation[1]:
                min_operation = (2, c2_ops)

        # Possibility #3 - Multiply by 3
        if current_value % 3 == 0:
            c3_ops = min_ops[(current_value / 3) - 1] + 1

            if c3_ops < min_operation[1]:
                min_operation = (3, c3_ops)

        # Write minimum operation
        if min_operation[0] == 1:
            sequence.append(sequence[index] + 1)
            min_ops.append(c1_ops)
        elif min_operation[0] == 2:
            sequence = sequence[:(index / 2)]
            sequence.append(current_value)
            sequence.append(sequence[index / 2] * 2)
            min_ops.append(c2_ops)
        elif min_operation[0] == 3:
            sequence.append(sequence[index / 3] * 3)
            min_ops.append(c3_ops)

        current_value += 1
        index += 1

        #print "index: " + str(index)
    print min_ops
    print sequence

    #print "\n"
    return sequence

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    # print(len(sequence) - 1)
    # for x in sequence:
    #     print str(x) + " "


# def optimal_sequence(n):
#     """return optimal sequence"""
#     if n == 1:
#         return [1]
#
#     if n == 2:
#         # 1 operation required
#         # 2 possibilities
#             # + 1
#             # * 2
#         return [1, 2]
#
#     if n == 3:
#         # 1 operation required
#         # 1 possibility
#             # * 3
#         return [1, 3]
#
#     if n == 4:
#         # 2 operations required
#         # 2 possibilities
#             # * 2 * 2
#             # * 3 + 1
#         return [1, 2, 4]
