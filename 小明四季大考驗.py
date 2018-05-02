n = eval(input())

if 3 <= n <= 5:
    print('Spring')
elif 6 <= n <= 8:
    print('Summer')
elif 9 <= n <= 11:
    print('Autumn')
elif n==1 or n==2 or n==12:
    print('Winter')
else:
    print("Month doesn't exist!")
