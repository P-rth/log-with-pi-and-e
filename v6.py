
import math
import sys  
print('                        ')
print('to use pi as base enter 1')
print('to use e as base enter 2')
print('to use custom enter 3')
print('to use pi as number enter 4')
print('to use e as a number enter 5')
print('to view preveous ans enter 6')
print('for help mode enter help')
print('to exit enter exit')

option = None
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
linedown = "\u001b[B"
def delete_last_lines(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)
def up(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
def down(n=1):
 for _ in range(n):
   sys.stdout.write(linedown)

answers=["answer",] 
use = 0
help=0
linesused=0
firstrun=1
noofans=0
while True:
   
  if option != 'error':
   
   if help==1:
     up(20)
     down(40)
     for x in answers:
       print (x)
       noofans=noofans+1
     up(21+noofans)
     delete_last_lines(7)  
   if option is None:
     option = input('choose : ')
     if firstrun == 1:
      delete_last_lines(15)
      firstrun=0  
   if use>0:
     if help != 1:
       delete_last_lines(15) 
   if option != 'help':    
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
     print()
     print('your anwer is :',ans)
     option=None
     use = use+1
     linesused=6
     answers.append(ans)
     continue
   elif option == '2':
     num = input('enter a number:')
     if not num.isnumeric():
       print ('error')
       option='2'
       continue
     num=float(num)  
     ans=math.log(num)
     print()
     print('your anwer is :',ans)
     option=None
     use = use+1
     linesused=6
     continue
   elif option == '3':
     num = input('enter a number:')
     base = input('enter a base for log')
     if not num.isnumeric():
       print ('error')
       option='3'
       continue
     if not base.isnumeric():
       print ('error')
       option='3'
       continue
     num=float(num)
     base=float(base)   
     ans=math.log(num,base)
     print('your anwer is :',ans)
     option=None
     use = use+1
     linesused=6
     continue
   elif option == '4':
     base = input('enter a base for log:')
     if not base.isnumeric():
       print ('error')
       option='4'
       continue
     base=float(base)
     print(base)  
     ans=math.log(math.pi,base)
     print('your anwer is :',ans)
     option=None
     use = use+1
     linesused=6
     continue
     continue
   elif option == '5':
     base = input('enter a base for log:')
     if not base.isnumeric():
       print ('error')
       option='5'
       continue
     base=float(base)
     print(base)  
     ans=math.log(math.e,base)
     print('your anwer is :',ans)
     option=None
     use = use+1
     linesused=6
     continue
   elif option == 'help': 
     if help!=1:
       help=1 
       print('to use pi as base enter 1')
       print('to use e as base enter 2')
       print('to use custom enter 3')
       print('to use pi as number enter 4')
       print('to use e as a number enter 5')
       print('to view preveous ans enter 6')
       print('to exit enter exit')
       print(' ')
       print ("LOG      (NUMBER)")
       print ("   (base)")  
       option = None
       use=use+1
      
       continue
     else:
       delete_last_lines(2)
       option = None
       use=use+1
       continue  
   elif option == 'exit':  
     option = None
     break
   else:
     option = 'error'
     continue
  else:
   if help != 1:
     delete_last_lines(15)
   delete_last_lines(2)
   use = use+1
   print ('tip: type help for help')
   option = input('please try again : ')
   delete_last_lines(2)
   continue   
