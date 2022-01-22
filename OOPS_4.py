# #Inheritance :-Helps in code reusability
# #class childclass(Parentclass)
#
# class P:
#     a=10
#     def __init__(self):
#         self.b=20
#
#     def m1(self):
#         print("Parent class instance method")
#     @classmethod
#     def m2(cls):
#         print("Parent class method")
#     @staticmethod
#     def m3():
#         print("Parent class static method")
# class C(P):  #Inheritance
#     pass
# c=C()
# print(c.a) #Can call any variable of parent class
# print(c.b)
# c.m2()
# c.m3()

#object :-Parent for all python class

# class P:
#     def m1(self):
#         print("Parent class method")
# class C(P):
#     def m2(self):
#         print("child class method")
# c=C()
# c.m1()
# c.m2()


# class P:
#     a=10
#     def __init__(self):
#         self.b=20
# class C(P):
#     c=30
#     def __init__(self):
#         self.d=40
# c=C()
# print(c.a,c.b,c.c,c.d)

#It wont work because if child class has already constructor then it will not execute Parent class constructor
# therefore we have to use super().__init__() in child constructor

# class P:
#     a=10
#     def __init__(self):
#         self.b=20
# class C(P):
#     c=30
#     def __init__(self):
#         super().__init__() # As child class has to access the parent class even though constructor is defined
#         self.d=40
# c=C()
# print(c.a,c.b,c.c,c.d)

#Inheritance --IS-A Relationship:-Extend the class functionality
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eat_n_drink(self):
#         print("Eat biryani and drink beer")
#
# class Employee(Person):
#     def __init__(self,name,age,eno,esal):
#         super().__init__(name,age)   #This we are using to call name and age from parent class
#         self.eno=eno                #But this we have to reference as this is inside child class
#         self.esal=esal
#     def work(self):
#         print("coding python")
#     def empinfo(self):
#         print("Employee Name:",self.name)
#         print("Employee age:", self.age)
#         print("Employee eno:", self.eno)
#         print("Employee esal:", self.esal)
#
# e=Employee('Durga',32,872425,10000)
# e.eat_n_drink()
# e.work()
# e.empinfo()

#HAS-A Relationship :-do the require functionality mot extend
#Adding car class

#Employee is a person , employee has car , employee has name
# class Car:
#     def __init__(self,name,model,color):
#         self.name=name
#         self.model=model
#         self.color=color
#     def getinfo(self):
#         print('\tCar Name:{}\tCar Model:{}\tCar Color{}:'.format(self.name,self.model,self.color))
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eat_n_drink(self):
#         print("Eat biryani and drink beer")
#
# class Employee(Person):
#     def __init__(self,name,age,eno,esal,car):  #Since very employee requires Car functionality we are passing car
#         super().__init__(name,age)   #This we are using to call name and age from parent class
#         self.eno=eno                #But this we have to reference as this is inside child class
#         self.esal=esal
#         self.car=car
#     def work(self):
#         print("coding python")
#     def empinfo(self):
#         print("Employee Name:",self.name)
#         print("Employee age:", self.age)
#         print("Employee eno:", self.eno)
#         print("Employee esal:", self.esal)
#         print("Car Info:")
#         self.car.getinfo()
#
# c=Car('Innova','2.5v','grey')
# e=Employee('Durga',32,872425,10000,c)
# e.eat_n_drink()
# e.work()
# e.empinfo()