f1 = open('字典練習3.py','r')
pylst = f1.readlines()
f1.close()

for i in range(len(pylst)):
    pylst[i] = pylst[i].strip()
    print(pylst[i])
