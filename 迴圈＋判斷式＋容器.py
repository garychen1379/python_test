lst = []

while True:
    n = eval(input())
    if n != -1:
        lst.append(n)
    else:
        break

print(lst)
lst.sort()
print(lst)

total = 0

for i in range(len(lst)):
    p = lst.pop()
    if p > 30:
        total += p
    else:
        continue

print(total)
    
