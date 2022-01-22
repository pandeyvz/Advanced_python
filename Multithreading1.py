# #Creating a thread without any class
#
# from threading import *
# def display():
#     for i in range(10):
#         print("Child Thread")
# t=Thread(target=display) #Thread is a predefined class present in the threading module, here we created a thread object
# t.start()                #Thread will start
# for i in range(10):
#     print("Parent Thread")

#Creating a thread by extending thread class
#
# from threading import *
# class Mythread(Thread):  #Creating child class of Thread as we have by default Thread class available
#     def run(self):
#         for i in range(10):
#             print("Child thread-1")
# t=Mythread()
# t.start()
# for i in range(10):
#     print("Main Thread-1")

#Creating a thread without extending thread class

# from threading import *
# class Test:
#     def display(self):
#         for i in range(10):
#             print("Child Thread2")
# obj=Test()
# t=Thread(target=obj.display)  #To call function from class obj.display
# t.start()
# for i in range(10):
#     print("Main Thread-2")

#Without Multithreading
from threading import *
# import time
# def double(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Double:",2*n)
# def square(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Square:",n*n)
# numbers=[1,2,3,4,5,6]
# begintime=time.time()
# double(numbers)
# square(numbers)
# print("the total time taken:",time.time()-begintime)

#With Multithreading
#
# import time
# from threading import *
# def double(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Double:",2*n)
# def square(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Square:",n*n)
# numbers=[1,2,3,4,5,6]
# begintime=time.time()
# t1=Thread(target=double,args=(numbers,)) #args is taking the list value
# t2=Thread(target=square,args=(numbers,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("The Total time taken:",time.time()-begintime)

#Setting and getting name of a thread
# from threading import *
# print(current_thread().getName())
# current_thread().setName("Vineet Pandey")
# print(current_thread().getName())
# print(current_thread().name)

#Thread identification number:-For every thread a unique identification number  is available we can access that by using
# implicit variable :- ident
# from threading import *
# def Test():
#     print("Child Thread\n")
# t=Thread(target=Test)
# t.start()
# print("Main thread identification no. is :",current_thread().ident)
# print("Child thread identification no. is :",t.ident )

#active_count:-This function returns the no. of active threads running
# from threading import *
# import time
# def display():
#     print(current_thread().getName(),"started")
#     time.sleep(3)
#     print(current_thread().getName(),"ended")
# print("The no. of active threads:",active_count())
# t1=Thread(target=display,name="child_thread1")
# t2=Thread(target=display,name="child_thread2")
# t3=Thread(target=display,name="child_thread3")
# t1.start()
# t2.start()
# t3.start()
# print("the no. of active threads:",active_count())
# print(time.sleep(5))
# print("The no. of active threads :",active_count())

#enumerate():-This function returns a list of all active threads currently running
from threading import *
import time
from threading import *
import time
def display():
    print(current_thread().getName(),"started")
    time.sleep(3)
    print(current_thread().getName(),"ended")
print("The no. of active threads:",active_count())
t1=Thread(target=display,name="child_thread1")
t2=Thread(target=display,name="child_thread2")
t3=Thread(target=display,name="child_thread3")
t1.start()
t2.start()
t3.start()
L=enumerate()
for t in L:n
    print("Thread name:",t.name)
time.sleep(5)
L=enumerate()
for t in L:
    print("Thread name :",t.name)