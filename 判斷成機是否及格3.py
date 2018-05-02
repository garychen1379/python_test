school = eval(input())

if school != 1 and school != 2:
    print('roll error')
else:
    if school == 1:
        score = eval(input())
        if score > 100 or score < 0:
            print('score error')
        else:
            if score >= 60:
                print('pass')
            else:
                print('fail')
    else:
        score = eval(input())
        if score > 100 or score < 0:
            print('score error')
        else:
            if score >= 70:
                print('pass')
            else:
                print('fail')
