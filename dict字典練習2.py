d = {'P':'Pikachu','M':'Mickey Mouse','H':'Hello kitty'}

while True:
    n = input()
    if n != '-1':
        if n not in d:
            print(n,'does not exist. Enter a new one:')
            n_value = input()
            d[n] = n_value
            continue
        else:
            print(d[n])
    else:
        break
