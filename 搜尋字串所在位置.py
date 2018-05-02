s = input()
f = input()

n = s.count(f)
pos = -1
for i in range(n):
    pos = s.find(f,pos+1)
    print(pos)
