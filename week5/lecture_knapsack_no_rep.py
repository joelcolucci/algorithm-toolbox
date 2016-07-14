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


"""
