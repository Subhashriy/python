a=[int(x) for x in input().split()]

for i in range(len(a)-1):
    k=1
    for j in range(len(a)-1):
        if a[j]>a[k]:
            a[j],a[k]=a[k],a[j]
        k+=1
        #print(a)

print(a)