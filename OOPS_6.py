#Polymorphism
#Duck Typing philoshopy:-Python always give the importance to behaviour rather than type,type will be decided from behaviour
# class Duck:
#     def  talk(self):
#         print("Quack quack")
#
# class Dog:
#     def  talk(self):
#         print("Bhou Bhou")
#
# class Cat:
#     def  talk(self):
#         print("Meow Meow")
#
# class Goat:
#     def  talk(self):
#         print("Myah Myah")
#
# def f1(obj):
#     obj.talk()
#
# l=[Duck(),Dog(),Cat(),Goat()]
# for obj in l:
#     f1(obj)

#Thre is no way to specify the type explicitly

#Overloading :-
# Operator overloading :-Same operator for different purpose , sometime addition , sometime concatenation,java dont support
# Method overloading :- Same method but different arguments different use

# Operator overloading
# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#
    # def __add__(self, other):
    #     return self.pages+other.pages    #magic method we can add object
#
    # def __add__(self, other): #This we r using to change the return value so that we can add mor than 2 object
    #     total=self.pages+other.pages
    #     return Book(total)
#
    # def __mul__(self, other):
    #     return self.pages*other.pages
#
#     def __str__(self):
#         return str(self.pages)
# b1=Book(100)
# b2=Book(200)
# b3=Book(300) #If 3 objects are there then how we will add
# print(b1+b2)  #Adding 2 book objects , error we will get , which operation you want here conczt or add
# # if u want total no. of pages to make the above statement true u have to add magic method i.e.__add__
# print(b1*b2) #magic method is __mul__
# print(b1+b2+b3) #It will not work as b1+b2 is int will return but b3 is string int plus book will not happen
# #so we have to modify the magic function return value
# #After modifying we are getting the address , so we have to define one str function to get the actual value
# b4=Book(400)
# print(b1+b2+b3+b4)


#Another example

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def __gt__(self, other):   # magic function to check greater than
#         return self.marks>other.marks   # self.marks signifies to s1 , other.marks signifies to s2
#
# s1=Student('Vineet',100)
# s2=Student('Nikita',200)
# print("s1>s2:",s1>s2)   #It will throw an error directly we cant compare 2 objects so we will define one magic method

## Another example
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#
#     def __mul__(self, other):
#         return self.salary*other.days
#
# class Timesheet:
#     def __init__(self,name,days):
#         self.name=name
#         self.days=days
#     def __mul__(self, other):
#         return self.days*other.salary
# e=Employee("Vineet",100)
# t=Timesheet("Vineet",25)
# print("This month salary:",e*t)   #We have to call magic func
# print("This month salary:",t*e)   #for this also we have to call magic function
