# Exception handling comes in picture during runtime errors(zero division error , type error, value error,file not found error, EOF error)
# exception:-unwanted event that disrupt the normal flow of program
# Every exception in python is class
# try:
#     risky code
# except:
#     handling code
#
# try:
#     stmt-1
#     stmt-2 #if stmt has error then it will go to except and stmt 3 will bypass as once it will go to except it will not return to try
#     stmt-3
# except xxx:
#     stmt-4
# stmt-5
# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     print("Exception raised and its description is :",msg)

#According to ur risky code , there may be more than 1 except statement
# try:
#     x=int(input("Enter the first no"))
#     y=int(input("Enter the second no"))
#     print(x/y)   # Here we can get value error if suppose x not provided also we can get zero division error , except statement macthed from top to bottom
# except ZeroDivisionError:
#     print("Cant divide with 0")
# except ValueError:
#     print("Plz enter valid integer value")
#
# #Single except block that can handle multiple exceptions
# except(execution1,execution2,......)
#     handling code
# try:
#     x=int(input("Enter the first no"))
#     y=int(input("Enter the second no"))
#     print(x/y)   # Here we can get value error if suppose x not provided also we can get zero division error , except statement macthed from top to bottom
# except (ZeroDivisionError,ValueError) as msg :
#     print("Plz provide valid numbers only and problem is:",msg)

#default except block:-if we have covered all the exceptions but unknown  exception occurred then we use
# eg:-
# here if 0 division error will come then fine we have used except but if value error comes then default except statement will be used
try:
    x=int(input("Enter the first no"))
    y=int(input("Enter the second no"))
    print(x/y)   # Here we can get value error if suppose x not provided also we can get zero division error , except statement macthed from top to bottom
except ZeroDivisionError :
    print("cant divide with 0")
except:      #But default except must be last except
    print("Default except:Plz provide valid input")

#finally block :- To maintain cleanupcode
----if no exception finally block will be executed
----if an exception raised and handled finally block will be executed
----even in the case of abnormal termination finally block will be executed

#os.__exit(0):-This module will shutdown the python virtual machines and then only finally block cant be executed
#control flow in try except finally
try:
    stmt-1
    stmt-2
    stmt-3
except XYZ:
    stmt-4
finally:
    stmt-5
stmt-6
1.if no exception : 1,2,3,5,6 NT(Normal termination)
2.If an exception raised at 2 and matched except block is available them 1 4,5,6,NT
3.If an exception raised at 2 and no matched except block then abnormal termination , that is 1,5,AT
4.If and exception  raised at 4 it is always AT , but before AT stmt-5 will be executed
