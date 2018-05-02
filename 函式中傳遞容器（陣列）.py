lst = []

def find3rd(slst):
    slst.sort()
    return slst[-3]


while True:
    n = eval(input())
    if n == -1:
        break
    else:
        lst.append(n)
sslst = lst.copy()
sslst.sort()


print('input =',lst)
print('sorted =',sslst)
print('max 3rd =',find3rd(lst.copy()))
print('list =',lst)
