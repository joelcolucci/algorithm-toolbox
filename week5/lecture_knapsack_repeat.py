"""
Knapsack(W)

value(0) <- 0
for w from 1 to W:
    value(w) <- 0
    for i from 1 to n:
        if wi <= w:
            val <- value(w - wi) + vi
            if val > value(w):
                value(w) <- val

return value(W)

Item Weight Value
1    6      $30
2    3      $14
3    4      $16
4    2      $9

"""
# W - total max weight W that knapsack will hold
# n - number of items to pick from
# w - weights to pick from
# v - values of each weight

def knapsack_with_repetitions(W):
    """Return greatest value to fill knapsack"""
    w = [2, 3, 4, 6]
    v = [9, 14, 16, 30]

    n = len(w)

    value = [0]

    for i in range(1, W + 1):
        value.append(0)

        for j in range(0, n):
            if w[j] <= i:
                val = value[i - w[j]] + v[j]
                if val > value[i]:
                    value[i] = val # The maximal value of knapsack of weight w

    return value[W] # The maximal value of knapsack of weight w


if __name__ == '__main__':
    print knapsack_with_repetitions(10)
