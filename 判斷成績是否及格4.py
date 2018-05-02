s = []

while True:
    score = eval(input())
    s.append(score)
    n = input()
    if n == 'y':
        continue
    else:
        break

s.reverse()
for i in range(1,len(s)+1):
    x = s.pop()
    if x >= 60:
        print('pass')
    else:
        print('fail')
