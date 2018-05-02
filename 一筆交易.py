n = eval(input())
s = input()

sstrip = s.strip()
lst = sstrip.split(sep=' ')

for i in range(n):
    print(int(lst.pop()),end=' ')
print()
