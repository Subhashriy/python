#print odd numbers in a range

def odd(a,b):
    for i in range(a,b+1):
        if(i%2!=0):
            print(i,end=' ')
print("Odd numbers in a range")
a=int(input("Start range: "))
b=int(input("End range: "))
odd(a,b)
