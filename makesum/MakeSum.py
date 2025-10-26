def makesum(sum, numbers):

    if sum == 0:
        return True

    if sum < 0:
        return False

    for num in numbers:
        if makesum(sum - num, numbers) == True:
            return True

    return False



print(makesum(101, [2,3,5,7]))