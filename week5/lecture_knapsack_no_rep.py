"""
Knapsack(W)
initialize all value(0, j) <- 0
initialize all value(w, 0) <- 0

for i from 1 to n:
    for w from 1 to W:
        value(w, i) <- value(w, i - 1)
        if wi <= w:
            val <- value(w - wi, i - 1) + vi
            if value(w, i) < val:
                value(w, i) <- val
return value(W, n)

[ ][ ][ ][ ]
[ ][ ][ ][ ]
[ ][ ][ ][ ]
[ ][ ][ ][ ]

"""

def Knapsack(W):
    w = [2, 3, 4, 6]
    v = [9, 14, 16, 30]
    n = len(w)

    value = [[ 0 for i in range(0, n)] for i in range(0, W + 1)]

    for i in range(1, n):
        for j in range(1, W + 1):
            value[j][i] = value[j][i - 1]
            if w[i] <= j:
                val = value[j - w[i]][i - 1] + v[i]
                if value[j][i] < val:
                    value[j][i] = val

    return value[W][n - 1]


if __name__ == '__main__':
    print Knapsack(10)


# [
# [0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 14, 14, 14],
# [0, 14, 16, 16],
# [0, 14, 16, 16],
# [0, 14, 16, 30],
# [0, 14, 30, 30],
# [0, 14, 30, 30],
# [0, 14, 30, 44],
# [0, 14, 30, 46]
# ]
