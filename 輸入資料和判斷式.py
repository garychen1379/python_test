ft = 1
it = 1
q = 'q'
while True:
    n = eval(input())
    if type(n) == int:
        it *= n
    elif type(n) == float:
        ft *= n
    elif n == 'q':
        break

print('%.2f'%ft)
print('%d'%it)

if ft == it:
    print('Float = Int')
elif ft > it:
    print('Float > Int')
else:
    print('Float < Int')
