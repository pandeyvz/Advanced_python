# Method Overloading :- is not applicable in python , if we declare 2 method with the same name then
#old method will be gone and only new or recent method will work
#
# class Test:
#     def m1(self):
#         print("No arg method")
#     def m1(self,a):
#         print("One arg method")
#
# t=Test()
# t.m1(10)
#
# #But how we will handle below types :- By using variable length and default arguments
# m1(int i)
# m1(int i , int j , int k)

# Variable arguments:--

class Test:
    def sum(self,*a): # *a signifies we can take any no. of arguments
        total=0
        for x in a:
            total=total+x
            print("The Sum:",total)
t=Test()
t.sum()
t.sum(10)
t.sum(10,20)
t.sum(10,20,30)