class Account:
    def __init__(self,id):
        self.id=id
        self.bal=10000
    def withdraw(self,wamt):
        if wamt%100==0:
            if self.bal-wamt>=5000:
                self.bal-=wamt
                print ("current balance: {}".format(self.bal))
            else:
                print ("Enter a lesser amount")
        else:
            print ("Enter valid amount")

    def deposit(self,damt):
        if damt%50==0:
            self.bal+=damt
            print("current balance: {}".format(self.bal))
    
    def checkBal(self):
        print("Current balance is: {}".format(self.bal))

acc=Account(1)
#print(acc.bal)
#acc.withdraw(3000)
acc1=Account(2)
#acc.withdraw(1250)
acc1.withdraw(700)
acc1.deposit(1900)
acc1.checkBal()