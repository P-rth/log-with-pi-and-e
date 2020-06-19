
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
use = 0
while 1 < 6:
  if option != 'error':
   print()
   if option is None:
     option = input('choose : ')
   delete_last_lines(15)
   if use > 0:
     delete_last_lines(15)
   print ("you have choosed option " , option)
   print()
   if option == '1':
     num = input('enter a number:')
     if not num.isnumeric():
       print ('error')
       option='1'
       continue
     num=float(num)  
     ans=math.log(num,math.pi)
     print('your anwer is :',ans)
     option=None
     use = use+1
     continue
   elif option == '2':
     print('your anwer is :',math.log(float(input("number:"))))
     option = None
     use = use+1
     continue
   elif option == '3':
     print('your answer is :',math.log(float(input("number:")),float(input("base  :"))))
     option = None
     use = use+1
     continue
   elif option == '4':
     print('your answer is :',math.log(math.pi,float(input("base  :"))))
     option = None
     use = use+1
     continue
   elif option == '5':
     print('your answer is :',math.log(math.e,float(input("base  :"))))
     option = None
     use = use+1
     continue
   elif option == 'help':
     print('to use pi as base enter 1')
     print('to use e as base enter 2')
     print('to use custom enter 3')
     print('to use pi as number enter 4')
     print('to use e as a number enter 5')
     print('to exit enter exit')
     print(' ')
     print ("LOG      (NUMBER)")
     print ("   (base)")  
     option = None
     use = use+1
     continue
   elif option == 'exit':  
     option = None
     break
   else:
     option = 'error'
     continue
  else:
   delete_last_lines(9)
   use = use+1
   print ('tip: type help for help')
   print()
   option = input('please try again : ')
   continue   
