height = eval(input())
weight = eval(input())
h = height/100
BMI = weight/(h**2)

print('%4.2f'%(BMI))

if BMI < 18.5:
    print('Underweight')
elif 18.5 <= BMI < 24:
    print('Normal')
elif 24 <= BMI < 27:
    print('Overweight')
elif 27 <= BMI < 30:
    print('Obese Class I')
elif 30 <= BMI < 35:
    print('Obese Class II')
else:
    print('Obese Class III')
