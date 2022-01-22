 #Recursive functions :- A function that can call itself
# for eg:- fact(3)=3*fact(2)
#          fact(2)=2*fact(1)  i.e. fact(n)=fact(n)*fact(n-1)
#
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print(fact(3))
#
# ###Anonymous function:-declare function without name , nameless function , instant use purpose
# def squareIt(n):
#     return n*n
# or we can write
# s=lambda n:n*n     #lambda is keyword to define anonymous function ,, syntax lambda input:expression
# print(s(4))

#WAP To write a sum of 2 no. using lambda functions:-
# sum=lambda a,b:a+b
# print(sum(2,10))
#
# #we can pass a function as argument to other function, below function always expect other function as argument
# #filter()
# #map()
# #reduce()
#
# 1.filter() :- i want to filter only required things from the group if we want to filter some objects
#      syntax:- filter(function,sequence) :- for every element in the sequence this function will be applied

##################To generate random pwd of 6 length
# 1,3,5 are alphabet symbols
# 2,4,6 are digits
# Note:-- 65 = A , 66=B ,.....65+25=Z   , to convert this character to int values use ,, chr(A)--->Int
from random import *
for i in range(10):
    print(chr(randint(65,65+25)),randint(0,9),chr(randint(65,65+25)),randint(0,9),chr(randint(65,65+25)),randint(0,9) )

