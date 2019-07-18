import random

def randomnum(i,n):
    print(random.randint(i,n+1))
    #print(random.randint(1,100))
i=int(input('Enter the start range:'))
n=int(input('Enter the end range:'))
randomnum(i,n)