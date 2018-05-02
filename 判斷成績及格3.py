school = eval(input())

if school == 1 or school == 2:
    break
else:
    print('roll error')

score = eval(input())

if 0 <= score <= 100:
    print('fail')
