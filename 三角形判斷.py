a = eval(input())
b = eval(input())
c = eval(input())

if a + b > c and a + c > b and b + c > a:
    print('True')
    if a >= b:
        if a >= c:
            Max = a
            if a**2==b**2+c**2:
                print('Right Triangle')
            else:
                print('Non-Right Triangle')
        else:
            Max = c
            if c**2==b**2+a**2:
                print('Right Triangle')
            else:
                print('Non-Right Triangle')
    else:
        if b >= c:
            Max = b
            if b**2==a**2+c**2:
                print('Right Triangle')
            else:
                print('Non-Right Triangle')
        else:
            Max = c
            if c**2==b**2+a**2:
                print('Right Triangle')
            else:
                print('Non-Right Triangle')
            
else:
    print('False')
