# Built in functions:- print(),len(),eval(),input()
# Default return value is none for user defined func
#we can return any no of values in python
# def f1():
#     print("Hello")
# f1() #we are calling here so we will get the output
# print(f1()) #Here we r printing but their is no return statement thats why by default it will return NONE
###Factorial of the numbers
# def fact(n):
#     result=1
#     while n>=1:
#         result=result*n
#         n=n-1
#     return result
# for i in range (10):
#     print("The factorial of {} is {}".format(i,fact(i)))

###To check for multiple return values
# def sum_sub(a,b):     #Here a,b are formal parameters
#     sum=a+b
#     sub=a-b
#     return sum,sub
# x,y=sum_sub(100,50)     #100,50 is actual arguments
# print("The sum is ",x)
# print("The sub is ",y)

###To check for multiple return values
# def calc(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return sum,sub,mul,div
# t=calc(100,50) ##here we are creating a tuple which contains all diff values instead of x ,y,z,a
# print(type(t))
# for x in t:
#     print(x)
#
# #Types of arguments :-
# -->positional arguments:-The no. of arguments and order of arguments must be same
# -->keword arguments:- order is not important
# -->default arguments
# -->variable length arguments
# examples:-
# keword arguments:-
# def wish(name ,msg):
#     print("hello",name,msg)
# wish(name="durga",msg="Good morning")
# wish(msg="Good morning",name="durga")  #this is also same as above , order is not important
# wish("durga",msg="good morning") #Here durga is positional argument , msg is keyword argument , but there is no problem in that it will work perfectly
# wish(msg="good morning","durga")  #here we will get error , first positional argument , then keyword argument.

# #####Default arguments :--define default value for arguments
# def wish(name="Guest"):
#     print("Hello",name,"Good evening")
# wish("Durga")   #here we are passing durga so will get the name
# wish()  #here we not passing so it will take default arguments

# def wish(name="Guest",msg): #here it will come error as default argument should be the last argument only
#     print("Hello",name,msg)
#
# ####Variable Length arguments:-- if we have to increase the arguments in different function call then we have to declare separate func every time
# and code size will increase , thats why we will use variable length arguments  by using *a or *n or anything
# for eg:--
# def sum(*a):     #a will be internally as tuple
#     result=0
#     for x in a:   #since a will act as tuple so x will iterate
#         result=result+x
#     print("The sum is :",result)
# sum()
# sum(10)
# sum(10,20)
# sum(10,20,30)
# sum(10,20,30,40)

#We can take positional and variable arguments together and there is no order problem
# def sum(name,*a):
#     result=0
#     for x in a:   #since a will act as tuple so x will iterate
#         result=result+x
#     print("The sum by ",name,":",result)
# sum("Durga")
# sum("Ravi",10)
# sum("Pavan",10,20)
# sum("Shiva",10,20,30)
# sum("Anil",10,20,30,40)

#Keyword variable length arguments
# def display(**kwargs):    #### 2 star is for variable length keyword arguments
#     print(type(kwargs))    ##this kwargs will become dictionary
#     print("Record information")
#     for k,v in  kwargs.items():
#         print(k,".....",v)
#
# display(name="Durga",marks=100,age=48,GF="Sunny")
# display(name="Ravi",wife1="Nandita",wife2="abc",wife3="xyz")

####Modules:-is a file contains a group of functions
####Package:- group of different modules
####packages:- a group of similar packages

#Python support 2 types of variables:-
# 1.global variable :- defined outside function which is available for all module
# 2.Local variable :-defines inside function only
a=10
def f1():
    global a              #if we want to declare this as a global , then we have to use global a
    a=777
    print("f1:",a)     #here a will take local variable
def f2():
    print("f2:",a)    #here a will take global variable
f1()
f2()     #if we will call f2 ffirst then a=10 will take as f1 is not called where global a is declared
#####
# a=10
# def f1():      # Here local variable will take preference over global but if we want to global as highest priority then
#     a=20
#     print(a)
#     print(globals()['a'])     #This  global is dictionary and in that  a values we want
# f1()