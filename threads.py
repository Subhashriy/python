from threading import Thread
import time

#importing thread class 
class A(Thread):
    def run(self):
        for i in range(1,4):
            print(i**3)
            time.sleep(1)
    
class B(Thread):
    def run(self):
        for i in range(1,4):
            print(i**2)
            time.sleep(1)
    

a=A()
b=B()

if __name__=='__main__':
    '''
    #creating threads
    t1=threading.Thread(target=cubes,args=())
    t2=threading.Thread(target=squares,args=())
  

    print(t1.is_alive())
    #start thread
    t1.start()
    t2.start()
    print(t2.is_alive())
    #active thread count
    print("Number of threads active: {}".format(threading.activeCount()))


    #setName function
    t1.setName('qubes')
    t2.setName('square')
    #getName function
    print(t1.getName())
    print(t2.getName())
    
    
    
    t1.join()
    t2.join()


    #cubes()
    #squares()
    


print(dir(threading))
'''


a.start()
b.start()
a.join()#main thread waits till a is executed
b.join()#main thread waits till b is executed

for i in range(1,3):
    print("main thread")