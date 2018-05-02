d = {'A':10,'J':18,'S':26,
 'B':11,'K':19,'T':27,
 'C':12,'L':20,'U':28,
 'D':13,'M':21,'V':29,
 'E':14,'N':22,'W':32,
 'F':15,'O':35,'X':30,
 'G':16,'P':23,'Y':31,
 'H':17,'Q':24,'Z':33,
 'I':34,'R':25}

identity = []
while True:
    n = input().upper()
    if n != '-1':
        identity.append(n)
    else:
        break

identity.reverse()

for i in range(1,len(identity)+1):
    x = identity.pop()
    if len(x) != 10:
        print('fake')
    else:       
        first_letter = x[0:1:1]
        first_number = str(d[first_letter])
        a1 = first_number[0:1:1]
        b1 = first_number[1:2:1]
        c1 = x[1:2:1]
        d1 = x[2:3:1]
        e1 = x[3:4:1]
        f1 = x[4:5:1]
        g1 = x[5:6:1]
        h1 = x[6:7:1]
        i1 = x[7:8:1]
        j1 = x[8:9:1]
        k1 = x[9:10:1]
        
        calculated = int(a1)*1 + int(b1)*9 + int(c1)*8 + int(d1)*7 + int(e1)*6 + int(f1)*5 + int(g1)*4 + int(h1)*3 + int(i1)*2 + int(j1)*1 + int(k1)*1
        if calculated%10==0:
            print('real')
        else:
            print('fake')

