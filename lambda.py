#########################################################################
#                           LAMBDA FUNCTIONS


# Definition:
# A lambda function in Python is a small, anonymous function defined using the lambda keyword instead of def


# syntax :   lambda arguments: expression

# new_var = lambda v_n1 , v_n2, v_n3  : expression
#          print(new_var)

# Characteristics :
# Can have any number of arguments
# Only one expression (no statements)
# Returns the result of the expression automatically
# Often used for short, throwaway functions


#  basic examples :
# lambda arguments: expression
# # Add two numbers
# add = lambda a, b: a + b
# print(add(3, 5))  # Output: 8

# # Square of a number
# square = lambda x: x * x
# print(square(4))  # Output: 16

# # Check even number
# is_even = lambda x: x % 2 == 0
# print(is_even(4))  # Output: True

# | Feature    | `def` function     | `lambda` function           |
# | ---------- | ------------------ | --------------------------- |
# | Syntax     | Uses `def` keyword | Uses `lambda` keyword       |
# | Name       | Usually named      | Anonymous (can be assigned) |
# | Return     | Must use `return`  | Returns automatically       |
# | Multi-line | Yes                | No (single expression)      |
# | Use Case   | Complex logic      | Short, simple functions     |

# questions
# n = eval(input('enter a number :'))
# even_odd = lambda n : n**2 if n % 2== 0 else n**3 
# print(even_odd(n))

# nested = lambda x: lambda y: x + y
# add_5 = nested(5)
# print(add_5(3))  # Output: 8

# l = [11,22,33,44,57]
# even_num = lambda num: [i**2 if i %2==0 else i**3 for i in num]
# print(even_num(l))


# people = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}]
# sorted_people = sorted(people, key=lambda x: x['age'])
# print(sorted_people)


# wap to retrun the keys of the dictionary 
# a={'hello':'sony','how':'are','you':'bye'}

# keys = lambda a : a.keys()
# print(keys(a))

# result = lambda di : [di[i] for i in di]
# print(result(a))



# 8. wap  which returns a list of squares of number in a list 
# l = [2,3,4,5,6]

# square = lambda a : [i**2 for i in a]
# print(square(l))


# 9. wap to extract list of elements are palindrome 

# l = ['nayana','kayak','mom','school','bag','dad']

# palindrome = lambda a : [i for i in a if i[::-1] == i ]
# print(palindrome(l))

# 10. WAP TO  print the numbers present in a list with their corresponding indices pair 

# l = [100,200,300,400,500]
# for i in enumerate(l):
#     print(i)

# indexnum = lambda a :[i for i in enumerate(a)]
# print(indexnum(l))


# indexnum = lambda a : enumerate(a)
# print(list(indexnum(l))) 


#  Lambda with map() class 
# 📌 1. What is map()?
# The map() function is a built-in Python function that allows you to apply a function to every item
# of an iterable (like a list, tuple, etc.) and returns a map object (which is an iterator).

# syntax :  map(function, iterable)
# function → The function to apply to each item
# iterable → The iterable whose items will be passed to the function one by one
# without using the lambda :

# def square(x):
#     return x * x

# nums = [1, 2, 3, 4]
# result = map(square, nums)

# print(list(result))  # [1, 4, 9, 16]

# with using the lambda:

# nums = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x**2, nums))
# print(squares)  # [1, 4, 9, 16, 25]


# Q : wap to create a list of 1st character fromm each name 

# name = ['manu','lohit','pratik','aishu','akahs','tejas']
# f_char = map(lambda x : x[0],name)
# print(f_char)  # <map object at 0x0000014F89E96350>

# print(list(f_char))  # ['m', 'l', 'p', 'a', 'a', 't']

# for i in f_char:
#     print(i,end=" ")

# a = [1, 2, 3]
# b = [4, 5, 6]

# result = map(lambda x, y: x + y, a, b)
# print(list(result))  # [5, 7, 9]
# ⚠️ If the iterables are of different lengths, map() stops at the shortest one.

# str_nums = ['1', '2', '3']
# int_nums = list(map(int, str_nums))
# print(int_nums)  # [1, 2, 3]

# names = ['alice', 'bob', 'carol']
# upper_names = list(map(str.upper, names))
# print(upper_names)  # ['ALICE', 'BOB', 'CAROL']



\















# Lambda with filter()

# nums = [1, 2, 3, 4, 5]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)  # [2, 4]












# Lambda with reduce()

# from functools import reduce

# nums = [1, 2, 3, 4]
# product = reduce(lambda x, y: x * y, nums)
# print(product)  # 24











# CLOSURES : You can return lambda from a function (closure)

# def multiplier(n):
#     return lambda x: x * n

# double = multiplier(2)
# print(double(5))  # Output: 10








# when we use map and filter it is mandatory to type cast otherwise we will  get output in object address...


# a= lambda a,b :a+b
# print(a(4,5))

# a = lambda :10+5
# print(a())


# s='good monring'
# y = lambda s:(s,len(s))
# print(y(s))


# w=lambda s: f'{s} number is even ' if s%2==0 else f'{s} number is odd'
# print(w(13))


