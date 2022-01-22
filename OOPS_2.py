# # Accessing members of one class  inside another class
#
# class Employee:
#     def __init__(self,eno,ename,esal):
#         self.eno=eno
#         self.ename=ename
#         self.esal=esal
#
#     def  display(self):
#         print("Employee number:" ,self.eno)
#         print("Employee name:", self.ename)
#         print("Employee salary:", self.esal)
#
# class Test:
#     def modify(emp):
#         emp.esal=emp.esal+10000  #Accessing members of other class
#         emp.display()
# e=Employee(100,"Durga",10000)  #Statisc method as emp is self but not pointing to test
# Test.modify(e)

#Inner class :-Class inside another class :Without existing one type of object if there is no chance of existing
#another type of objects , then we go for Inner classes .

# class University:
#     class Department: #Without university Department will not exist

#Destructor:- Job is to perform clean up activities and Garbaje collector destroy Object
#if object does not have any reference variable , object is eligible for Garbaje collection
# def __del__(self)
#
# import time
# class Test:
#     def __init__(self):
#         print("Object Initialisation")
#
#     def __del__(self):
#         print("Fulfilling last wish and performing cleanup activites")
# t1=Test()
# print("Using t1 based on requirement")
# time.sleep(5)
# print("Work with t1 completed make eligible for GC")
# t1=None         # Destructor will execute and GC will call destructor
# time.sleep(10)
# print("End of app")

#Another Example

# import time
# class Test:
#     def __init__(self):
#         print("Object Initialisation")
#
#     def __del__(self):
#         print("Fulfilling last wish and performing cleanup activites")
# t1=Test()
# t2=t1
# t3=t2
# del t1 #Not Deleting object , deleting reference variables
# time.sleep(10)
# print("Object yet not destroyed")
# del t2
# time.sleep(10)
# print("object yet not destroyed")
# del t3
# time.sleep(10)
# print("By this time object compulsory will be destroyed")
# print("End of application")


# import time
# class Test:
#     def __init__(self):
#         print("Object Initialisation")
#
#     def __del__(self):
#         print("Fulfilling last wish and performing cleanup activites")
#
# list=[Test() ,Test() , Test()]
# del list
# time.sleep(5)
# print("End of application")

# class Test:
#     def __init__(self):
#         print("Object Initialisation")
#
#     def __del__(self):
#         print("Fulfilling last wish and performing cleanup activites")
#
# list=[Test() ,Test() , Test()]
# print("End of application")   #Will the object will be destroyed or not
#when the program ends , destructor will be called if we use del or not
#and by default all the objects will be destroyed for GC

# import sys
# class Test:
#     pass
# t1=Test()
# t2=t1
# t3=t1
# t4=t1
# print(sys.getrefcount(t1))  #This will count the no of references are there
# #How we got 5 , self will be by default refernce variable , that's why 5