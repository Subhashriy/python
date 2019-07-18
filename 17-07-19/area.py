import math

r=int(input('Enter the radius: '))

area=lambda x: math.pi*x*x

print('Area: {}'.format(area(r)))