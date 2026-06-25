# class Data:
#     def spam(self,*args):
#         if len(args)==1:
#             return args[0]
#         elif len(args)==2:
#             return args[0]+args[1]
#         elif len(args)==3:
#             return args[0]+args[1]+args[2]
#         else:
#             raise ValueError
        
# d= Data()



# class Operation:
#     def math(self,a=None,b=None,c=None):
#         if a is not None and b is not None and c is not None:
#             return a+b+c
#         elif a is not None and b is not None:
#             return a+b
#         elif a is not None:
#             return a
#         else:
#             return 0
# x=Operation()
# print(x.math(10))
# print(x.math())

# class Total :
#     def __init__(self,marks):
#         self.marks=marks
        
#     def __add__(self,other):
#         return self.marks+other.marks
# t=Total(50)
# t1=Total(50)
# print(t+t1)   #TypeError: unsupported operand type(s) for +: 'Total' and 'Total'


# class Operation :
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b 
#         self.c = c 
#     def __add__(self,other):
#         return Operation(self.a+other.a,self.b+other.b, self.c + other.c)
#     def __sub__(self,other):
#         return Operation(self.a -other.a,self.b-other.b, self.c - other.c)
#     def __str__(self):
#         return f'{self.a},{self.b},{self.c}'
    
# o = Operation(1,2,3)
# o1=Operation(2,3,4)
# print(o+o1)
# print(o-o1)
# print(dir(int))     
# print(int('0b010',base=16))  