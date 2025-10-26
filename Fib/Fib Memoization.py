def fib(memo, n):

    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        return n

    memo[n] = fib(memo, n - 1) + fib(memo, n - 2)

    return memo[n]

mem ={}

print(fib(mem,100))