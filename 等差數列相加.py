a1 = eval(input())
d = eval(input())
n = eval(input())

t = (2*a1 + d*(n-1))*n/2

for i in range(1,n+1):
    an = a1 + (i-1)*d
    if i == n:
        if an < 0:
            print('(%s) = '%(an),end='')
        else:
            print('%s = '%(an),end='')
    else:
        if an < 0:
            print('(%s) + '%(an),end='')
        else:
            print('%s + '%(an),end='')

print('%d'%(t),sep='',end='')



