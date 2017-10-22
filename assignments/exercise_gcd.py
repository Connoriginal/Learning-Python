def gcd(m,n):
    if n != 0:
        return gcd(n,m%n)
    else:
        return abs(m)

def gcd1_1(m,n):
    while n!=0:
        print("gcd1_1",m,n)
        m , n = n, m%n
    return abs(m)

def gcd1_2(m,n):
    print("gcd1_2")
    def loop(m,n,k):
        print("gcd1_2," ,"loop",m,n,k)
        if not (m ==0 or n==0):
            if m % 2==0 and n % 2 ==0:
                return loop(m//2, n//2, k*2)
            elif m % 2 == 0 and n % 2 ==1:
                return loop(m//2, n , k)
            elif m % 2 == 1 and n% 2 == 0:
                return loop(m, n//2, k)
            elif m <= n:
                return loop(m, (n-m)//2,k)
            else:
                return loop(n,(m-n)//2,k)
        else:
            if m == 0:
                return abs(n*k)
            else:
                return abs(m*k)
    return loop(m,n,1)

def gcd1_3(m,n):
    k = 1
    print("gcd1_3")
    while not (m==0 or n==0):
        print("gcd1_3,","while",m,n,k)
        if m %2==0 and n % 2==0:
            m,n,k= m//2, n//2, k*2
        elif m % 2 ==0 and n% 2 ==1:
            m, n, k= m//2, n, k
        elif m%2 ==1 and n % 2 == 0:
            m, n, k= m, n//2, k
        elif m <= n:
            n = (n-m)//2
        else:
            m, n = n, (m-n)//2
    if m == 0:
        return abs(k*n)
    else:
        return abs(k*m)



print(gcd1_1(18,48))
print(gcd1_2(18,48))
print(gcd1_3(18,48))
