def fibonacci(n):
    a=0
    b=1
    print(a,b,end=' ')
    for i in range(2,n):
        c=a+b
        a,b=b,c
        print(c,end=' ')

n=int(input('Enter the number of terms in a fibonnaci series: '))
fibonacci(n)


