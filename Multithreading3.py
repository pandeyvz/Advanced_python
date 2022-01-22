#Synchronisation:-One thread will not start until  another thread completes , to solve data imconsistency problem , ef:-Online booking of ticket
# from threading import *
# import time
# l=Lock()       #Here we are starting the lock, Main thread creating lock object
# def wish(name):
#     l.acquire()    #l.acquire we have to use from where we want only one thread to execute at a time
#     for i in range(10):
#         print("Good evening:",end='')
#         time.sleep(3)
#         print(name)
#     l.release()    #If we will not release the lock then thread1 will be dead and program will be halted for lifetime , ctrl+break use to stop
# t1=Thread(target=wish,args=("Dhoni",))
# t2=Thread(target=wish,args=('Kohli',))
# t1.start()
# t2.start()
#Here which thread will get to execute first nobody knows , depends on system to system
#Rlock:-To overcome lock problem, for recursive function l.acquire will be called multiple time and code will halt,
#RLock=Re entrant lock , same lock can be acquired again and again
# l=RLock()
# l.acquire()--Got lock-->holds1
# l.acquire()-->holds2
# l.acquire()-->Holds3
# l.release()-->holds3-1=2
# l.release()-->holds 2-1=1
# l.release()-->holds=1-1=0

from threading import *
import time
l=RLock()
def factorial(n):
    l.acquire()
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    l.release()
    return result
def results(n):
    print("The factorial of",n ,'is:',factorial(n))
t1=Thread(target=results,args=(5,))
t2=Thread(target=results,args=(9,))
t1.start()
t2.start()
#In Lock() there is no mechanism to track who is acquiring the lock thats why
#semaphore:-At a time multiple thread can execute which was not there in lock and Rlock, synchronisation for fix no of threads