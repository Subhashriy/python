lst=[int(x) for x in input('Enter the elements of list: ').split(' ')]

lst=filter(lambda a: (a%2!=0),lst)
print(list(lst))