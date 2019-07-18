lst=[5,1,10,24,53,12,53]

def desc(lst):
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if(lst[i]<lst[j]):
                t=lst[i]
                lst[i],lst[j]=lst[j],t

    print(lst)

desc(lst)
