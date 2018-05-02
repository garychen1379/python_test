lst = []
n = input()
lst = n.split()

head = int(lst[0])
foot = int(lst[1])
c = (4*head-foot)
r = (foot-2*head)

if c%2 != 0 or r % 2 != 0 or c<0 or r < 0:
    print('NO')
else:
    print('YES')
    print('%d %d'%(c/2,r/2),end='')
