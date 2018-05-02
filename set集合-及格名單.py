math_pass = {'柯南','灰原','步美','美環','光彦'}
eng_pass = {'柯南','灰原','丸尾','野口','步美'}

math_not_eng = math_pass.difference(eng_pass)
eng_not_math = eng_pass.difference(math_pass)
i = math_pass.intersection(eng_pass)

lstm = list(math_not_eng)
lstm.sort()
lste = list(eng_not_math)
lste.sort()
lsti = list(i)
lsti.sort()

print(lstm)
print(lste)
print(lsti)
