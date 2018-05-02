a = eval(input())
b = eval(input())
c = eval(input())

s = a+b+c
ave = s/3
pro = a*b*c

print('sum is',s)
print('average is %.2f'%(ave))
print('product is',pro)

if a >= b:
    if b >= c:
        print('smallest is',c)
    else:
        print('smallest is',b)
else:
    if a >= c:
        print('smallest is',c)
    else:
        print('smallest is',a)


if a >= b:
    if a >= c:
        print('largest is',a)
    else:
        print('largest is',c)
else:
    if b >= c:
        print('largest is',b)
    else:
        print('largest is',c)
