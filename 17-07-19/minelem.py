lst=[int(x) for x in input('Enter the list: ').split(' ')]
min=99999
for i in range(len(lst)):
    if lst[i]<min:
        min=lst[i]

print('least element : {}'.format(min))
