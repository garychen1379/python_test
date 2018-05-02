d = {4:'鼠',5:'牛',6:'虎',7:'兔',8:'龍',9:'蛇',10:'馬',11:'羊',0:'猴',1:'雞',2:'狗',3:'豬'}

lst = []
y_name = input()

if y_name == 'AD':
    while True:
        year = eval(input())
        if year == -1:
            break
        else:
            lst.append(year)
    lst.reverse()
    for i in range(len(lst)):
        n = int(lst.pop())%12
        print(d[n])

else:
    while True:
        year = eval(input())
        if year == -1:
            break
        else:
            lst.append(year)
    lst.reverse()
    for i in range(len(lst)):
        n = (int(lst.pop())+3)%12
        print(d[n])
        
