n = eval(input())

print((n-1)*' ','*',sep='')


for i in range(-1,2*(n-1-2),2):
    for j in range(1,4):
        print((n-((2*j+i)//2+1))*' ',(2*j+i)*'^',sep='')

for k in range(1,n-1):
    print((n-n//2)*' ',(n-2)*'#',sep='')
