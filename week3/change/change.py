# Uses python2


def get_change_naive(n):
    #write your code here
    converted_value = 0
    remaining_value = n

    num_of_10_coin = 0
    num_of_5_coin = 0
    num_of_1_coin = 0

    if remaining_value >= 10:
        num_of_10_coin = n / 10
        converted_value = num_of_10_coin * 10
        remaining_value = n - converted_value

    if remaining_value >= 5:
        num_of_5_coin = remaining_value / 5
        converted_value += num_of_5_coin * 5
        remaining_value = n - converted_value

    num_of_1_coin = remaining_value / 1
    converted_value += num_of_1_coin * 1
    remaining_value = n - converted_value

    return num_of_10_coin + num_of_5_coin + num_of_1_coin


def get_change(n):
    coins = [10, 5, 1]

    value_remaining = n
    total_coins = 0

    for i in range(0, len(coins)):
        cur_coin = coins[i]
        num_cur_coin = value_remaining / cur_coin

        value_remaining -= num_cur_coin * cur_coin
        total_coins += num_cur_coin

    return total_coins


if __name__ == '__main__':
    n = int(input())
    print get_change(n)
