iA = {"蘋果", "香蕉", "鳳梨", "芭樂"}
iB = {"鳳梨", "蘋果", "水梨", "蓮霧"}

'''u = iA.union(iB)
i = iA.intersection(iB)
ans = u - i
lst = list(ans)
lst.sort()
print(lst)'''


a = input()
b = input()
c = input()
d = input()


iA.add(a)
iA.add(b)
iA.remove('蘋果')
iB.add(c)
iB.add(d)
iB.remove('蓮霧')
lstia = list(iA)
lstia.sort()
lstib = list(iB)
lstib.sort()
print('iA:',lstia)
print('iB:',lstib)

u = iA.union(iB)
lstu = list(u)
lstu.sort()
print('union:',lstu)
i = iA.intersection(iB)
lsti = list(i)
lsti.sort()
print('intersection:',lsti)

adb = iA.difference(iB)
lstadb = list(adb)
lstadb.sort()
print('A diff B:',lstadb)

bda = iB.difference(iA)
lstbda = list(bda)
lstbda.sort()
print('B diff A:',lstbda)



ans = u - i
lstans = list(ans)
lstans.sort()
print('A xor B:',lstans)
