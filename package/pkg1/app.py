# import entire module

'''import calc

calc.add(45,34,23)
calc.div(10,5)
calc.mul(9,7)'''


#import req. functions 


from calc import add
from calc import mul
add(45,56)
mul(9,8)



#imported functions can be renamed

from calc import div as division
division(20,10)


#import all the functions

from calc import *

sub(7,2)


