'''n = eval(input())
total = 0
for i in range(n+1):
    total += i
print(total)'''

'''n = eval(input())
total = 1
for i in range(1,n+1):
    total *= i
print(total)'''

n = eval(input())
total = 0
for i in range(1,n+1):
    total += i
    print(i,end="")
    if i == n:
        print("",end="")
    else:
        print("+",end="")
print(" =",total)
 

