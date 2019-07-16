import re
n=int(input())
lst=[]
lst1=[]
for i in range(n):
    lst.append(input())
    mailid=re.search(r'\w+@[a-z0-9]+\.[a-z]{1,3}',lst[i])
    if mailid!=None:
        lst1.append(lst[i])

lst1=sorted(lst1)
print(lst1)