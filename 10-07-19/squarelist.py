#Square elements in a list

lst=[1,2,5,7,6,9]
lst1=[]

def sqr(lst):
    for i in range(len(lst)):
        lst1.append(lst[i]**2)

    return lst1
print(lst)
sqr(lst)
print(lst1)
