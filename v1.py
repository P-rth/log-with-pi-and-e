import math 
print('to use pi as base enter 1')
print('to use e as base enter 2')
print('to use custom enter 3')
print('to use pi as number enter 4')
print('to use e as a number enter 5')
option = input('choose : ')
print ("you have choosed option " , option)
if option == '1':
 print('your answer is :',math.log(float(input("number:")),math.pi))
if option == '2':
 print('your anwer is :',math.log(float(input("number:"))))
if option == '3':
 print('your answer is :',math.log(float(input("number:")),float(input("base  :"))))
if option == '4':
 print('your answer is :',math.log(math.pi,float(input("base  :"))))
if option == '5':
 print('your answer is :',math.log(math.e,float(input("base  :"))))