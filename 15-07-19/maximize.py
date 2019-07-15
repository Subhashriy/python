a=input().split(' ')
#print(a)
k=int(a[0])
m=int(a[1])
kl=[]
max2=[]
for i in range(k):
    max1=0
    k1=input().split(' ')
    for j in range(1,int(k1[0])+1):
        kl.append(int(k1[j]))
    max1=max(kl)
    max2.append(max1**2)

print(sum(max2)%m)