#Difference between str() and repr()
#()str internally calls __str__() and repr() calls __repr__()
#()str converts string to object and ()repr converts object to string
#
# class Employee:
#     def __init__(self,name ,salary):
#         self.name=name
#         self.salary=salary
#     def __str__(self): #If we will not use this then we will not get the desired output
#         return ('{} salary is {}'.format(self.name,self.salary))
# e=Employee('Vineet',50000)
# print(e)

class Employee:
    def __init__(self,name ,salary):
        self.name=name
        self.salary=salary
    def __repr__(self):
        return ('{} salary is {}'.format(self.name,self.salary))
e=Employee("Vineet",50000)
print(e)

# Mini Project Banking Application

# class Account:
#     def __init__(self,name,balance ,min_balance):
#         self.name=name
#         self.balance=balance
#         self.min_balance=min_balance
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#     def withdraw(self,amount):
#         if self.balance-amount >= self.min_balance:
#             self.balance-=amount
#         else:
#             print("sorry insufficient funds")
#     def printstatement(self):
#         print("Account Balance:",self.balance)
#
# class Current(Account):
#     def __init__(self,name,balance):
#         super().__init__(name,balance,min_balance=-1000)
#     def __str__(self):
#         return ('{} Current account balance {}'.format(self.name,self.balance))
#
# class Savings(Account):
#     def __init__(self,name,balance):
#         super().__init__(name,balance,min_balance=0)
#     def __str__(self):
#         return ('{} Savings account balance {}'.format(self.name,self.balance))
#
# c=Savings("Vineet",50000)
# c.deposit(5000)
# c.withdraw(60000)
# print(c)
#
# c1=Current("Ravi",20000)
# print(c1)


