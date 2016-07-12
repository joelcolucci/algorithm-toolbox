"""
Input:  money
        coins = [6, 5, 1]


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

def dp_change(n, coins):
    """Return minimum number of coins needed"""
    min_num_coins = [0]

    for i in range(1, n + 1):
        min_num_coins.append(min_num_coins[i - 1] + 1)
        for j in range(0, len(coins)): # For each coin
            if i >= coins[j]:
                num_coins = min_num_coins[i - coins[j]] + 1
                if num_coins < min_num_coins[i]:
                    min_num_coins[i] = num_coins

    return min_num_coins[n]


if __name__ == '__main__':
    print dp_change(2000, [1, 4, 5, 10])
