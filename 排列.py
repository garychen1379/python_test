def fac(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total

def P(n,m):
    return fac(n)/fac(n-m)

a = eval(input())
b = eval(input())
print(int(P(a,b)))
