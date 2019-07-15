from datetime import datetime

'''print("Hello")
for i in range(5):
    if i==3:
        continue
    print(i)'''


class Employee:
    bonus=5000

    def __init__(self,empNo,name,salary):
        self.name=name
        self.salary=salary
    def getSalary(self):
        return self.salary

    def applyHike(self):
        self.salary*=1.04
        return self.salary

    #class method
    @classmethod
    def setBonus(cls,amount):
        cls.bonus=amount
         #cls is class reference

    #static method   
    @staticmethod
    
    def isworkingDay():
        day=datetime.now().strftime('%w')
        if day=='0' or day=='6':
            return False
        else:
            return True

    def __str__(self):
        return self.name

    '''def __repr__(self):
        return str(self.salary)'''

    def __add__(self,other):
        return self.salary + other.salary



class Developer(Employee):
    def __init__(self,empNo,name,salary,stack):
        self.stack=stack
        super().__init__(empNo,name,salary)
            
    def getStack(self):
        return self.stack





if __name__=='__main__':


    dev=Developer(12,'Hari',25000,'Python')
    print(dev.getStack())
    print(dev.getSalary())

    print(getattr(dev,'salary'))
    setattr(dev,'salary',20000)
    print(getattr(dev,'salary'))

    print(dev.__dict__)
    delattr(dev,'salary')
    print(dev.__dict__)
    print(hasattr(dev,'salary'))

    #object creation
    emp1=Employee(10,'Ram',10000)
    emp2=Employee(20,'Sam',20000)
'''    print('Hello'+'world')

    print(emp1+emp2)
print(emp1)
print(emp2)


print(emp1.salary)

print(emp1.getSalary())
print(Employee.getSalary(emp2))


print(emp1.bonus)
print(emp2.bonus)



Employee.setBonus(1000)
print(emp1.bonus)
print(emp2.bonus)




emp1.applyHike()
print(emp1.__dict__)
print(emp2.__dict__)


print(Employee.isworkingDay())
'''
    