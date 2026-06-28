############################ FUNCTIONS ##################################


# Functions --> a set of statements / Block of code it will execute whenever we are calling the function name 
# Without calling function name it will wont execute it will give blank space output 
# WHY ---> To reduce the code reusability and redundancy 

#  Types of functions :
        # 1.Predefined Functions --> print(),input(),sum(),...etc
        # 2.User Defined Functions 
    
# Syntax :
# def function_name (Parameter):   #Function declaration 
# <--->   statement1
# <--->   statement2
# Function_name(arguments)      #Function Calling 


# def (keyword) func_name (any thing) parameter (var_name/s optional): (colon mandatory)
# <---> (indentation mandatory) statement(code block of code)   

# func_name(same name like declaration) (arguments) (var values)

# def palindrome(char):
#     if char.lower()==char.lower()[::-1]:
#         print('the given string is palindrome')
#     else:
#         print('the given string is not palindrome')
        
# palindrome('Mom')
# l=[11,12,13]
# def isodd(a):
#     for a in a:
#         if a%2==1:
#             print("the number is odd",a,end=" ")
#         else:
#             # print("the number is even ...")
#             ...

# isodd((101,102,103))  # if we miss argument type error raises (missing 1 req position argument)

# Without passing parameters

# def greet():
#     print("Hello")
    
# greet()    # output --> Hello 
# greet      # output -->          blank space 
# print(greet) # output  --><function greet at 0x0000019D3ADF1760>
# print(greet()) #output --> Hello next line - None  (output + None output)

# name="hello world"
# def subject(name):
#     print(name)
# subject('python')  #o/p ---> python 
# subject(name)      #o/p ---> hello world


def Total():
    amount=1000
    # print(amount)
    
Total()
# print(amount)  #NameError: name 'amount' is not defined


# ***********************  SCOPE  ******************************** 

# SCOPE  is nothing but a space where we are assigning / creating a variable   type1.local ,2.Global ,3.Nonlocal
# varible scope -->
# Local Variable 
# --> any variable it will present inside the function that type of variable we can call local var
# --> We cant access outside the function directly it will raise name error 
# --> If we want to access we have to use return keyword.


# Syntax :
# def function_name (Parameter):   #Function declaration 
# <--->   statement1
# <--->   statement2
#         return data1, data2...
# Function_name(arguments)      #Function Calling 


# def Total():
#     amount=1000
#     # print(amount)
#     return amount   # In function we can use only one return keyword 
# print(Total())



# Functions:
# 1.Positional Argument (limited argument) (only values to pass)
# 2.Variable Positional Argument (*args) (unlimited) -- return type (tuple)
# 3.Keyword Argument    (limited argument) (var_name = val)
# 4.Variable Keyword Argument (**kwargs) (unlimited) -- return type (dict)
# 5.Combination () 

# 2.GLOBAL variable 
# any variable it will present outside the function that type of variable we can call it global variable
# global variable we can access any where in the function or outside the function 




# a=100    # ----> Global Variable
# def spam():
#     b=200   # ---> Local Variable 
#     print(a)  #---> accessing global inside function   ---> o/p 100
#     print(b)  #---> accessing local inside function    ---> o/p 200
#     return b    #---> way to access local outside function using return keyword
# spam()
# print(a)    # ---> accessing global outside function   ---> o/p 100
# print(spam())
# print(b)    # ---> accessing local outside function    ---> o/p  NameError: name 'b' is not defined



# a=100
# def fun():
#     global a # modification done inside the function of global variable
#     a+=300   # without global --> UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
#     print(a)
# fun()
# print(a)


# x=10
# # print(x)  ---working
# def outer():
#     y = 20   #--->non local variable
#     # print(x) ---working
#     # print(y)  #--->working
#     # print(z)  --->NameError: name 'z' is not defined
    
#     def inner():
#         z=30
#         # print(x) ---working
#         print(y)  #--->working
#         # print(z)   ---working
        
#     inner()
    
#     # print(y) ---working  
        
