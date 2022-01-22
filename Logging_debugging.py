# Logging exceptions:
# by using log files we can debug the important event that has happended
# to implement logging , logging module is required
# Logging levels:-
# 1.critical=50=needs high attention
# 2.error=40= a serious problem
# 3.warning=30=alert to take special care
# 4.Info=20=important info
# 5.Debug=10
# 6.Notset=0
#
# how to implement logging
# --name of file in which data we have to store
# --level messgaes
# by using basicConfig() of logging module
# import logging
# logging.basicConfig(filename='log.txt',level=logging.WARNING)
# logging.debug(message)  #By using these we can write this info to file
# logging.info()
# logging.warning()
# logging.critical()
# logging.error()

# WAP to create a log file and write warning and higher level messages (error and critical)
# import logging
# logging.basicConfig(filename='log.txt',level=logging.WARNING)
# print("demo")
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")  #Only this and below data will be added to the file , only selected and higher level will be added
# logging.error("error")
# logging.critical("critical")

#WAP to write python program exceptions to the log file -- logging.exception(msg)
import logging
logging.basicConfig(filename='log.txt', level=logging.INFO)
logging.info("a new request came")
try:
    x=int(input("Enter first no"))
    y=int(input("Enter second no."))
    print(x/y)
except ZeroDivisionError as msg:
    print("Cant divide with 0")
    logging.exception(msg)     #Here we are also storing the msg as a logs
except ValueError as msg:
    print("Enter only int values")
    logging.exception(msg)
logging.info("req processing completed")

##########################################################################################################
Debugging :process of identifying and fixing the bug is called as debugging and its the job of developers
bug:-any mismatch bw expected results and actual result
--common way of performing debugging is by using print statement , but there is 1 bigger problem after fixing this
we have to remove all print statement thats why it is not recommended

i.e why we will for *****assert statement***** :-advantage is after performing the debug it will automatically get disabled on the client machine
Types of assert statement:-
1.simple version
2.Augmented version

1.simple version :- assert conditional_expression , if this is true then code will continue if it false then error will be raised
2.Augmented version :-assert conditional_expression,message , if this is false then we will get some handful message
