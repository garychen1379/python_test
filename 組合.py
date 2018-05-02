def fac(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total

def C(n,m):
    return fac(n)/(fac(m)*fac(n-m))

a = eval(input())
b = eval(input())
print(int(P(a,b)))
