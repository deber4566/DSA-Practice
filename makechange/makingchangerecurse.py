def minchange(amount, coins):

    if amount < 0:
        return float("inf")

    if amount == 0:
        return 0

    min_coin = float("inf")

    for coin in coins:
        current = 1 + minchange(amount - coin, coins)
        min_coin = min(min_coin, current)

    return min_coin


print(minchange(15, [1, 2, 3], ))