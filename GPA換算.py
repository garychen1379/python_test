n = eval(input())

if 90 <= n <=100:
    print('4.3\nA+')
elif 85 <= n <=89:
    print('4.0\nA')
elif 80 <= n <=84:
    print('3.7\nA-')
elif 77 <= n <=79:
    print('3.3\nB+')
elif 73 <= n <=76:
    print('3.0\nB')
elif 70 <= n <= 72:
    print('2.7\nB-')
elif 67 <= n <= 69:
    print('2.3\nC+')
elif 63 <= n <= 66:
    print('2.0\nC')
elif 60 <= n <= 62:
    print('1.7\nC-')
else:
    print('0\nF')