# x=[1,2,3,4,5]
# q=lambda x :[i**2 for i in x]
# print(q(x))

# q = lambda x :(x**2,x**3)
# print(q(10))

# q = lambda x = int(input("enter a number :")) :(x**2,x**3)
# print(q(5))


# w= lambda s:f'{s} its a palindrome' if s==s[::-1] else f'{s} its not a palindrome'
# print(w("mom"))


# w=lambda x:abs(x)
# print(w(-100))


# a={"hello":"sony","How":"are","you":"bye"}
# w=lambda a:a.keys()
# print(w(a))


# seq = in which data type we can do indexing and slicing  (list , str, tuple)

# s="pratik"
# s=[1,2,3,4,5]
# s=(9,8,7,6,5)
# x  = lambda s:(s[0],s[-1])
# print(x(s))

# s='pratik'
# x = lambda x:len(x)
# print(x(s))


# wap to check if the lsit elements are palindrome or not

# l = ['nayana','kayak','mom','school','bag','dad']

# x= lambda l :[ i for i in l f'{i} is palindrome' if i==i[::-1] else f'{i} is not palindrome ' ]

# print([f"{i} is palindrome" if i == i[::-1] else f"{i} is not palindrome" for i in l])




# w=lambda i:type(i) if (type(i))in (str,list,tuple) else f'{i:type(i)}'


# w = lambda i: type(i) if type(i) in (str, list, tuple) else f'{i}: {type(i)}'
# print(w(20))



# x=[1,2,3,4,5,6,7]
# y=lambda i:i%2==0
# print(list(map(y,x)))

# print(list(filter(y,x)))


# u = ['mom','level','snap','chat','insta']
# y=lambda u: u ==u[::-1]
# print(list(map(y,u)))
# print(list(filter(y,u)))




# x=[1,2,3,4,5]
# y=[2,3,4,5,6]
# z=lambda x,y:x+y
# print(list(map(z,x,y)))


# name=['ravi','sachin','rahul','rohit']
# age = [34,43,52,39]

# z =lambda x,y:(x,y)
# print(list(map(z,name,age)))



# name=['ravi','sachin','rahul','rohit']
# a = lambda x:(x[0],x[-1])
# print(list(map(a,name)))


# x=[1,-90,45,65,-76,-78]
# a = lambda x: x>0
# print(list(filter(a,x)))


# r = 'good morning guys well come to python class in room number eight'
# a = lambda r: r[0] in 'aeiou'
# print(list(filter(a,r.split())))



# x=[20,25,35,89,100,121,33,17]
# a = lambda a:a%5==0
# print(list(map(a,x)))
# print(list(filter(a,x)))


# s = [1, True,'hii',[1,2,3],{34,56},3+4j]
# a = lambda a :isinstance(a,(int,float,bool,complex))
# print(list(map(a,s)))
# print(list(filter(a,s)))



#wap to create a list of 1st characters from each name
# names=["manu","lohit","jivago","wank","yaseen"]
# a = lambda a:a[0]
# print(list(map(a,names)))



#wap to return list of name and length pair
# names1=["laptop","mouse","board","house","week"]
# a = lambda x:{x:len(x)}
# print(list(map(a,names1)))
# print(list(filter(a,names1)))  # not working not applicable to update any change in original list


#wap to print sum of indices from both list
# l1=[2,3,4,5,6]
# l2=[3,4,5,8,9]
# a = lambda x,y :x+y
# print(list(map(a,l1,l2)))
# print(list(filter(a,l1,l2)))   # Error filter expected only 2 argument s got 3



#wap to make a pair of names and age
# names=["a","b","c","d",]
# age=[20,35,21,56,58]
# a = lambda x ,y : {x : y}
# print(list(map(a,names,age)))  #[{'a': 20}, {'b': 35}, {'c': 21}, {'d': 56}]


#wap to return if the key is individual returns its value else return its type
# d={10:"ten","hai":"value",(1,2,3):"colln",1.2:"decimal"}
# a = lambda a : a if type(a) in (int, float, bool , complex) else type(a)
# print(list(map(a,d)))


# 1.wap to return a list having only even valuesa
# l=[4,3,5,6,7,8,10]
# a = lambda a :a%2==0
# print(list(filter(a,l)))


# 2.wap to return a list having only flowers

# l=["sun flowers","banana tree","lily flowers","lotus flower","marigold flowers"]
# a = lambda a :  'flower' in a
# print(list(filter(a,l)))

# 3.wap to return a list having elements which are starting with consonants

# l=["hello","guys","please","respond","to","insta","computer"]
# a = lambda a : a[0] in 'aeiou'
# print(list(filter(a,l)))



# 4.waf to build a list with only even length strings using filter

# k=["apple","google","walmart","fb","insta","act","zomato"]
# a = lambda a : len(a)%2==0
# print(list(filter(a,k)))


# 5.waf to return only positive values in the list using filter

# m=[-5,-6,9,-34,90,-28,78,100,89,45,-65]
# a = lambda a : a>0
# print(list(filter(a,m)))