# outer()  
# # print(x) ---working
# # print(y)  #---NameError: name 'y' is not defined
# # print(z)    ---NameError: name 'z' is not defined


# def demo(d,a=0,b=0,c=0):  # non default should be first then insert default parameters
#     print(d,a,b,c)
# demo(0)
# demo(1,1)
# demo(1,1,3)
# demo(1,1,1,1)



# 1. wap to perform addition and subtraction if a is greather than b return sum else return difference

# def operation(a,b):
#     if a>b:
#         return(a+b)
#     else:
#         return(a-b)
# print(operation(10,50))

# 2.wap to check string is palindrom or not take user input 
# string=input("enter the string :")
# def ispalindrome(string):
    
#     if string==string[::-1]:
#         print("the given string is palindrome")
#     else:
#         print("the given string is not palindrome")
        
# ispalindrome(string)

# 3.wap to return length of variable keywords argument 

# def lenth(**kwargs):
#     return len(kwargs)

# print(lenth(a=1,b=2,c=3))

# 4. wap to return length of variable positional argument

# def length(*args):
#     print(len(args))
# length(1,2,3)

# def length (*args):
#     return(len(args))
# print(length(1,2,3,4))

# def length(*args1):
#     count=0
#     while count <len(args1):
#         count+=1
#     return count
# print(length(1,2,3,4,5))

# count =0
# def lenght (*args):
#     global count
#     for i in args:
#         count+=1
#     print(count)
# lenght(1,2,3,4)


# 5.WAF to search for character in a given string and return corresponding index
string="coding part is done "
# def check(string,char):
#     return char,string.index(char)
#     return char,string.find(char)
# print(check(string,'e'))
    
            #OR
            
# def position(string,char):
#     for i in range(len(string)):
#         if string[i]==char:
#             print(string[i],i)
# position(string,'c')
    
    
# 6.wap to squaring of the element in the given list
# l=[1,2,3,4,5]
# def square(data):
#     for i in l:
#         print(i,'-->' ,i**2)
# square(l)

# def square1(data):
#     k=[]
#     for i in l:
#         k.append(i**2)
#     print(k)
# square1(l)


# 7.wap to fetch last digit number
# when we want to fetch last number --- num%10 last 2 digits num%100 like this...

# def last_digit(num):
#     print(f'the last digit of number is {num%10}')
# last_digit(125)
        
    
# 8.wap to read 3 numbers from the user,first two numbers should be added and the result of addition should be subtracted by third number 
 
# def operation (x,y,z):
#     a=x+y
#     print(z-a)   
# operation(10,20,50)

# 9.wap to find square,cube,square root and cube root of a number

# num=int(input("enter the number :"))
# def operations(num):
    
#     square = print(f'square :{num*num}')
#     cube = print(f'cube :{num**3}')
#     sqrt= print(f'square root : {num**0.5}')
#     cubert = print(f'cube root :{round(num**(1/3))}')
# operations(num)

# import math
# def Data(y):
#     return math.sqrt(y),math.cbrt(y)

# print(Data(64))

# 10.wap to check the given characters is alphabets or digit or special characters
# def Fun(s):
#     if s.isalpha():
#         print('its alphabet')
#     elif s.isdigit():
#         print('its digit')
#     else:
#         print('its special character')
# Fun('$#')

# 11.wap to check given iterable is a sequence,if it is a sequence reverse it,if not add one extra element to the iterable

# def Data(w):
#     if isinstance(w,(str,tuple,list)):
#         print(w[::-1])
#     elif isinstance(w,set):
#         a = int(input("enter the number to add in set :"))
#         (w.add(a))
#         print(w)
#     elif isinstance(w,dict):
#         a = input("enter the key and value in space")
#         a = a.split()
#         w[a[0]]=a[1]
#         print(w)
#     else:
#         print("INVALID INPUT")
# Data({100,200,65})


# 12.write a function to print the below output
# func("TRACXN",1)
# should print RCN
# 13.write a function to print the below output
# func("TRACXN",0)
# should print TAX


