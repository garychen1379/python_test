n = eval(input())
fct = 0

for j in range(2,n+1):
    for i in range(1,j+1):
        if j%i == 0:
            fct += 1
    if fct == 2:
        print(j,"is prime")
    fct=0

   
        

