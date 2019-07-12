import re

n=int(input("Enter no. of lines:"))
a=[]

for i in range(n):
    a.append(input())
    str1=re.sub(r'&&','and',a[i])
    str1=re.sub(r'\|\|','or',a[i])

    










