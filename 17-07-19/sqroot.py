tup=(1,2,3,4,5,6,7,8)
lst=[]
def sqrt(tup1):
    for i in range(len(tup1)):
        lst.append((tup1[i]**(1/2)))

    print(tuple(lst))
tup1=list(tup)
sqrt(tup1)


