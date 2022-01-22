# # 1.Setter and Getter
#
# class Student:
#     def setName(self,name):    #Setter Method :-Also Known as Mutator methods
#         self.name=name
#
#     def getName(self):         #Getter Method :- Also Known as accessor methods
#         return self.name
#
#     def setMarks(self,marks):
#         self.marks=marks
#
#     def getMarks(self):
#         return self.marks
#
# l=[]
# n=int(input("Enter no of students "))
# for i in range(n):
#     s=Student()
#     name=input("Enter name of Students:")
#     marks=int(input("Enter Marks of Students "))
#     s.setName(name)
#     s.setMarks(marks)
#     l.append(s)
# print(l)
#
# for s in l:
#     print("Student Name:" ,s.getName())
#     print("Student Marks:" ,s.getMarks())
#     print()


#2.Class Methods :- Not using any instance variable only using Static variables
# @classmethod , m1(cls): --pointing to current class object
# We can call class methods by using classname or object reference

# class Animal:
#     legs=4   #Static variable
#
#     @classmethod
#     def walk(cls,name):
#         print('{} walks with {} legs'.format(name, cls.legs))
#
# Animal.walk('Dog')
# Animal.walk('Cat')

#To check the no. of objects created for class
#
# class Test:
#     count=0 #Static variable
#     def __init__(self):
#         Test.count=Test.count+1
#     @classmethod
#     def noofobjectsCreated(cls):
#         print("The no of objects created :", Test.count) #Here we are calling only static varisble it means we have to call
#                                                          #Class method
# t1=Test()
# t2=Test()
# t3=Test()
# Test.noofobjectsCreated()

#3.Static Method :- Inside method if we are not using instance variables and static variables
#Genral utility methods :- Static methods

# @staticmethod :- To call , either by class name or object reference

class DurgaMath:

    @staticmethod
    def add(x,y):
        print("The sum :", x+y)
    @staticmethod
    def product(x,y):
        print("The product :",x*y)
    @staticmethod
    def average(x,y):
        print("The average :",(x+y)/2)

DurgaMath.add(10,20)
DurgaMath.product(10,20)
DurgaMath.average(10,20)