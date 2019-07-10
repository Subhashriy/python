n=int(input("Enter the number of words: "))
lstr=[]
lcount=[]
print("Enter the words: ")
for i in range(n):
    lstr.append(input())
print(lstr)
count1=0
m=n
for i in range(n-1):
    count=1
    for j in range(i+1,n):
        if lstr[i]==lstr[j]:
            count+=1
            count1=1
            lstr.remove(lstr[j])
            n-=1
        if count1==1:
            m-=1
    lcount.append(count)

    
print(m)
    
