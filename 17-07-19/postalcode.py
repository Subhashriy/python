import re
p=(input('Enter the postal code: '))

inrange=re.search(r'^[1-9][0-9]{5}$',p)
#print(inrange.group(0))
altrep=re.search(r'(\d)\d(\d)',p)
print(altrep.group(0))
if(altrep==[]):
    print('valid')
else:
    print('invalid')