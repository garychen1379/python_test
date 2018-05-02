bond = eval(input())
strbond = str(bond)

if bond%7==0 or '7' in strbond:
    print('YES',end="\n")
else:
    print('NO',end="\n")
