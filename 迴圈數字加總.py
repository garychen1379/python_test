n = input()
lstn = n.split(',')
total = 0
odd_t = 0
even_t = 0

for i in range(len(lstn)):
    x = int(lstn.pop())
    total += x
    if x % 2 == 0:
        even_t += x
    else:
        odd_t += x

print(odd_t)
print(even_t)
print(total)
    

