#                                        DECORATOR
# import time
# def outer_most (x):
#     start =time.time()
#     def outer(func):
#         def inner():
#             time.sleep(x)
#             func()
#         return inner()
#     end=time.time()
#     a=end-start
#     print(a)
#     return outer

# @outer_most(3)
# def joy():
#     print("its joy day")
#     print(time.time())
# @outer_most(2)
# def func():
#     print("its fun day")
#     print(time.time())
# @outer_most(3)
# def func1():
#     print("its demo...")
#     print(time.time())
# joy
# func
# func1




# def my_decorator(func):
#     def wrapper():
#         print("Before the function....")
#         func()
#         print("After the function")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("Hello !")
# say_hello()


# def double_args(func):
#     def wrapper(a,b):
#         print("Doubling the arguments :")
#         return func(a*2,b*2)
#     return wrapper
# @double_args
# def add(x,y):
#     print(f'Results : {x+y}')

# add(1,3)
    
    
    

    
'''

def outer(spam):

    def inner(*args,**kwargs):

        print("Good morning")

        spam(*args,**kwargs)

    return inner

@outer



def spam():

    print("spam method")

@outer

def display():

    print("display method")



spam()

display()




def outer_most(Parameter):

    def outer(func):

        def inner(*args,**kwargs):

            statement

            func(*args,**kwargs)

        return inner

    return outer    



@outer_most(Parameter) 

 

def main_function(parameter):

    statement

main_function(Argument)    

 





def outer_most(x):

    def outer(func):

        def inner(*args,**kwargs):

            print(x)

            func(*args,**kwargs)

        return inner

    return outer

@outer_most("Mulitiplication operation")

def MUl(x,y):

    print(x*y)



@outer_most("Good morning")

def spam():

    print("spam method")



@outer_most("Good afternoon")

def display():

    print("display method")



spam()

display()

MUl(2,5)
'''

import time

def outer(func):

    def inner(x,y):

        start=time.time()

        print(f'main function name is {func.__name__}')

        print("waiting for the result")

        func(x,y)

        end=time.time()

        print(f'total time is ---->  {end-start}')

    return inner

@outer

def Sub(x,y):

    time.sleep(5)

    print(x-y)

Sub(10,5)

'''

































def outer(spam):

    def inner(*args,**kwargs):

        print("Good morning")

        spam(*args,**kwargs)

    return inner

@outer

def spam():

    print("spam method")

@outer

def display():

    print("display method")



spam()

display()

'''



"""



def outer_most(Parameter):

    def outer(func):

        def inner(*args,**kwargs):

            statement

            func(*args,**kwargs)

        return inner

    return outer    



@outer_most(Parameter) 

 

def main_function(parameter):

    statement

main_function(Argument)    

 

"""



def outer_most(x):

    def outer(func):

        def inner(*args,**kwargs):

            print(x)

            func(*args,**kwargs)

        return inner

    return outer

@outer_most("Mulitiplication operation")

def MUl(x,y):

    print(x*y)



@outer_most("Good morning")

def spam():

    print("spam method")



@outer_most("Good afternoon")

def display():

    print("display method")



spam()

display()

MUl(2,5)


    
###################### GENERATOR ############################

# WHAT IS A GENERATOR ?
# ---> A generattor in python is a special type of function (iterable) that allows you to create an iterator in a simple ,memory efficient way .
# Unlike regular functions that return a single value and terminate , generators use the yield statements to produce a series of values ,suspending and resuming execution as needed.
# This means they generate values on the fly and do not store all result in memory at once

# How Generator Works :
# A generator function is defined like a regular function but used yield insted of return .
# When called , it doesnt execute the whole function body but returns a generator object that can be iterated over.
# Each call to next() resumes the functions execution immediately after the last yield statement preserving the functions local state


# eg..
# def countdown(n):
#     while n>0:
#         yield n
#         n-=1
# print(countdown(3))  # its showing the object address
# gen = countdown(3)
# print(next(countdown(3)))  # it becomes same 3
# print(next(countdown(3)))  # it becomes same 3
# print(next(countdown(3)))  # it becomes same 3
# print(next(gen)) # condition satisfied 3>0
# print(next(gen)) # condition satisfied 2>0
# print(next(gen)) # condition satisfied 1>0
# print(next(gen))  # ERROR :   StopIteration


# Why Use Generators ?
# Memory Efficiency: it saves memory by yielding one result at a time ideal for handling large datasets or streams
# Convenience : Easier to write and read than manually implemented iterators (which req managing state and exceptions )
# Lazy Evaluation : values are generated as needed dalaying computation until results are requested.


