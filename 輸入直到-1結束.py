score = 0
total = 0
ct = -1
MaxVal = 0
MaxPos = 0

while score!= -1:
    total += score
    ct += 1
    if score > MaxVal:
        MaxVal = score
        MaxPos = ct
    score = eval(input())


print(total)
print(total/ct)
print(MaxVal)
print(MaxPos)
