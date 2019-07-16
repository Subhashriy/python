def fibonacci(n):
    a=0
    b=1
    print(a,b,end=' ')
    for i in range(2,n):
        c=a+b
        a,b=b,c
        yield c

#n=int(input('Enter the number of terms in a fibonnaci series: '))
obj=fibonacci(4)
#print(next(obj),ebd=' ')
#print(next(obj),end=' ')

for i in obj:
    print(i,end=' ')