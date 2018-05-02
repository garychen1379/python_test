'''count = 0
Min = 1
Max = 100

ans = eval(input())
print(Min,"< ? <",Max)
#count += 1
keyin = eval(input())
while keyin > ans:
    print("wrong answer, guess smaller")
    print(Min,"< ? <",keyin)
elif keyin < ans:
    print("wrong answer, guess larger")
    print(keyin,"< ? <",Max)
else:
    break'''

'''count = 0
Min = 1
Max = 100

ans = eval(input())

while count < 1:
    keyin = eval(input())
    if keyin > ans:
        print("wrong answer, guess larger")
    elif keyin < ans:
        print("wrong answer, guess smaller")
    else:
        break
print("bingo answer is 45")'''

count = 0
Min = 1
Max = 100

ans = eval(input())
keyin = 0      
while keyin != ans:
    print(Min, '< ? <',Max)
    keyin=eval(input())
    count +=1
    if keyin > ans:
        print('wrong answer, guess smaller')
        Max = keyin
    elif keyin < ans:
        print('wrong answer, guess larger')
        Min = keyin
    else:
        print('bingo answer is',ans)
   
