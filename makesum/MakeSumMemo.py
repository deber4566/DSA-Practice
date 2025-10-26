def makesum(sum, arr, memo):

    if sum in memo:
        return memo[sum]

    if sum == 0:
        return True

    if sum < 0:
        return False

    for num in arr:
        memo[sum] = makesum(sum - num, arr, memo)
        if memo[sum] == True:
            return True

    memo[sum] = False
    return memo[sum]


memo = {}
print(makesum(1001,[2,3,5,7], memo))