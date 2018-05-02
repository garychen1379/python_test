d = {'A':10,'J':18,'S':26,
 'B':11,'K':19,'T':27,
 'C':12,'L':20,'U':28,
 'D':13,'M':21,'V':29,
 'E':14,'N':22,'W':32,
 'F':15,'O':35,'X':30,
 'G':16,'P':23,'Y':31,
 'H':17,'Q':24,'Z':33,
 'I':34,'R':25}

identity = input().upper()
first_letter = identity[0:1:1]
first_number = str(d[first_letter])

if len(identity) != 10:
    print('fake')
else:
    a = first_number[0:1:1]
    b = first_number[1:2:1]
    c = identity[1:2:1]
    d = identity[2:3:1]
    e = identity[3:4:1]
    f = identity[4:5:1]
    g = identity[5:6:1]
    h = identity[6:7:1]
    i = identity[7:8:1]
    j = identity[8:9:1]
    k = identity[9:10:1]
    calculated = int(a)*1 + int(b)*9 + int(c)*8 + int(d)*7 + int(e)*6 + int(f)*5 + int(g)*4 + int(h)*3 + int(i)*2 + int(j)*1 + int(k)*1
    if calculated%10==0:
        print('real')
    else:
        print('fake')
