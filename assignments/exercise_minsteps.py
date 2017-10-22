def minsteps(n):
    memo = [0] * (n+1)
    for i in range(2,n+1):
        memo[i] = 1 + memo[i-1]
        if i % 3 == 0:
            memo[i] = min(memo[i], 1 + memo[i//3])
        if i % 2 ==0:
            memo[i] = min(memo[i], 1 + memo[i//2])
    return memo[n]
