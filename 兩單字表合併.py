n1 = input()
n2 = input()

lst1 = n1.split(';')
set1 = set(lst1)
lst2 = n2.split(',')
set2 = set(lst2)

u = set1.union(set2)
#i = set1.intersection(set2)
lst = list(u)
lst.sort()
lst.reverse()


for i in range(1,len(lst)+1):
    #print(lst.pop()+' ',end='')
    if i == 1:
        print(lst.pop(),end='')
    else:
        print(' '+lst.pop(),end='')
