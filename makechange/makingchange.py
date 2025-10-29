def min_change(amount, coins, memo):

    if amount in memo:
        return memo[amount]

    if amount == 0:
        return 0

    if amount < 0:
        return float("inf")

    min_coin = float("-inf")

    for coin in coins:
        current_coin = 1 + min_change(amount - coin, coins, memo)
        memo[amount]= min(min_coin,current_coin)

    return memo[amount]

dict = {}
print(min_change(51, [1,2,3], dict))