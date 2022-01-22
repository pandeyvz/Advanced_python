# Daemon Threads:-Threads running in the background to support for main thread . Eg:-Garbaje collector
# To check if the thread is deamon or not  t.isdaemon

# from threading import *
# print(current_thread().isDaemon())
# current_thread().setDaemon(True)
# print(current_thread().isDaemon())
#to change daemon nature use t.setdaemon("name),,we cant change the daemon nature of active thread , i.e why
# we cant change the daemon nature of
#

# from threading import *
# import time
# def job():
#     for i in range(10):
#         print("Lazy thread")
#         time.sleep(3)
# t=Thread(target=job)  #here both main and child thread are non daemon , i.e. why if main thread stopped also child thread will continue
# t.start()
# time.sleep(5)
# print("End of the Main thread")

# from threading import *
# import time
# def job():
#     for i in range(10):
#         print("Lazy thread")
#         time.sleep(3)
# t=Thread(target=job)
# t.setDaemon(True) #Here we are changing the child thread daemon to true i.e now its duty is to support the main thread and
#                    # thats why if main thread will stop with that cild thread will also stop
# t.start()
# time.sleep(5)
# print("End of the Main thread")

#By default only Main thread is non daemon rest thread inherits from the parent
from threading import *
import time
def job1():
    print("Job1 Execution...")
    print(current_thread().name,"is daemon:", current_thread().daemon)
    t=Thread(target=job2, name="Child_Thread2")  #Here we are creating child thread 2 , since we have called thhis inder child thread 1 so it will inherit
                                                   #the daemon from child thread 1 which is daemon
    print('t is daemon:',t.daemon)

def job2():
    print("Job2 execution...")
t=Thread(target=job1,name='Child_Thread')
t.setDaemon(True)  #Here we are changing to daemon
t.start()
time.sleep(10)