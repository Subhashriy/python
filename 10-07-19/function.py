#variable length arguments

def stud(**data):
    for key,val in data.items():
        print("{} , {} ".format(key,val))


stud(id=10,name="Sam",age=20)




print()

print()
#map function
lst=[1,3,5,7,9]
sqr=lambda x: x**2
sqrlst=map(sqr,lst)
print(list(sqrlst))


print()

print()
#Filter function

lst=[1,3,5,6,7,9,10]
sqr=lambda x: x%2==0
sqrlst=filter(sqr,lst)
print(list(sqrlst))




