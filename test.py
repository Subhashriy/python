
lst=[['ono',12354,12355,12356],['btitle','Computer Programming','programming for beginners','computer basics'],['quan',5,8,3],['price',449,649,179]]
tot=lambda a: tuple(a)
lst2=['']
lst3=[]
result=()
for i in range(1,len(lst[0])):
    lst2.append(lst[2][i]*lst[3][i])
    
for i in range(1,len(lst[0])):
    lst4=[]
    lst4.append(lst[1][i])
    lst4.append(lst2[i])
    #lst3.append(tuple(lst4))
    tot(lst4)
    lst3.append(tot)

print(lst3)
               





'''    
#electricity bill

unit=int(input("Enter the number of units: "))

if(unit>=0 and unit <=100):
    bill=(unit*1.00)
    bill+=(bill*0.015)
    print(" Bill amount: {}".format(bill))

elif unit>=101 and unit<=200:
    bill=(unit*1.50)
    bill+=(bill*0.015)
    print(" Bill amount: {}".format(bill))

elif unit>=201 and unit<=500:
    bill=(unit*3.00)
    bill+=(bill*0.015)
    print(" Bill amount: {}".format(bill))

elif unit>500:
    bill=(unit*5.00)
    bill+=(bill*0.015)
    print(" Bill amount: {}".format(bill))
    
'''
