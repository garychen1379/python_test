n = eval(input())
k = n//2 + 1

for i in range(0,k):
    print((k-i-1)*' ',(2*i+1)*'*',sep='')
for i in range(k-2,-1,-1):
    print((k-i-1)*' ',(2*i+1)*'*',sep='')

