# r-->open a existing file for read operation , it is default mode
# w-->open a existing file for write operaion , override existing data , if file not available then it will create it
# a-->open a existing file for append operaion , will not override existing data , if file not available then it will create it
# r+ -->read and write , not override
# w+-->write and read  , override
# a+ -->to append and read
# x-->to open a file in exclusive creation mode for write operation , file should not be available
# rb-->
# wb-->
# Various properties of file object:--
# f.name
# f.mode
# f.closed      #These things are variables , properties
# f.readable()    #is method as they have parenthesis
# f.writable()
# f=open("File_1.txt",'w+')
# print("Filename:", f.name)
# print("Filemode:",f.mode)
# print("Is file readable:",f.readable())
# print("Is file writable:",f.writable())
# print("Is File closed:",f.closed)
# f.close()
# print("Is file closed:",f.closed)
###################################################
# #Writing data to text files
#
# f=open("File_1.txt",'w+')
# f.write("Vineet\n")
# f.write("Pandey\n")
# print("Data written to file successfully")

# f=open("File2.txt",'w+')
# list=["sunny\n","bunny\n","Vinny\n","Chinny\n"]
# f.writelines(list)
# print("List of lines written to the file successfully")
# f.close()
#
# #Reading character data from text files
#
# f=open("File2.txt",'r')
# data=f.read(10)
# print(data)
# f.close()
#
# f=open("File2.txt",'r')
# data=f.read()
# print(data)
# f.close()

#To read data line by line
# f=open("File2.txt",'r')
# line1=f.readline()
# print(line1,end="")  #by giving end="" we can avoid the newline character that was automatically coming
# line2=f.readline()
# print(line2,end="")
# f.close()

#To read all lines in the list
# f=open("File2.txt",'r')
# lines=f.readlines()
# for line in lines:
#     print(line, end="")

# f=open("File2.txt",'r')
# print(f.read(3))  #when we use read statement cursor move to that specified count if you again call that read(n) it will
# print(f.readline()) #start the count from that previous cursor point , when we used the readline the output we got was from the existing cursor point
# print(f.read(4))

# #With Statement:- i want my file to be closed automatically,even in the case of exceptions also we dont need to close this  if i want to run
# group operations then also we need this , whatever written below the with statement will be considered as a code within with block
# with open("File2.txt",'w') as f:
#     f.write("Durga\n")
#     f.write("Software\n")
#     f.write("solutions\n")
#     print("Is file closed :",f.closed)      #Here this is under block so this is not closed , we will get false
# print("Is file closed :",f.closed) #By use with operation file get automatically closed after execution

#The seek() and tell() method
#tell():can be used to tell the current position of cursor
# f.seek(offset,fromwhere ) , offset represents the no. of positions . seeking the cursor to specified location
# but here is one twist , allowed value for fromwhere is as below , but these conditions are in python 2 not in python 3 :-
# 0-->from beginning of the file
# 1-->from current position
# 2-->from end of the file

# f=open("File2.txt",'r')
# f.write("Durga\n")
# f.write("Software\n")
# print(f.tell())
# print(f.read(3)) #it will read first 3 characters and cursor will go to that position
# print(f.tell())
# print(f.seek(2,4)) #Put cursor to specified location
#
# print(f.read())
#
# data ="all students are STUPIDS"
# f=open('abc.txt','w')
# f.write(data)
# with open( 'abc.txt','r+') as f:  # r+ =read then write
#     text=f.read()
#     print(text)
#     print( "the current cursor position:",f.tell())
#     f.seek(17)
#     print(" the current cursor position:",f.tell())
#     f.write("GEMS!!!") #now data will overwrite from 17 as cursor is there
#     f.seek(0)  #now again pointer is coming to 0th position
#     text=f.read()
#     print("data after modification:", text)

##################

# How to check a particular file exist or not , we will use OS library
# OS has path module contains isfile() to check whether file exist or not os.path.isfile(filename)
# import os,sys
# fname=input("Enter the file name: ")
# if os.path.isfile(fname):
#     print("File exists :",fname)
#     f=open(fname,'r')
# else:
#     print("file not exist:",fname)
#     sys.exit(0) #stop the program
# print("the content of the file is :")
# data=f.read()
# print(data )

#WAP to print no, of lines , words and charactes present in the given file

f=open("File2.txt",'r')
lines=f.readlines()
print(lines)
count=0
for line in lines:
    count+=1
print(count)      #No of lines got printed
list=f.read()
for l in list:
    print(l)