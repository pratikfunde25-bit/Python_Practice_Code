#                                                   POLYMORPHISM
# POLY - MANY   MORHISM - FORMS                                          
# A single object will behave differently in different stages of lifecycle
# 2 typs of polymorphism
#  i) Run Time Polymorphism    --------- Method Overriding ()
# ii) Compile Time Polymorphism -------- Method Overloading ()

# 1. Definition
# Polymorphism = “Many Forms”
# In OOP, it allows the same function/method/operator to behave differently based on the object or data type.


# 2. Types of Polymorphism in Python

# a) Compile-Time Polymorphism ❌ (Not in Python)  (method overloading)
# In languages like Java/C++, achieved by method overloading.
# Python does not support traditional method overloading (last defined method overrides the earlier one).

# b) Run-Time Polymorphism ✅ (Used in Python)  (method overriding)
# Achieved by method overriding (same method in parent & child, but child version is called).

# 3. Ways Polymorphism is Achieved in Python

# (i) Polymorphism with Functions
# print(len("Pratik"))   # string → counts characters
# print(len([1, 2, 3]))  # list → counts items
# print(len{'a':10,'b':20}) # dict -> count key-value pairs
# 👉 Same function → works differently depending on object type.

# (ii) Polymorphism with Classes (Method Overriding)

# class Animal:
#     def sound(self):
#         print("Some generic sound") 

# class Dog(Animal):
#     def sound(self):
#         print("Bark!")

# obj = Dog()
# obj.sound()   # Bark! (child overrides parent)



# (iii) Polymorphism with Inheritance (Duck Typing)
# “If it looks like a duck and quacks like a duck, it’s a duck.”
# In Python, only the behavior (methods) matter, not the class type.

# class Dog:
#     def sound(self):
#         print("Bark!")

# class Cat:
#     def sound(self):
#         print("Meow!")
# class Duck:
#     def sound (self):
#         print('Quack ....')
# def Animal(x):
#     x.sound()

# l = [Dog(),Cat(),Duck()]

# for i in l:
#     # print(i.sound())  
#     Animal(i)

# for animal in (Dog(), Cat(),Duck()):
#     animal.sound()   # Bark! / Meow! (same method name, different behavior)



class Bird :
    def fly(self):
        print("am flying")
class Plane:
    def fly(self):
        print("am travelling")
class Human:
    def fly(self):
        print("am playing above ---->****") 
# def Check(q):
#     q.fly()

# for i in (Bird(),Plane(),Human()):
#     Check(i)                             # with calling it will act like the duck type 

# for i in (Bird(),Plane(),Human()):
#     i.fly()                              # without calling creating it will act like normal program not duck type

# x=Bird()
# Check(x)


# (iv) Operator Overloading
# Operators (+, *, >, etc.) work differently based on operands.

# print(5 + 10)          # integer addition
# print("Hello " + "AI") # string concatenation

# You can define custom behavior using dunder methods (Magic Methods):
# A method Starts and Ends with the doubel underscore __ function __ is called magic method
# class Book:
#     def __init__(self, pages): 
#         self.pages = pages
#     def __add__(self, other): 
#         # print(b1+b2)  #RecursionError: maximum recursion depth exceeded
#         return self.pages + other.pagesf
    
#     def __sub__(self,other):
#         return self.pages - other.pages
#     def __mul__(self,other):
#         return self.pages * other.pages
#     # def __div__(self,other):
#     #     return(self.pages / other.pages)
# b1 = Book(100)
# b2 = Book(200)
# # print(b1 + b2)   #  TypeError: unsupported operand type(s) for +: 'Book' and 'Book'
# print(b1-b2)   # 300 Correct Output
# print(b1+b2)
# print(b1*b2)
# # print(b1 / b2)  #   TypeError: unsupported operand type(s) for /: 'Book' and 'Book'



# class Student:
#     def __init__(self, name, marks, age):
#         self.name = name
#         self.marks = marks
#         self.age = age

#     # String representation
#     def __str__(self):
#         return f"Student(Name: {self.name}, Marks: {self.marks}, Age: {self.age})"

#     # Add marks of two students
#     def __add__(self, other):
#         return self.marks + other.marks

#     # Compare students by marks
#     def __gt__(self, other):
#         return self.marks > other.marks

#     # Equality check (by name + marks)
#     def __eq__(self, other):
#         return self.name == other.name and self.marks == other.marks

#     # Length (return name length just for fun 😅)
    
#     def __len__(self):
#         return len(self.name)


# # 🔹 Create objects
# s1 = Student("Pratik", 90, 21)
# s2 = Student("Ankit", 85, 22)
# s3 = Student("Pratik", 90, 21)

# # 🔹 Demonstrating magic methods
# print(s1)                # __str__
# print(s1 + s2)           # __add__ → 175
# print(s1 > s2)           # __gt__  → True
# print(s1 == s3)          # __eq__  → True
# print(len(s1))           # __len__ → 6 (length of "Pratik")





# class Student:
#     def __init__(self, name, marks, age):
#         self.name = name
#         self.marks = marks
#         self.age = age

#     # User-friendly
#     def __str__(self):
#         return f"Student(Name: {self.name}, Marks: {self.marks}, Age: {self.age})"

#     # Developer/debug-friendly
#     def __repr__(self):
#         return f"Student('{self.name}', {self.marks}, {self.age})"


# # Create object
# s1 = Student("Pratik", 90, 21)

# print(s1)         # Calls __str__ → nice readable output
# print(repr(s1))   # Calls __repr__ → shows constructor-like output

# # Example with list
# students = [s1, Student("Ankit", 85, 22)]
# print(students)   # List uses __repr__ for each element




 
# class Data:
#     def __init__(self,a,b):
#          self.a = a
#          self.b = b
#     def __add__(self,other):
#         print(self.a+other.a,self.b+other.b)
#         return Data(self.a +other.a,self.b + other.b)   # <__main__.Data object at 0x000002143EA34F50>
#         return self.a + other.a ,self.b + other.b       #(3,5)
#     def __str__(self):
#         return (f'{self.a} and {self.b}')
        
# t= Data(1,2)
# t1= Data(2,3)
# print(t+t1)

         
 
 
 
 
 
 
 
 
 
 
 
 
 
#  4. Key Concepts
# Overloading (same method, different parameters or different datatypes ): Not directly supported, but can be mimicked with *args / default args.
# Overriding (child class redefines parent’s method): Supported → true runtime polymorphism.
# Duck Typing: Focus on behavior, not object type.
# Operator Overloading: Customize operators for user-defined classes.

# 5. Advantages
# ✅ Increases code reusability
# ✅ Improves readability and flexibility
# ✅ Models real-world scenarios naturally (Dog & Cat both have sound())
# ✅ Promotes extensibility (add new classes without modifying existing code)

# 6. Quick Summary
# Polymorphism = “One name, many forms.”
# In Python, mainly via:
# Built-in functions (len, +)
# Method overriding (runtime)
# Duck typing (different classes, same method name)
# Operator overloading (__add__, __str__, etc.)
# Python doesn’t have true method overloading like Java.
