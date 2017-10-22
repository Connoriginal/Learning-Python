def mult(m,n):
    if n > 0:
        return m + mult(m,n-1)
    else:
        return 0

def mult1(m,n):
    def loop(n,ans):
        if n > 0:
            return loop(n-1,ans+m)
        else:
            return ans
    return loop(n,0)

def mult2(m,n):
    ans = 0
    while n > 0:
        ans += m
        n = n-1
    return ans

def double(n):
    return n*2

def halve(n):
    return n//2

def fastmult1(m,n):
    if n >0:
        if n % 2==0:
            return fastmult1(double(m),halve(n))
        else:
            return m + fastmult1(m,n-1)
    else:
        return 0

def fastmult2(m,n):
    def loop(m,n,ans):
        if n > 0:
            if n % 2 ==0:
                return loop(double(m),halve(n),ans)
            else:
                return loop(m,n-1,ans + m)
        else:
            return ans
    return loop(m,n,0)

def fastmult3(m,n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            m,n= double(m), halve(n)
        else:
            n -= 1
            ans += m
    return ans

def russianmult1(m,n):
    def loop(m,n):
        if n > 1:
            if n % 2 == 0:
                return loop(double(m), halve(n))
            else:
                return m + loop(double(m), halve(n))
        else:
            return m
    if n >0:
        return loop(m,n)
    else:
        return 0

def russianmult2(m,n):
    def loop(m,n,ans):
        if n > 1:
            if n % 2 == 0:
                return loop(double(m), halve(n), ans)
            else:
                return loop(double(m), halve(n), ans + m)
        else:
            return ans + m
    if n > 0:
        return loop(m,n,0)
    else:
        return 0

def russianmult3(m,n):
    ans = 0
    while n > 1:
        if n % 2 == 0:
            m, n = double(m), halve(n)
        else:
            ans += m
            m, n = double(m), halve(n)
    if n > 0:
        ans += m
        return ans
    else:
        return 0

print(russianmult2(57,86))
