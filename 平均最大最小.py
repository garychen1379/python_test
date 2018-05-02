score = 0
total = 0
ct = -1
MaxValue = 0
MaxPosition = 0

while score != -1:
    total += score
    ct += 1
    if score > MaxValue:
        MaxValue = score
        MaxPosition = ct
    score = eval(input())

print(total)
print(total/ct)
print(MaxValue)
print(MaxPosition)
