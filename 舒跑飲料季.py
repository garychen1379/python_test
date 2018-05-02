a = eval(input())
n = a
total = a

while True:
    b = n // 4
    c = n % 4
    n = b + c
    total += b
    if n < 4:
        if n == 3:
            total += 1
            print(total)
            break
        else:
            print(total)
            break
    else:
        continue
            
    
