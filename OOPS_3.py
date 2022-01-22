#Inheritance
#composition
#Method Resolution order

#Polymorphism
#duck typing
#Operator overloading
#Overriding

#encapsulation
#interface
#abstract class
#private public protected

#Inheritance
# Members of 1 class inside another class --:
# -By composition(HAS-A Realionship) :-By using class name or by creating object
# -By inheritance (IS-A relationship)

# -By composition(HAS-A Realionship) :-
# class Engine:
#     engine specific functionality
# class Car:   #has Engine reference (Code reusability advantage )
#     e=Engine()
#     e=m1()
#     e=m2()


# class Engine:
#     a=10
#     def __init__(self):
#         self.b=20
#
#     def m1(self):
#         print("Engine Specific functionality ")
# class Car:
#     def __init__(self):
#         self.engine=Engine()
#
#     def m2(self):
#         print("class car using engine class functionality ")
#         print(self.engine.a)   #Here we can use Engine.a also as a is a atatic variable
#         print(self.engine.b)
#         self.engine.m1()
# c=Car()
# c.m2()

class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print("Car name:", self.name)
        print("Car model:", self.model)
        print("Car color:", self.color)
class Employee:
    def __init__(self,eno,ename,car):
        self.eno=eno
        self.ename=ename
        self.car=car
    def empinfo(self):
        print("Emp no.:",self.eno)
        print("Emp name.:", self.ename)
        print("Car information.....:")
        self.car.getinfo()
car=Car("Innova","2.5v","balck")
emp =Employee(100,"Durga",car)
emp.empinfo()