# s="TRACXN"
# def func(s,i):
#     if i==0:
#         print(s[::2])
#     if i==1:
#         print(s[1::2])
# func(s,1)

# 14.A function take variable number of positional arguments
#    as input. how to check if the arguments are more than 5.
# a=eval(input("enter data"))  # NO NEED
# def number_of_data(*args):
#     if len(args)>5:
#         print('the length of positional argument is more than 5')
#     else:
#         print('less tthan 5')
# number_of_data(10,20,235,51,575,88,89)

# 16.waf to return a dictionary with characters and ascii value pair

# s='ITs yours day'
# def char_asc(string):
#     d={}
#     for i in s:
#         # d.update({i:ord(i)})
#         d[i]=ord(i)
#     print(d)
# char_asc(s)

# 17.waf to reverse a iterable if you are passing string or list or tuple else print type of the data

# def check(data):
#     if isinstance(data,(str,tuple,list)):
#         print(list(reversed(data)))
#     else:
#         print(type(data))
# check({1,2,3,4,5,6})
        
# key='l'
# x=[10,20,30,40,50,60,40,50]
# x={1,2,3,5,6,7,6,9,10}
# x="hello"
# for i in x:
#     if i==key:
#         print(x.index(key))
# for i in range(len(x)):
#     if x[i]==key:
#         print(i ,end=" ")
#         break
        
# 21.Write a function that calculates the sum of digits of a given integer.
# number=12345
# Output=15

# def sum(number):
#     sum=0
#     while number>0:
#         last_digit=number%10
#         sum=sum +last_digit
#         number//=10
#     print(sum)
# sum(number)

# 22.Write a function to find the largest of three numbers.
# Input: 3, 7, 2
# Output: 7
# def largest(a,b,c):
#     if a>b and a>c:
#         print(a ,'is largest')
#     elif b>a and b>c:
#         print(b ,'is largest')
#     elif c>a and c>b:
#         print(c,'is largest')
        
# largest(3,7,2)


# 23.Create a function that counts the number of vowels in a string.
# x= "hello"
# # Output: 2
# def count_vowel(x):
#     count=0
#     for i in x:
#         if i in 'aeiouAEIOU':
#             count=count+1
#     print(count)
    
# count_vowel(x)


# def fact(number):
#     i=1
#     fact=1
#     while i<=number:
#         fact=fact*i
#         i+=1
#     print(fact)
# fact(5)

# 25.Write a function that counts the number of words in a given sentence.
# Input= "This is a sample sentence."
# # Output: 5
# def word_count(sentence):
#     count=0
#     for i in sentence.split():
#         count+=1
#     print(count)
# word_count(Input)

# 26. Write a function that removes duplicates from a given list.
# Input= [1, 2, 2, 3, 4, 4, 5]
# # Output: [1, 2, 3, 4, 5]
# def rem_duplicate(data):
#     s=set(Input)
#     print(Input)
#     print(list(s))
# rem_duplicate(Input)

# 27. Write a function that returns the middle element of a list.
# Input= [1, 2, 3, 4, 5]
# # Output: 3
# def middle(input):
#     mid=len(input)//2
#     print(input[mid])
# middle(Input)

# 28.waf to print index and element pair
# l = ["amazon", "flipkart", "ebay", "insta", "twitter", "meta"]
# def index_ele(data):
#     d={}
#     for i in enumerate(l):
#         d.update({i[0]:i[1]})
#     print(d)
# index_ele(l)


# 29.waf to create a dictionary Ascii and character pair
# l=[89,51,111,77,108,120]
# def char_asc(ord_data):
#     d={}
#     for i in l:
#         d[i]=chr(i)
#     print(d)
# char_asc(l)
    
    

# 30.waf to create a dictionary word and reverse word pair
# s="tomorrow is weekend and non-veg special"
# def rev_word(sentence):
#     d={}
#     for i in s.split():
#         d.update({i:i[::-1]})
#     print(d)
# rev_word(s)

        
    
    
#                   SEARCHING ALGORITHM

