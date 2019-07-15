class Mobile:
    #Dunder method
    def __init__(self):
        self.__maxPrice=9999  # __ makes the variable private

    def getPrice(self):
        return self.__maxPrice

    def setPrice(self,price):
        self.__maxPrice=price

mob=Mobile()
#print(mob.maxPrice)
print(mob.getPrice())
mob.setPrice(8999)
print(mob.getPrice())