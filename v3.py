
import math
import sys 
print('                        ')
print('to use pi as base enter 1')
print('to use e as base enter 2')
print('to use custom enter 3')
print('to use pi as number enter 4')
print('to use e as a number enter 5')
print('for help enter help')
print('to exit enter exit')
option = None
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
def delete_last_lines(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

while 1 < 6:
  if option != 'error':
   print()
   if option is None:
     option = input('choose : ')
   delete_last_lines(9)
   print ("you have choosed option " , option)
   print()
   if option == '1':
     print('your answer is :',math.log(float(input("number:")),math.pi))
   elif option == '2':
     print('your anwer is :',math.log(float(input("number:"))))
   elif option == '3':
     print('your answer is :',math.log(float(input("number:")),float(input("base  :"))))
   elif option == '4':
     print('your answer is :',math.log(math.pi,float(input("base  :"))))
   elif option == '5':
     print('your answer is :',math.log(math.e,float(input("base  :"))))
   elif option == 'help':
     print('to use pi as base enter 1')
     print('to use e as base enter 2')
     print('to use custom enter 3')
     print('to use pi as number enter 4')
     print('to use e as a number enter 5')
     print('to exit enter exit')
     print()
     print ("LOG      (NUMBER)")
     print ("   (base)")
   elif option == 'exit':
     break
   else:
     option = 'error'
  else:
   delete_last_lines(9)
   print ('tip: type help for help')
   print()
   option = input('please try again : ')
   continue
