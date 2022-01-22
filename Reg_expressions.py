#To represent a group of strings according to particular pattern we write regular expression
# Application:
# 1.Validations of data :-Eg- MObile no should start with 9,8,7,6
# 2.To develop Pattern Matching application.Eg. ctrl+f, grep
# 3.To develop Translators like compilers,interpreters,assemblers
# 4.To develop digital circuits
# 5.To develop communication protocols
# re module contains several inbuilt functions to use regular expressions
# List of functions:-

# 1.compile():-Create regex object with pattern
# import re
# pattern=re.compile('Python') #regex object , i want to search for python
# print(type(pattern))
#
# 2.finditer() :-return and iterate
# matcher=pattern.finditer("Learning python is very easy") #To check how may python words are there in line
# 3.start():Start index of match
# 4.end():-end+1 index of the match
# 5.group():-Returns matched string , returns the matched items

############################################################################
# import re
# pattern=re.compile("ab")
# matcher=pattern.finditer("abaababa")
# count=0
# for match in matcher:
#     count+=1
#     print('match is available at start index:',match.start( ))
#     print("The no of occurences:",count)

# import re
# pattern=re.compile("ab")
# matcher=pattern.finditer("abaababa")
# count=0
# for m in matcher:
#     count+=1
#     print('start:{},end:{},group:{}'.format(m.start(),m.end(),m.group()))
#     print("The no of ocuurences:",count)

# #To short the above code
# import re
# matcher=re.finditer('ab',"abaababa") #Bypassed compile line
# count=0
# for m in matcher:
#     count+=1
#     print('start:{},end:{},group:{}'.format(m.start(),m.end(),m.group()))
#     print("The no of ocuurences:",count)
#
# #Character classes:--
# [abc]--either a or b or c
# [^abc]--except a and b and c
# [a-z]-->Any lowercase alphabet symbols
# [A-Z]-->any upper case alphabet symbols
# [a-zA-Z]-->Any Alphabet symbol
# [0-9]-->Any digit
# [a-zA-Z0-9]-->Any alphanumeric character
# [^a-zA-Z0-9] -->Except alphanumeric chracter
# ^ :-Cap symbol is for except
# import re
# matcher=re.finditer('[a-z]','a7b@k9z')
# for m in matcher:
#     print(m.start(),'......',m.group())

####################################################################
#Predefined character classes
# \s -->space character
# \S -->except space character
# \d --> [0-9] , any digit
# \D -->except digits
# \w -->alphanumeric character
# \W -->Any character except word(special character)
# .  --> Every character

# import re
# matcher=re.finditer('.','a7b @k9z')
# for m in matcher:
#     print(m.start(),'......',m.group())
###############################################################
# Quantifiers:- To specify the The no. of occurrences
# a -->Exactly 1 a it will count
# a+ --> This will count a group of a side by side as single count or atleast 1 a
# a* --> Any no. of a's including zero number also
# a? --> Atmost 1 a , either 1 a or 0 no. of a's
# a{3} --> exactly 3 a i want
# a{2,3} -->Min 2 no. of a and maxm of 3 nos. of a
# a{2}a* --> 2 a is mandatory and then u can take any nos. of a
# ^a --> Is the given target string start with a or not
# a# --> Is the given target string end with a or not
# In Reg expression cursor move to next to the 1 more of last index also

# import re
# matcher=re.finditer('a{2}a*','abaabaaab')
# for m in matcher:
#     print(m.start(),'......',m.group())

#########################################################
# Important fuctions of re module
# 1.match() :-To check if the given pattern is at the beginning of the target string or not , if it is available then return match object or none
# 2.fullmatch() :-To match pattern to total target string, read 1 identifier from the string
# 3.search() :-To search the given pattern in the target string if it match then it will return match object of the first occurence
# 4.findall() :-To findall occurences of the matches
# 5.finditer() :-It returns iterator of match object, to match multiple times
# 6.sub() :-substitution or replacement , re.sub(regex,pattern,targetstring)
# 7.subn() :-To know the no of replacement , return type is not string its tuple(resultstring ,no of replacement) ,re.subn(regex,replacement,targetstring)
# 8.split() :-
# 9.compile()

# 1.Match
# import re
# s=input("Enter pattern to check :")
# m=re.match(s,'abcdefgh')
# if m!=None:
#     print("Match is available at the beginning of the string ")
#     print("Start index:{} and End index:{}".format(m.start(),m.end()))
# else:
#     print("Match is not available at the beginning of the string ")

# 2.fullmatch()
# import re
# s=input("Enter pattern to check :")
# m=re.fullmatch(s,'abcdefgh')
# if m!=None:
#     print("Full string matched ")
# else:
#     print("full string doesnt matched")

#3.search()
# import re
# s=input("Enter pattern to check :")
# m=re.search(s,'abaabaaab')
# if m!=None:
#     print("match is available")
#     print("first occurence with start index:{} and end index:{}".format(m.start(),m.end()))
# else:
#     print("full string doesnt matched")

#4.findall()
# import re
# l=re.findall('[0-9]','a7b9k6z') #Findall the ocuurrences and store in a list
# print(l)

#5.finditer()
# import re
# matcher=re.finditer('\d','a7bk9z6')
# for m in matcher:
#     print(m.start(),m.end(),m.group())

#6.sub()
# import re
# s=re.sub('\d','#','a7b9k5t9k') # Here the pattern is digit , # is the replacement and a7b9k5t9k is the target string
# print(s)

#7.subn():
# import re
# s=re.subn('\d','xxxx','a7b9k5t9k') # Here the pattern is digit , # is the replacement and a7b9k5t9k is the target string
# print(type(s))
# print("the result string : {} and the no.of replacement:{}".format(s[0],s[1] ))

# 8.split():
import re
l=re.split('-','10-20-30-40-50') # here we r going to split according to hyphen module
print(l)
m=re.split('\.','www.google.com') # if we want to use dot as a normal we have to use backslash
for i in m :
    print(i)