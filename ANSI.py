#ANSIECAPECODES BY PARTH
import sys

def UP(n=1):
    for _ in range(n):
        sys.stdout.write('\x1b[1A')

def DOWN(n=1):
    for _ in range(n):
        sys.stdout.write('\x1b[1B')

def RIGHT(n=1):
    for _ in range(n):
        sys.stdout.write('\x1b[1c')

def LEFT(n=1):
    for _ in range(n):
        sys.stdout.write('\x1b[1D')

def CLRLINE():
   sys.stdout.write('\x1b[K')

def SCP():
   sys.stdout.write('\x1b[1s')
   
def GOTOSCP():
   sys.stdout.write('\x1b[1u') 

def printnoenter(word):
   print(word)
   sys.stdout.write('\x1b[1A')

def cls():
  sys.stdout.write('\x1b[2J')   

def deldownlines(n):
  for _ in range(n):
   sys.stdout.write('\x1b[1K')
   sys.stdout.write('\x1b[1B')

def deluplines(n):
  for _ in range(n):
   sys.stdout.write('\x1b[1K')
   sys.stdout.write('\x1b[1A')

def goto00():
  sys.stdout.write('\x1b[0;0f')