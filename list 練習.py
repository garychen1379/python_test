lst = []

while True:
    n = eval(input())
    if n != -1:
        lst.append(n)
    else:
        lst.sort()
        print(lst)
        lst.insert(3,10)
        print(lst)
        print(lst.count(10))
        lst.sort()
        lst.reverse()
        print(lst)
        break
