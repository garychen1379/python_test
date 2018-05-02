n = eval(input())
lst = []

for i in range(n,0,-1):
    lst.append(i)
    print('data',i)

print()

for i in range(1,n+1,1):
    print('data',lst.pop())
