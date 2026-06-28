# 🔹 Multiple Inheritance in Python
# Definition:

# Multiple Inheritance is a feature in Python where a class can inherit from more than one parent class.

class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass

# 1. Syntax:
# class DerivedClass(Base1, Base2, ...):
    # class body
    
    
# 2. Method Resolution Order (MRO):

# it will be showing how the code executes order by order tracking of the code (classes and objects)

# Python uses C3 Linearization (C3 MRO) to determine the order in which classes are searched when calling methods.

# Use ClassName.__mro__ or ClassName.mro() to view the MRO.

# super() follows MRO to call the next method in line.

# print(Child.__mro__)  # return type will be tuple
# print(Child.mro())    # return type will be List


# 3. super() Function:

# Calls the next class’s method in MRO.

# Helps in cooperative multiple inheritance.

# Ensures that all parent classes get initialized if used properly.

# class A:
#     def __init__(self):
#         print("A init")
#         super().__init__()

# class B:
#     def __init__(self):
#         print("B init")
#         super().__init__()

# class C(A, B):
#     def __init__(self):
#         print("C init")
#         super().__init__()

# obj = C()
# print(C.mro())

# 4. Diamond Problem (program):

# Occurs when multiple classes inherit from a common base class, and a child inherits from all of them.

# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")
#         super().show()

# class C(A):
#     def show(self):
#         print("C")
#         super().show()


# class D(B, C):
#     pass

# d = D()
# d.show()
# print(D.mro())



# 5. Best Practices:

# Always use super() for constructors in cooperative inheritance.

# Avoid naming conflicts between parent classes.

# Keep class hierarchies simple and readable.

# Use MRO to understand the calling sequence of methods. 

# 6. Checking Class Relationships:

# Use issubclass() and isinstance() to check relationships.

# print(issubclass(D, A))  # True
# print(isinstance(d, B))  # True

# A: Base class

# B and C: Inherit from A

# D: Inherits from both B and C

# If both B and C inherit a member from A, and D uses that member, which path does it come from? That’s the ambiguity.


    #     A
    #    / \
    #   B   C
    #    \ /
    #     D
    
    
'''
#step1
class Father:
    def Money(self):
        print("father money")
class Mother:
    def care(self):
        print("Mother-care")

class Child(Father,Mother):
    def joy(self):
        print("enjoy the day")

x=Child()
# x.Money()
# x.care()
# x.joy()
print(Child.__mro__)





Through class_name
class Qspider:
    def sql(self):
        print("query_part from Qspider")

    def Manual(self):
        print("Testing from Qspider")
class Pyspider:
    def Python(self):
        print("Python from Pyspider")
    def sql(self):
        print("Sql from Pyspider")

class Student(Qspider,Pyspider):
    def Study(self):
        print("working")

    def sql(self):
        print("No---->query Part")
        Qspider.sql(x)  #Through class
        Pyspider.sql(x)

x=Student()
x.sql()
x.Manual()
x.Python()
x.Study()
'''

'''
Through super() function

class Qspider:
    def sql(self):
        print("query_part from Qspider")
        super().sql()
    def Manual(self):
        print("Testing from Qspider")
       
class Pyspider:
    def Python(self):
        print("Python from Pyspider")
    def sql(self):
        print("Sql from Pyspider")

class Student(Qspider,Pyspider):
    def Study(self):
        print("working")

    def sql(self):
        print("No---->query Part")
        super().sql()
x=Student()
x.sql()
x.Manual()
print(Student.__mro__)
'''


'''
Diamond--> program in wrong format
class A:
    def spam(self):
        print("class--->A")

class B(A):
    def demo(self):
        print("Class--->B")
class C(A):
    def display(self):
        print("Class--->C")

class D(A,C):
    def Joy(self):
        print("Class-->D")

d=D()  #TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, C
d.spam()
d.demo()
d.display()
d.Joy()

print()

print(D.__mro__)
'''



'''
#Diamond--> program in currect format
class A:
    def spam(self):
        print("class--->A")

class B(A):
    def demo(self):
        print("Class--->B")
class C(A):
    def display(self):
        print("Class--->C")

class D(B,C):
    def Joy(self):
        print("Class-->D")

d=D()
d.spam()
d.demo()
d.display()
d.Joy()
''' 











#                   HIRARCHICAL INHERITANCE

# multiple childerns will take the properties from single parent 

# 🔷 1. Definition

# Hierarchical Inheritance is a type of inheritance where multiple child classes inherit from the same parent class.

# All child classes share the parent’s attributes and methods, but can also override or extend them.

# class Parent:
#     def display(self):
#         print("Parent method")

# class Child1(Parent):
#     def show1(self):
#         print("Child1 method")

# class Child2(Parent):
#     def show2(self):
#         print("Child2 method")
        
# c1 = Child1()
# c2 = Child2()
  
  
# 3. Features

# Promotes code reuse — the shared logic remains in the parent.

# Allows child classes to have individual behavior while reusing parent features.

# Does not lead to the diamond problem (unlike multiple inheritance).

# Supports polymorphism and method overriding.

# 4. Constructor Behavior (__init__)

# If the parent has an __init__() and child doesn't define its own, it inherits the parent's constructor.

# class Parent:
#     def __init__(self):
#         print("Parent init")

# class Child(Parent):
#     pass
# class Child2(Parent):
#     pas

# c = Child()  # Output: Parent init
# c1= Child()  # Output: Parent init


# If the child defines its own __init__(), the parent’s constructor is not called automatically — you must call it explicitly using super().
class Parent:
    def __init__(self):
        print("Parent init")
class Child(Parent):
    def __init__(self):
        super().__init__()  # must call manually
        print("Child init")

c = Child()  # Output: Parent init  \n Child init

# 5. Method Overriding

# Child classes can override methods of the parent.
 

# 6. Accessing Parent Methods

# Use super() or directly call Parent.method(self).

# 7. isinstance() and issubclass()

# Used to check class relationships in hierarchical inheritance:
# isinstance(obj, Parent)     # True
# issubclass(Child1, Parent)  # True

# 8. Method Resolution Order (MRO)

# Python uses depth-first, left-to-right MRO in single and hierarchical inheritance.

# 10. When to Use Hierarchical Inheritance

# When multiple classes share a common behavior or structure.

# When you need clear class relationships and separation of roles.

# Common in GUI elements, banking systems, games, organization structures, etc.

# 11. Limitations

# If parent class changes, all child classes may be affected.

# Not suitable when child classes need to inherit from multiple unrelated parents — use multiple inheritance or composition in that case.

# 12. Best Practices

# Use super() when overriding __init__() or methods.

# Keep the parent class focused and minimal to avoid tight coupling.

# Avoid deep inheritance trees — use composition when needed.


