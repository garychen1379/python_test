import math

n = eval(input())

print('Original: %.2f'%(n))

m = math.sqrt(n)*10
d = m - n

print('Adjusted: %.2f(+%.0f)'%(m,d))
