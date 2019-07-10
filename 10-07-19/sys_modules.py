#Time module

import time
#print(dir(time))
print()
print(time.time())
print()
print(time.localtime(time.time()))
print()
print(time.asctime(time.localtime(time.time())))
print()
#time.sleep(5)

print()
print()

#Datetime module

from datetime import datetime
print(datetime.now())

print(type(datetime.now()))

print()
#strftime- string format time
d=datetime.now()
print(d.strftime("%A"))
print(d.strftime("%p"))
print(d.strftime("%b"))
#print(datetime.date())
print()

print()


#sys module

import sys
print(sys.version)
print(sys.platform)
print(sys.copyright)
print(sys.path)

print()
print()
print()

#os module

import os

print(os.listdir())
print(os.getcwd())

#to change the current directory

os.chdir(r'C:\\Users\\trainee\\Desktop\\python')
print(os.getcwd())



print()
print()
print()

#math module

import math
print(dir(math))

print(math.pi)
print(math.sqrt(4))
print(math.pow(2,3))
print(math.factorial(6))
print(math.fabs(19))



print()
print()
print()
#random module

import random

print(random.random())#any no. between 0 and 1
print(random.randint(1,100))#any no.between the range include end points
print(random.randrange(1,100))#any no.between the range does not include end points
print(random.choice(['red','green','yellow']))#random value from the list
print(random.shuffle(['red','green','yellow']))#shuffle the list




print()
print()

from functools import reduce
add=lambda a,b: a+b
tot=reduce(add,[10,20,30,40,50])
print(tot)

lst1=[4,6,45,9,23,56]
maximum=lambda a,b: a if a>b else b
result=reduce(maximum,lst1)
print(result)
