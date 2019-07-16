import multiprocessing
from threading import Thread
import os
import time

class A(Thread):
    def run(self):
        for i in range(3):
            print("Worker1: {}".format(os.getpid()))
            time.sleep(1)
class B(Thread):
    def run(self):
        for i in range(3):
            print("Worker2: {}".format(os.getpid()))
            time.sleep(1)



def worker1():
    for i in range(3):
            print("Worker1: {}".format(os.getpid()))
            time.sleep(1)

def worker2():
    for i in range(3):
            print("Worker2: {}".format(os.getpid()))
            time.sleep(1)


if __name__=='__main__':


    a=A()
    b=B()
    p1=multiprocessing.Process(target=worker1)
    p2=multiprocessing.Process(target=worker2)

    p1.start()
    p2.start()

    p1=a
    p2=b
    p1.start()
    p2.start()

    

