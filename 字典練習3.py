d = {'P':'Pikachu','M':'Mickey Mouse','H':'Hello kitty'}
lst = []
vlst = []

while True:
    n = input()
    if n != '-1' and n != '-2':
        if n not in d:
            print(n,'does not exist. Enter a new one:')
            n_value = input()
            d[n] = n_value
            continue
        else:
            print(d[n])
    elif n == '-2':
        lst = list(d)
        lst.sort()
        print('keys:',lst)
        lst.reverse()
        for i in range(len(lst)):
            x = lst.pop()
            v = d[x]
            vlst.append(v)
        print('values:',vlst)
        continue
    else:
        break
