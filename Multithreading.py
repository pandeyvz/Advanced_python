# Multitasking :-executing several task
# 2 types:--Process based
#           thread based
# Process based:-Executing Several task simultaneously where each task is a separate independent process, based suitable at os level
# thread based:-at programmatical level, executing several task simutaneously where each task is separate independent part of same program
# eg:- if we have 200 lines of code and first 100 lines and last 100 lines has no relation then we will run the both part
# simultaneously which will save execution time , each independent part is called thread . Animations, multi medigraphics
# video games, webservers and application servers
# Python support the threading module inbuilt  , By default every python program conain 1 thread, i.e. Main Thread
# Thread:- Flow of execution , for every thread separate job is available

# import threading
# print("Current executing thread:",threading.current_thread().getName())

#Create threads in python
# --without using class
# --extending Thread class
# --without extending thread class

#enumerate():-List of all active thread objects we want
# from threading import *
# import time
# def display():
#     print(current_thread().name,'started.....')
#     time.sleep(3)
#     print(current_thread().name,'ended.....')
# print("The no. of active threads:",active_count())
# t1=Thread(target=display,name='child_thread1')
# t2=Thread(target=display,name='child_thread2')
# t3=Thread(target=display,name='child_thread3')
# t1.start()
# t2.start()
# t3.start()
# l=enumerate()
# for t in l:
#     print('Name:',t.name)
# time.sleep(10) #After 10 sec all child thread will sleep only main thread will remain
# l=enumerate()
# for t in l:
#     print('Name:',t.name)
# #To check if thred i alive or not :- isAlive
#
# from threading import *
# import time
# def display():
#     print(current_thread().name,'started.....')
#     time.sleep(3)
#     print(current_thread().name,'ended.....')
# print("The no. of active threads:",active_count())
# t1=Thread(target=display,name='child_thread1')
# t2=Thread(target=display,name='child_thread2')
# t3=Thread(target=display,name='child_thread3')
# t1.start()
# t2.start()
# t3.start()
# print(t1.name,'is Alive:',t1.isAlive())
# print(t2.name,'is Alive:',t2.isAlive())
# print(t3.name,'is Alive:',t3.isAlive())
#
# time.sleep(10) #Will check if thread is alive after 10 secs or not
#
# print(t1.name,'is Alive:',t1.isAlive())
# print(t2.name,'is Alive:',t2.isAlive())
# print(t3.name,'is Alive:',t3.isAlive())

#If a function present inside the class it is called method and if outside its called function
#if a thread wants to wait until completing some other thread then we go for join method
#suppose 3 threads r there t1,t2,t3 ,and we want t2 to execute after completion of t1 then t2 has to execute t1.join()

from threading import *
import time
def display():
    for i in range(10):
        print("Seeta Thread")
        time.sleep(2)
t=Thread(target=display)
t.start()
t.join()  # NOw we want rama thread to continue after seeta thread so , here main thread id t2 and child thread is t1
for i in range(10):
    print("Rama thread") #First rama thread will complete as seeta thread is sleeping for 2 mins
