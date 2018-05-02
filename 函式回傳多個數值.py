def fac_sum1(n):
    tf = 1
    ts = 0
    for i in range(1,n+1):
        tf *= i
        ts += i
    return tf,ts

x = eval(input())
ans = fac_sum1(x)
print(ans[0])
print(ans[1])
