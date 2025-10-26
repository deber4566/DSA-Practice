def makesum(sum, numbers):

    arr = [False] * (sum + 1)

    arr[0] = True

    for i in range(len(arr)):
        if arr[i] == True:
            for num in numbers:
                if (i + num) < len(arr):
                    arr[i + num] = True

    print(arr)

    return arr[sum]


makesum(18,[19,5,7])

