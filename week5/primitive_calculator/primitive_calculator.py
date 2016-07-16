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



n = 3
t = [1, 2, 3, 4, 5, 6, 7, 8]
o = [1, 1, 1, 2, 3, 2, 3, 4]

# SEPARATE index AND value were calculating for

def optimal_sequence(n):
    """return optimal sequence"""
    # Parallel arrays
    sequence = [1]
    min_ops = [0]

    index = 0
    current_value = 2

    while current_value <= n:
    # Calculate three possible step values
        print "\nCurrent Value: " + str(current_value)
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
            print "sequence operation 1"
            print sequence
            sequence.append(current_value)
            min_ops.append(c1_ops)

        elif min_operation[0] == 2:
            print "sequence operation 2"
            print "before backtrack"
            print sequence
            sequence = sequence[:(current_value / 2) - 1]
            print "after backtack"
            print sequence

            sequence.append(current_value)
            min_ops.append(c2_ops)

        elif min_operation[0] == 3:
            print "sequence operation 2"
            print "before backtrack"
            print sequence
            sequence = sequence[:(current_value) / 3]
            print "after backtack"
            print sequence

            sequence.append(current_value)

            min_ops.append(c3_ops)


        current_value += 1
        index += 1

    # print "index: " + str(index)
    print min_ops[index]
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
