num = int(input())

a = num//12
b = num%12
if b!= 0:
    print(a,'dozen and',b)
else:
    print(a,'dozen')
