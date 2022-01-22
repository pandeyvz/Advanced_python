# #various possible combination of try-except-else-finally
# --try without except or finally and vice versa is always invalid
# --try with only else is not valid , except block must be required
# --at a time we can take onlt 1 try , multiple except , 1 else , 1 finally
# --bw try and except and except and finally and except and else  u cant add some statement in the middle without identation
#
# #Userdefined exception
# every exception in python is class
# define and raise customized exceptions
# class classname(parent):
#     def __init__(self,arg):
#         self.msg=arg
# class TooYoungException(Exception):
#     def __init__(self,arg):
#         self.msg =arg
# class TooOldException(Exception):
#     def __init__(self,arg):
#         self.msg =arg
# age=int(input("Enter age "))
# if age>60:
#     raise TooYoungException("Plz wait some time")
# elif age<18:
#     raise TooOldException("u r late ")
# else:
#     print("Thanks for reg , u ll get match details ")
###########################################################################################
