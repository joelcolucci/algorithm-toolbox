# Uses python2
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.0

    # Calculate unit value
    unit_values = []
    for i in range(0, len(weights)):
        unit_value = float(values[i]) / float(weights[i])
        unit_values.append((unit_value, weights[i]))
    # Sort in descending order; Max unit value first
    unit_values.sort(key=lambda tup: tup[0], reverse=True)

    # # While capacity is not full
    for i in range(0, len(unit_values)):
        if capacity == 0:
            break

        unit_value = unit_values[i][0]
        amount_available = unit_values[i][1]

        if capacity >= amount_available:
            value += amount_available * unit_value
            capacity -= amount_available
        elif capacity < amount_available:
            value += capacity * unit_value
            capacity -= capacity

    return value


if __name__ == "__main__":
    data = [int(i) for i in sys.stdin.read().split()]
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    # print "capacity: " + str(capacity)
    # print "values: " + str(values)
    # print "weights: " + str(weights)

    opt_value = get_optimal_value(capacity, weights, values)
    print "{:.10f}".format(opt_value)
