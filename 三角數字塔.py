s = eval(input())
n =0
for i in range(1,s+1):
    for j in range(1,i+1):
        n += 1
        print(n,end="")
        if j != i+1:
            print(" ",end="")
        else:
            print("",end="")
    print()
