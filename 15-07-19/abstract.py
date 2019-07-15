from abc import ABC, abstractmethod

import math

class Shape(ABC):
    @abstractmethod
    
    def getArea(self):
        pass

class Circle(Shape):
    def getArea(self):
        return math.pi*10*10


cir=Circle()

print(cir.getArea())