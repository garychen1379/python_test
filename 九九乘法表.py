n = eval(input())
m = eval(input())

for j in range(1,n+1):
    for i in range(1,m+1):
        print("%d*%d=%2.0f"%(j,i,j*i),end=" ",sep="\n")
    print()
