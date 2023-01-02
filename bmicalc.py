print('enter your height:')
height = int(input())/100
print('enter your weight:')
weight = int(input())
bmi = weight/height **2 
print(round(bmi, 1))

if bmi < 18.5:
    print('underwight')
elif bmi < 24.9:
    print('normal')
elif bmi > 25:
    print('overweight')
    