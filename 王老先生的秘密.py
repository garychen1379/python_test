lst = []
n = eval(input())

for i in range(n):
    s = input()
    lst.append(s)

o = lst.count('yes') + lst.count('no')
x = lst.count('YES') + lst.count('NO')
uc = n - o - x

print('%d %d %d'%(o,x,uc))
