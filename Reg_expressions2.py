# #Write a RE to represent Yava language identifiers:-
# 1.Allowed characters are alphabets , digits ,#
# 2.First character should be lower case alphabet symbol from a to k
# 3.Second character should be any digit divisible by 3
# 4.The length of identifier shoud be atleast 2
# It will look like this as below:-
# [a-k][0369][a-zA-Z0-9#]*  # * means any no. of time , length of identifiers means after that length we can take anything
#
# import re
# s=input("Enter identifiers to validate :")
# m=re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',s)
# if m!=None:
#     print(s ,'is valid yava identifier')
# else:
#     print(s,'is not valid yava identifier')
####################################################################################
# 2.Write a regular expression tp represent all 10 digit mobile nos
# --First digit should be [6789] either 6 7 8 9
# --remaining no restrictions
# import re
# s=input("Enter the mobile no :")
# m=re.fullmatch("[6789][0-9]{9}",s) #It means first digit should be either 6,7,8 or 9 and 0-9 is for 9 times
# if m!=None:
#     print("Valid mobile no")
# else:
#     print("Invalid mobile no ")

#3.Now for 10 digit , 11 digit , 12 digit or 13 also
# 10: 6to 9, 9 digits
# 11:the first digit should be 0
# 12:the first 2 digit should be 91
# 13.the first 3 digit should be +91
#  Assignment:------
# import re
# s=input("Enter the mobile no :")
# m=re.fullmatch("[6789][0-9]{9}",s) #It means first digit should be either 6,7,8 or 9 and 0-9 is for 9 times
# if m!=None:
#     print("Valid mobile no")
# else:
#     print("Invalid mobile no ")
############################################################
#4.Write a RE to extract all mobile nos. present in input.txt file and display to console or write to output.txt

# import re
# f1=open('Re.txt','r')  #To read data from Re.txt
# f2=open('Op.txt','w')  #To write to Op.txt
# for line in f1:
#     # print(line)
#     list=re.findall('[6-9]\d{9}',line) #We need to findall the nos. in the line thats why target is line
#     # print(list)
#     for number in list:
#         f2.write(number+"\n")
# print("Extracted all mobile nos. into op.txt")
# f1.close()
# f2.close()
#But there is 1 flaw , where there is 11 digit nos. that is also get considered by deduction the extra value but we dont want that
#####################################################
# Web Scrapping by using Regular expression:-process of collecting data from webpages
# urllib.request module is required to get the url details
# import re,urllib
# from urllib import request
# sites=['http://google.com','http://rediff.com','http://gmail.com']
# for s in sites:
#     print('Searching....',s)
#     u=urllib.request.urlopen(s)
#     text=u.read() #It will read all the url details but will be in bytes format
#     title=re.findall("<title>.*</title>",str(text),re.IGNORECASE)  # to convert bytes format  to str we have used str(text)
#     print(title)
##########################################################################
#WAP to read all phone no from redbus.com and write that no. to a text file
# import re,urllib
# import urllib.request
# s="https://www.redbus.in/info/contactus"
# u=urllib.request.urlopen(s)
# print("Opening redbus website")
# text=u.read()
# numbers=re.findall('[0-9]{3}[-][0-9]{8}', str(text))
# for n in numbers:
#     print(n+'\n')

################################################################################
#WAP tp verify if the email id is correct gmail id or not
# RE= \w[a-zA-A0-9_.]*@gmail[.]com     # *is for any number
import re
s=input("Enter mail id ")
m=re.fullmatch("\w[a-zA-A0-9_.]*@gmail[.]com",s)
if m!=None:
    print("Valid mail id")
else:
    print("Invalid mail id")

#WAP is car registration no is valid TS(Telangana state) number or not
First letter should be TS only
TS[012][0-9][A-Z]{2}\d{4}
