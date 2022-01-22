#Nested try-except-finally
# try:
#     print("Outer try block")
#     try:
#         print("Inner Try block")
#         print(10/0)
#     except ZeroDivisionError:
#         print("Inner except block")
#     finally:
#         print("Inner finally block")
# except:
#     print("Outer except block")  #Only this will not execute as there is no error in main try
# finally:
#     print("Outer finally block")

try:
    stmt-1
    stmt-2
    stmt-3
    try:
        stmt-4
        stmt-5
        stmt-6
    except XXX:
        stmt-7
    finally:
        stmt-8
    stmt-9
except YYY:
    stmt-10
finally:
    stmt-11
stmt-12

1.If there is no exception :- stmt- 1 ,2,3,4,5,6,8,9,11,12 only 7 and 10 will not execute
2.if exception raised at stmt-2 and corresponding except block match :- 1,10,11,12
3.If exception raised at stmt-2 and corresponding except block not matched then AT but finally will execute definately :- 1 ,11,AT
4.if exception raised at stmt-5 and corresponding inner except block matched then :- 1,2,3,4,7,8,9,11,12, NT
5.If exception raised at stmt-5 and corresponding inner except block not matched but outer except block matched :-1,2,3,4,8,10,11,12 #for inner
   # its like abnormal termination thats why stmt-9 will not execute
6.If exception raised at stmt-5 and corresponding inner except block not matched neither outer except block matched :-1,2,3,4,8,11
7.If exception raised at stmt-7 and corresponding except  block  matched :-here if pointer is coming to stmt-7 it means ther must be some issue in try
    stmt-4,5,6 but we dont know but stmt-7 also has issue thats why it will check the outer except:-1,2,3,...,8,10,11,12
8.If exception raised at stmt-7 and corresponding except  block not matched :-1,2,3,...,8,11,AT
9.If exception raised at stmt-8 and corresponding except  block matched :-1,2,3,4,5,6,7(may or may not ),10,11,12
10.If exception raised at stmt-8 and corresponding except block not matched :-,1,2,3,4,5,6,7(may or may not ),11,AT
11.If exception raised at stmt-9 and corresponding except block matched :- 1,2,3,4,5,6,7(may or may not),8,10,11,12,NT
12.If exception raised at stmt-9 and corresponding except block not matched :-1,2,3,4,5,6,7(may or may not),8,11,AT
13.if exception raised at stmt-11 or stmt-12 it is always abnormal termination

########################################################################################################################
#else block :-if there is no exception then else block will execute , but finally will always execute whether exception is there or not
try:
    risky code
except:
    will be executed if exception in try
else:
    will be executed if there is no exception in try
finally :
    will always execute whether there is exception or not
