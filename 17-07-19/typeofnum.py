n=int(input('Enter the number: '))
def typeof(n):
    if n>0:
        print('{} is positive number'.format(n))
    elif n<0:
        print('{} is negative number'.format(n))
    else:
        print('{} is zero'.format(n))

typeof(n)