# Difference in return and yield 

# return                                                        Yield
# we cant use multiple return keyword                           we can use multiple Yield  keyword
# used in any funciton                                          used in generator function
# exits function returns a value, ends execution                returns a value pauses execution , state saved , resumes when needed


# Generator Expression 
# squares = (x**2 for x in range(4))
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(squares)




# s= 'good afternoon'
# d={}
# def charord(s):
#     for i in s:
#         d.update({i:ord(i)})
#     print(d)
# charord(s)

# s= 'good afternoon'
# d={}
# def charord(s):
#     for i in s:
#         d.update({i:ord(i)})
#     yield(d)
# print(list(charord(s)))
# print(next(charord(s)))



# wap to generate a+b,a-b,a*b,a/b by taking a and b from user

a = int(input())
b = int(input())

    









# wap to generate only values which are divisible by 5

# l=[34,55,60,56,78,90,25,40]









##################################################### THREADING ###########################################
import threading
from threading import *
import time
# print("hello how are you ",threading.currentThread().getName())  # getname() or name()  # by default it  will come (Main Thread)

#               SINGLE THREADED PROGRAM


# num=[1,2,3,4,5]
# def double(num):
#     for i in num:
#         time.sleep(0.5)
#         print(i*2)
# def square(num):
#     for i in num:
#         time.sleep(0.5)
#         print(i**2)
# be = time.time()
# double(num)
# square(num)
# ae = time.time()
# print('total  time take by program is ',ae-be)

################## MULTITHREADING ###########################


# l=[1,2,3,4,5]
# def double(num):
#     for i in num:
#         time.sleep(0.5)
#         print(i*2)
#     print(Thread.is_alive(t1))   # TRUE yes its active

#     print(threading.current_thread().name)  # by default it will come Thread 1 (double) we changed to Thread one ---
# def square(num):
#     for i in num:
#         time.sleep(1.0)
#         print(i**2)
#     print(Thread.is_alive(t2))   # TRUE yes its active
#     print(threading.current_thread().name) # by default it will come Thread 2 (square) we changed to Thread two ---
# be = time.time()
# t1= Thread(target=double,args=(l,),name="Thread one  ---")
# t2 = Thread(target=square,args=(l,),name="Thread two ---")
# print('number of active thread is',active_count())

# t1.start()
# t2.start()
# print('number of active thread after start is',active_count())

# t1.join()
# print('number of active thread after first join is',active_count())

# t2.join()  
# print('number of active thread after join is',active_count())
 
# ae = time.time()
# print('total  time take by program is ',ae-be)
# print(Thread.is_alive(t1))   # False
# print(Thread.is_alive(t2))   # False
# print('number of active thread is',active_count())

# print(threading.current_thread().name)    # Main Thread
# print('number of active thread after program is',active_count())




# def wish (name):
#     for i in range(5):
#         # print('Good Morning')
#         time.sleep(2)
#         print(name)
# t1 = Thread(target=wish,args=('Pratik',))
# t2 = Thread(target=wish,args=('Aish',))
# t1.start()
# t2.start()




########################################   SYNCHRONIZATION      ##########################################


# only one thread at a time  -----> LOCK
# i) Lock  ---> we cannot use lock in the recursion functions ....
# ii) RLock  ---> overcomes the drawback of the lock 
# iii) Semaphore(no of threads) ---> if we want to run on multiple thread we can use semaphore ( also it will  work on single thread)

# We can create object of lock :-   l = Lock()
# To acquire the lock  ---> l.acquire()  ( it will lock the thread and after completion all exection of that thread )
# To release the lock ---> l.release()

# l = Lock()
# def wish (name):
#     l.acquire()
#     print('hi')
#     print(active_count())
#     for i in range(5):
#          # print('Good Morning')
#         time.sleep(1)
#     print(active_count())
#     l.release()
# t1 = Thread(target=wish,args=('Pratik',))
# t2 = Thread(target=wish,args=('Aish',))
# print(active_count())

# t1.start()
# t2.start()
# print(active_count())


# l = RLock()
# def factorial(num):
#     l.acquire()
#     if num==0:
#         res=1
#     else:
#         res=num*factorial(num-1)
#     l.release()
#     return res
# def display(n):
#     print(f'Factorial of {n} is :',factorial(n))
# t1=Thread(target=display,args=(5,))
# t2 = Thread(target=display,args=(7,))
# t1.start()
# t2.start()









# unpacking in the return keyword 
# both using yield and return keyword 