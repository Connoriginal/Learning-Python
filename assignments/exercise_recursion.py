def minsteps(n):
    memo = [0] * (n+1)
    for i in range(0,n+1):
        if i > 1:
            memo[i] = 1 + memo[i-1]
            if i % 2 == 0:
                check = 1 + memo[i//2]
                if check < memo[i]:
                    memo[i] = check
            if i % 3 == 0:
                check = 1 + memo[i//3]
                if check < memo[i]:
                    memo[i] = check
    return memo[n]
