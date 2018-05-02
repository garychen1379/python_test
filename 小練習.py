'''shelf =['Book1','Book2','Book6','Book4','Book5']

shelf.append(shelf[2])
shelf[2] = 'Book3'
print(shelf)'''


lst = []

while True:
    n = eval(input())
    if n == -1:
        break
    lst.append(n)
lst.sort()
print(lst)
lst.insert(3,10)
lst.count(10)
lst.sort()
lst.reverse()
print(lst)

