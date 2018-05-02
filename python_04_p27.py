'''exam_score = input()

if int(exam_score) >= 95:
    print("2000元")
elif 90 <= int(exam_score) < 94:
    print("1000元")
elif 80 <= int(exam_score) < 89:
    print("500元")
else:
    print("0元")'''


'''age = input()
if int(age) >= 20:
    print('oijopj')
elif int(age) < 20 and int(age) >= 18:
    print("adsdsda")
else:
    print("afsdf")'''

'''sum1 = 0
for i in range(101):
    sum1 += i
print(sum1)'''


'''for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()'''


'''for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()'''

n =0
for i in range(1,6):
    for j in range(1,i+1):
        n += 1
        print(n,end="")
    print()

    
