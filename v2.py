'''
import math 
print ("to use pi write $")
print ("to use e write @")
base = str(input("base:"))
num  = float(input("number:"))
if base == "$" :
     print ("your answer is:")
     print (math.log(num,3.141592653589793238462643383279502884197169399375105820974944592307816406286))     
if base == '@' :
     print ("your answer is:")
     ans=math.log(num) 
     print 
ans=math.log(num,base)
print ("your answer is:")
print (ans)
            /\
failed code ||
'''
while 1 < 6:
  import math 
  print('                        ')
  print('to use pi as base enter 1')
  print('to use e as base enter 2')
  print('to use custom enter 3')
  print('to use pi as number enter 4')
  print('to use e as a number enter 5')
  print('to exit enter exit')
  print('                         ')
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
  if option == 'exit':
   break