import math
import sys 
import time 
import ANSI
answers=[]
def reset():
  global num
  global base
  global output
  global ans
  global retry
  global stage2
  num=None
  base=None
  output=None
  ans=None
  retry=0
  stage2=0
retry=0
#########################################################################
def Reverse(lst): 
    return [ele for ele in reversed(lst)]    
#########################################################################
def refreshanswers():
 ANSI.SCP()
 ANSI.goto00()
 #to change hight of previous ans change 5 in ANSI.DOWN(12+5-1)
 #helpcontent , distance to ans , -1 as print() new lines after evry output
 ANSI.DOWN(13+5-1)
 for x in Reverse(answers):
       if len(answers)>20:
         answers.pop(0)
       print (x)
 ANSI.GOTOSCP()
 #########################################################################
def help(): 
  print('to use pi as base enter 1')
  print('to calculate natural log enter 2')
  print('to use custom enter 3')
  print('to use pi as number enter 4')
  print('to use e as a number enter 5')
  print('to turn help off enter help off')
  print('to exit enter exit')
  print()
#########################################################################
def option1():
   reset()
   num = input('enter a number:')
   if not num.isnumeric():
     print ('error')
     global retry
     retry=1
     return False
   num=float(num)  
   ans=math.log(num,math.pi)
   print()
   output=('log of base PI and number %s is %s' % (num,ans))
   print(output)
   answers.append(output)
   refreshanswers()
   return False
#########################################################################
def option2():
  reset()
  num = input('enter a number:')
  if not num.isnumeric():
    print ('error')
    global retry
    retry=1
    return False
  num=float(num)  
  ans=math.log(num)
  print()
  output=('natural log of %s is %s' % (num,ans))
  print(output)
  answers.append(output)
  refreshanswers()
  return False
#########################################################################
def option3():
  global stage2
  reset()
  num = input('enter a number:')
  if not num.isnumeric():
   print ('error')
   global retry
   retry=1
   return False
  base = input('enter a base for log:')
  stage2=1
  if not base.isnumeric():
    print ('error')
    retry=1
    return False
  num=float(num)
  base=float(base)   
  ans=math.log(num,base)
  output=('log of base %s number %s is %s' % (base,num,ans))
  print(output)
  answers.append(output)
  refreshanswers()
  return False
#########################################################################
def option4():
 reset()
 base = input('enter a base for log :')
 if not base.isnumeric():
   print ('error')
   global retry
   retry=1
   return False
 base=float(base)
 ans=math.log(math.pi,base)
 output=('log of base %s and number PI is %s' % (base,ans))
 print(output)
 answers.append(output)
 refreshanswers()
 return False
########################################################################
def option5():
 reset()
 base = input('enter a base for log :')
 if not base.isnumeric():
   print ('error')
   global retry
   retry=1
   return False
 base=float(base)
 ans=math.log(math.e,base)
 output=('log of base %s and number E is %s' % (base,ans))
 print(output)
 answers.append(output)
 refreshanswers()
 return False
######################################################################
'''
help()
option3()
while retry == 1:
  time.sleep(0.75)
  print('                                       ')
  ANSI.UP(2)
  print('                                       ')
  ANSI.UP(2)
  print('                                       ')
  if stage2 == 1:
   ANSI.UP(2)
   print('                                       ')
  ANSI.UP(1)
  option3()
'''



help()
while True:
  option = input('choose a option: ')
  if option == '1': 
    option1()
    while retry == 1:
      time.sleep(0.75)
      print('                                       ')
      ANSI.UP(2)
      print('                                       ')
      ANSI.UP(2)
      print('                                       ')
      ANSI.UP(1)
      option1()
    for i in range(4):  
     sys.stdout.write("\033[F") #back to previous line
     sys.stdout.write("\033[K") #clear line
    continue  

  elif option == '2':
    option2()
    while retry == 1:
      time.sleep(0.75)
      print('                                       ')
      ANSI.UP(2)
      print('                                       ')
      ANSI.UP(2)
      print('                                       ')
      ANSI.UP(1)
      option2()
    for i in range(4):  
     sys.stdout.write("\033[F") #back to previous line
     sys.stdout.write("\033[K") #clear line
    continue 
  elif option == '3':
    option3()
    while retry == 1:
      time.sleep(0.75)
      print('                                       ')
      ANSI.UP(2)
      print('                                       ')
      ANSI.UP(2)
      print('                                       ')
      if stage2 == 1:
        ANSI.UP(2)
        print('                                       ')
      ANSI.UP(1)
      option3()
    for i in range(4):  
     sys.stdout.write("\033[F") #back to previous line
     sys.stdout.write("\033[K") #clear line
    continue 


  elif option == '4':
    option4()
    while retry == 1:
      time.sleep(0.75)
      print('                                       ')
      ANSI.UP(2)
      print('                                       ')
      ANSI.UP(2)
      print('                                       ')
      ANSI.UP(1)
      option4()
    for i in range(3):  
     sys.stdout.write("\033[F") #back to previous line
     sys.stdout.write("\033[K") #clear line
    continue 
    
  elif option == '5':
    option5()
    while retry == 1:
      time.sleep(0.75)
      print('                                       ')
      ANSI.UP(2)
      print('                                       ')
      ANSI.UP(2)
      print('                                       ')
      ANSI.UP(1)
      option5()
    for i in range(3):  
     sys.stdout.write("\033[F") #back to previous line
     sys.stdout.write("\033[K") #clear line
    continue 
  elif option == 'exit':
    ANSI.cls()
    ANSI.goto00()
    break 
  elif option == 'help off':
   ANSI.cls()
   ANSI.goto00()  
   continue
  else:
    print('wrong option') 
    time.sleep(1)
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line
    continue


