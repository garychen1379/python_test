n1 = eval(input())
n2 = eval(input())
s = input()

if s == '+':
    print('%.2f + %.2f = %.2f'%(n1,n2,n1+n2))
elif s == '-':
    print('%.2f - %.2f = %.2f'%(n1,n2,n1-n2))
elif s == '*':
    print('%.2f * %.2f = %.2f'%(n1,n2,n1*n2))
else:
    print('%.2f / %.2f = %.2f'%(n1,n2,n1/n2))
