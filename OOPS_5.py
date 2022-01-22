# Method Resolution order

# class A: pass
# class B(A):pass
# class C(A):pass
# class D(B,C):pass
# print(A.mro())  #mro is a method
# #By default each class has one parent class , i.e. Object
# print(B.mro())  #First it will search in B class then A class then Object class
# print(C.mro())
# print(D.mro())
#
# class A:
#     def m1(self):
#         print("A class method")
# class B(A):
#     def m1(self):
#         print('B Class method')
# class C(A):
#     def m1(self):
#         print('C class method')
# class D(B,C):
#     def m1(self):
#         print('D class method')
# # d=D()
# # d.m1()  #D class method will be called ,
#
# class D(B,C):pass
#
# d=D()
# d.m1() #if D has no methods then which method will be called , parent B method will be called as per order
# #if B is not ther then C will be called , if c is not there then A will be called
# #But if the range is too much , multiple levels r ther  , many classes are there then how will we decide, therefore MRO will come

#Super Method:- Inbulit method:-To call parent constructor from child constuctor
#
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Student(Person):
#     def __init__(self,name,age,rollno,marks):
#         super().__init__(name,age) #Calling parent constructor values to child class
#         self.rollno=rollno
#         self.marks=marks
#     def display(self):
#         print("Name:",self.name)
#         print("Age:", self.age)
#         print("Rollno:", self.rollno)
#         print("Marks:", self.marks)
# s=Student("durga",32,101,98)
# print(s.display())

#EXAMPLE:--2

class P:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print("Parent instance method")

    @classmethod
    def m2(cls):
        print('Parent class method')

    @staticmethod
    def m3():
        print("Parent Static method")

class C(P):
    a=888
    def __init__(self):
        self.b=999
        super().__init__()
        print(super().a) #calling parent class variables
        super().m1()  #Calling parent class method
        super().m2()
        super().m3()
c=C()