# 1.linear search algorithm (sequential search)
# It is a searching algorithm which works on a principle called sequential searching 
# where control will traverse through each and every value present in  a collection one after other sequentially to check whether key is present or not 


#           STEPS
# 1. Consider a list collection and a key to check 
# 2. Start comparing the values from 0'th index till len of a collection 
# 3. after getting the values same as key return its index
# 4. if key is not present then ignore or (return -1)

a=[0,1,2,2,1,3,4,5,6]
# by using for loop without range
# key=5
# def search(a,key):
#     for i in a:
#         if key==i:
#             return a.index(i)
# print(search(a,key))

# BY USING RANGE FUNCTION
# a=[0,1,2,2,1,3,4,5,6]
# key=2
# def search(collection , key):
#     for i in range(len(a)):
#         if a[i]==key:
#             print(i,end=" ")
# search(a,key)

# b=[7,11,9,8,7,70]
# key=7
# def search(b,key):
#     l=[]
#     for i in range(len(b)):
#         if b[i]==key:
#             l.append(i)
#     print(l)
# search(b,key)
            

# COUNT THE KEY IN THE COLLECTION


# a=[0,1,2,2,1,3,4,5,2,6]
# key=2
# def search(a,key,n):
#     b=0
#     count=0
#     for i in a:
#         if i==key:
#             count+=1
#             if count==n:
#                 print(b)
#         b+=1
#     else:
#         print(f"{n} th occurence is not found ...")
        
#     return 'count of the occurence of element -',count
# print(search(a,key,4))


# def search(a, key, n):
#     count = 0
#     for index, value in enumerate(a):
#         if value == key:
#             count += 1
#             if count == n:
#                 print(f"{n}th occurrence at index:", index)
#     return count
# print(search(a,2,3))

  
# def check ():
#     x=eval(input('enter the data :'))
#     key=eval(input('enter the key element:'))
#     count =0
#     for i in range(len(x)):
#         if key==x[i]:
#             count+=1
#             if count==3:
#                 return i
# w=check()
# print(w)  

#               Binary Search Algorithm

# steps
# 1.Consider a collection and a key to check
# 2.Initialise least index as a 0 and highest index as len(collections)-1
# 3.Check whether LI <= HI or not
# 4.Calculate mid index using mid=(LI+HI)//2
# 5.Check whether key==col[mid] if True return mid
#   elif check LI>col[mid] if true change li=mid+1
#   else check key<col[mid] if true change Hi=mid-1

# 6.Repeat all the points from 3 to 5 until you will get index of key


# x=[11,12,13,14,15,16,17]
# x=[1,2,3,3,4,5,5,6,7,7,7]
# key=7
# # key=150
# def Binary_search(x,key):
#     li=0
#     hi=len(x)-1
#     while li<=hi:
#         mid = (li+hi)//2
#         if key==x[mid]:
#             return f'key is present at index {mid}'
#         elif key>x[mid]:
#             li=mid+1
#         elif key<x[mid]:
#             hi=mid-1
#     return 'key is not present in the collection'
# print(Binary_search(x,key))


# y=[45,100,160,180,190]
# keys=[45,160,190]

# def check(y,keys):0  
#     li=0
#     hi=len(y)-1
#     while li<=hi:
#         mid=(li+hi)//2
#         if y[mid]==keys:
#             return mid
#         elif keys>y[mid]:
#             li=mid+1
#         else:
#             hi=mid-1
#     return -1
# # print(check(y,keys))  #TypeError: '>' not supported between instances of 'list' and 'int'

# for i in keys:
#     print(check(y,i))  # 0 2 4 
#     x=check(y,i)
#     if x != -1:
#         print(f'the number {i} is present at index {x}')
#     else:
#         print(f'the number {i} is not present in list')
    







    
    
    
    
    
        
def class1( **kwargs):
    print(*kwargs)
    
class1(a=1,b=2,c=3)
