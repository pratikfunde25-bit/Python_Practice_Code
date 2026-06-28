#                   OOPS CONCEPT 
# TO REPRESENT REAL WORLD OBJECT TO THE SOFTWARE WORLD 
#  CLASS : blueprint / design  / module  / plan  for creating the object
# whenever we create class it dont take any memory 
# members of the class : method, object , constructor
#  object : physical existance of the class 
# object will always pointing to the method self class
# whenever we create object it does take any memory 
# [To map with real world scenarios , we started using objects in the code ]
# [All the class have a fuction called __init__() , which is always executed when the object is created or initialized ]


# class Student :
#     name = 'pratik'
#     def __init__(self):
#         print(self)   # <__main__.Student object at 0x00000139E0837230>
        
#     age = None
# s=Student()   # instance or object ----> pointing to the memory address
# print(s)      # <__main__.Student object at 0x00000139E0837230>
# print(s.name)
# print(s.age)
# print(Student().name)  # when we use parenthesis it will give output along with memory student obj address
# print(Student.age)  # it will give only output

# print(Student())   # <__main__.Student object at 0x00000139E0AC4E10>







#               METHODS
#  A FUNCTION INSIDE THE CLASS IS CALLED METHODS
# 1. INSTANCE METHOD    2. CLASS METHOD     3. STATIC METHOD 
#  1.a method it will accept first argument of an object address (instance method) by default it will take first parameter as Self 
#  instance is nothing but a object for the class 
# 2.class method -> any method decorate with @ class method decorate ()  by default it will take first parameter as cls 











# class Test:
#     def spam(self):
#         print('Test Class')  
# t=Test
# print(t)  #<class '__main__.Test'>
# t= Test()  # object created for class Test
# print(t)   #  <__main__.Test object at 0x00000259E3AE7230>

# accessing the data by using object and class 
# t.spam   # no output 
# t.spam()    # Test Class
# Test.spam  # no output
# Test.spam()   # TypeError: Test.spam() missing 1 required positional argument: 'self'
# Test.spam(Test)  #Test Class
# Test.spam(t)  #Test Class



# class Car:
#     def BMW(self):
#         print('my car name is BMW --->')
# c=Car()   #  <__main__.Car object at 0x0000023A45E47380>
# print(c)
# c.BMW()  


# class Information:
#     a=10
#     def Employee(self,name,sal,empid):
#         name='abc'
#         sal=111
#         print(f'my name is {name} and my sal is {sal} my emp id is {empid}')
        

# x = Information()
# # x.Employee('pratik',11)  # my name is <__main__.Information object at 0x00000276F1507380> and my sal is pratik my emp id is 11
# x.Employee('pratik',120,11)

# Information.Employee(x,'pratik',120,11)
# Information.Employee(Information,'pratik',120,12)



#                   CLASS METHOD 
# cls and self both are the special parameters 
# if you want to create alternative way for creating constructors ...


class Fun :
    @classmethod
    def spam(cls):
        print("spam method")
        print(cls)
# f=Fun
# print(f)  # <class '__main__.Fun'>
# f = Fun()
# print(f)  #  <__main__.Fun object at 0x000001FB1A897230>
# f.spam()  # spam method
# Fun.spam()  # spam method
# Fun.spam(f)  # TypeError: Fun.spam() takes 1 positional argument but 2 were given





# class Animal :
#     @classmethod
#     def cat(cls):
#         print("cat class")
#     @classmethod
#     def lion(cls):
#         print('lion class')
#     def tiger(self):
#         print('tiger class')

# a=Animal()
# a.cat()
# a.lion()
# a.tiger()


# Animal.cat()
# Animal.lion()
# # Animal.tiger(Animal)
# Animal.tiger(a)




# class Flipkart :
    
#     @classmethod
#     def Product(cls, total_product , price):
#         print(f'Total product count is {total_product} and product price is {price}')
    
    
#     @classmethod
#     def Product_information(cls,color,loc):
#         print(f'My product color is {color} and product current location is {loc}')

    
#     def order_details(self, current_loc , name , mob):
#         print(f'current location is {current_loc} and name is {name} and mobile number is {mob}')
        

# f = Flipkart()

# f.order_details('pune','iphone',9882653515)
# f.Product(9,85000)
# f.Product_information('red','Mumbai')


# Flipkart.order_details(Flipkart,'pune','iphone',9882653515)
# Flipkart.Product(9,85000)
# Flipkart.Product_information('red','Mumbai')





# class ShowRoom :
#     @classmethod
#     def car_information(cls):
#         car_price= 11
#         car_color = 'Blue'
#         car_model = 2025
#         print(f'my car total price is {car_price} and car color is {car_color} and model year is {car_model}')
        
# s = ShowRoom()
# s.car_information()
# ShowRoom.car_information('dsfljkdaf')   # still it will be working ( without using @classmethod only)
# ShowRoom.car_information(+54354325435)  # # still it will be working ( without using @classmethod only)

# ShowRoom.car_information()



#               STATIC METHOD
#  When we do any modification it will wont affected 
# dont take any parameters like cls and self 
# third type of method 






#                              ------ CONSTRUCTOR --------

# CONSTRUCTOR IS A SPECIAL MEMBER IN THE CLASS
# IN PYTHON CONSTRUCTOR WE ARE DEFINED AS A ( __init__())
# whenver we create a constructor in the class and created the object it will be automatically executed we dont need to call the method 
# whenver we create multiple constructor always it will execute the latest one (updated one)


# class Hii:
#     def __init__(self,a,b):             #construcotor 
#         self.a=a
#         self.b=b
#         print('constructor method')
#     def spam(self):                 # instance method 
#         print('spam method')

# # Hii.spam(Hii)
# h=Hii(10,20)  # automatically constructor method is executed without calling 
# Hii.__init__(h,10,20)  # we need to pass explicitly object then constructor will be executed 
# # h.spam()



# class abc:
#     def __init__(self):
#         name  = 'abc'
#         age = 15
#         print('hello')
#         print(self)
# a= abc()




# in CONSTRUCTOR  we have 2 types : 1) Default Constructor (predefined Constructor)  2) User Defined Construcotr 

# 1) Default Constructor
# all the [instacne method] we can call it as best examples of Default constructor 
# internal it will be present we cant see inside 

# 2) User Defined Constructor 
# we are the user we only the defined the constructor 
#  here also we have 2 types of user defined constructors  :   1) Without parameterized constructor 2) with parameterized constructor 

# 1) without parameterized
# in this type when we create the multiple objects we cant do any modification for every object different output is impossible 
# # here in this type while creating the object we need to pass the arguments in the parentheses 


# class Bank:
#     def __init__(self):
#         Acc_holder_name = "Ram"
#         Acc_number =24348384
#         Acc_balance = 50000
#         Bank_name = "SBI"
#         IFSC_code = "SBIN00779"
#         print(f'account holder name is {Acc_holder_name} account number is {Acc_number} bank balance {Acc_balance} my bank name is {Bank_name} and ifsc code is {IFSC_code}')
        
# b = Bank()
# b1 = Bank
# b2 = Bank()
# print(b1) #<class '__main__.Bank'>
# print(b1())  # <__main__.Bank object at 0x000001ED74F04E10>
# print(b)     # <__main__.Bank object at 0x000001ADB4BC7230>




# 2) With Parameterized

# in this type when we create the multiple objects we can do any modification for every object different output is easily possible 
# here in this type while creating the object we need to pass the arguments in the parentheses 

# class Bank:
#     def __init__(self, Acc_holder_name,Acc_number,Acc_balance,Bank_name,IFSC_code=0):
#         print(f'account holder name is {Acc_holder_name} account number is {Acc_number} bank balance {Acc_balance} my bank name is {Bank_name} and ifsc code is {IFSC_code}')
        
# b = Bank('pratik',48737483,50000,'SBI',"SBIN09889")
# b1 = Bank('pratik',48737483,50000,'SBI')
# b2 = Bank()
# print(b1) #<class '__main__.Bank'>
# print(b1())  # <__main__.Bank object at 0x000001ED74F04E10>
# print(b)     #  output along with <__main__.Bank object at 0x000001ADB4BC7230>



#                               INSTANCE VARIABLE 
# the variable only working with constructor (restricted) inside the constructor
# if we done any modification through classs it will wont affectd but by using object modification is done it will be affected
# syntax :         self.new_var = value


# Instance variables are tied to the object and can be accessed using the object (either with self. inside methods or object_name. outside methods).
# Local variables are temporary within a method and cannot be accessed using the object. They cease to exist after the method completes. 



# class Bank:
#     def __init__(self):
#         self.Acc_holder_name = "Ram"
#         Acc_number =24348384
#         Acc_balance = 50000
#         Bank_name = "SBI"
#         IFSC_code = "SBIN00779"
#         print(f'account holder name is {self.Acc_holder_name} account number is {Acc_number} bank balance {Acc_balance} my bank name is {Bank_name} and ifsc code is {IFSC_code}')
        
#     def Account_details (self):
#         print(f'account holder name is {self.Acc_holder_name}' ) # account number is {Acc_number} bank balance {Acc_balance} my bank name is {Bank_name} and ifsc code is {IFSC_code}')

# b = Bank()
# b.Account_details()




# class ATM :
#     def __init__(self,bal):
#         self.a = bal
#         self.bal = bal
        
#     def deposit(self,amount):
#         # bal += amount   # UnboundLocalError: cannot access local variable 'bal' where it is not associated with a value
#         self.bal_updated= z.a
#         self.a += amount
    
       
#         print(f'balance was {self.bal_updated} Total amount after deposit is {self.a}')
# z = ATM(1000)
# print(z.bal)
# print(z.a)
# z.deposit(2000)
# print(z.bal)
# print(z.a)


# ATM.deposit(z,5000)    # balance was 3000 Total amount after deposit is 8000
# ATM.deposit(z,2000)    # balance was 8000 Total amount after deposit is 10000
# ATM.deposit(ATM,5000)  # AttributeError: type object 'ATM' has no attribute 'a'




# class Information:
#     def student(self,name,age):
#         print(name,age)
#     def student(self,name):
#         print(name)
#     def student(self , age,name):
#         self.age = age
#         print(self.age,name)
        


# i = Information()
# i.student(56,'pratik')


#                                                   method overloading

 
# developing the multiple method with same name and variations with parameters (arguments) and variation in the data types (int, float , ...)
# in python we cant achieve the method overloading due to python is a dynamic typed language (we can achieve in java)
# we can achieve partially not 100 %  just we can give clarification how the code will flow 


# class Data :
#     def __init__(self,a,b,c):   # simple constructor 
#         print(a,b,c)
# d = Data(1,2,3)
        
        
# class Data :
#     def __init__(self,a=0,b=2,c=10):   # default  constructor with parameters 
#         print(a,b,c)
# d = Data(1,2,3)   # 1 2 3
# d= Data(1,32)     # 1 32 10
# d= Data(b=25)     # 0 25 10


# class Data :
#     def __init__(self,a=0,b=2,c=10,*args):   # default  constructor with parameters 
#         print(a,b,c,*args) # we use * for unpacking 
# d = Data(1,2,3)   # 1 2 3
# d= Data(1,32)     # 1 32 10
# d= Data(b=25)     # 0 25 10
# d=Data(48,66,7,8,9,9,7,67)

# in instance method i want to access data outside the method without sing the object 

# class abc:
#     def info(self,a,b):
#         self.a=a
#         self.b=b
#         print(a,b)
#         print(self.a,self.b)

# abc.info(abc,10,20)


# in construcotr i want to acces data outside the without using the oject

# class Test:
#     def __init__(self):
#         print("hello ")

# Test.__init__(Test)



 


# class Bank :
#     bank_name  = 'BOI'
#     def __init__(self,bal):
#         self.bal = bal
    
#     def deposit(self, amount):
#         print(f'you deposited {amount} and now your current balance is {amount+self.bal} and bank name is {Bank.bank_name}')
        

# b= Bank(1000)
# b.deposit(2000)




        











    





 







































# class Parent :
#     def villa(self ):
#         print("dad's gift")
# class Child(Parent):
#     def party (self):
#         print("no amount")
        
# x = Child()
# x.villa()
# x.party()
# # print(dir(x))




# class Dad:
#     def __init__(self,name):
#         self.name = name 
        
#     def my_method(self):
#         print("Parent class mehtod ...")
#         print(f'my name is {self.name}' )
        
        
# class child(Dad):
#     def __init__(self):
#         super().__init__(name="pratik")
        
        
      
#     def child_method(self):
#         print("child class method ...")
#         self.my_method()
        
        
# c = child()
# # c= Dad()
# c.child_method()
# # c.my_method()



# class Dad:
#     def __init__(self,name):
#         self.name = name 
        
#     def my_method(self):
#         print("Parent class mehtod ...")
#         print(f'my name is {self.name}' )
        
        
# class child(Dad):
#     def __init__(self,age):
#         super().__init__(name="pratik") if we want to access parent data into child and to avoid method overriding 
#         self.age=age
#         print(f"my age is {self.age}")
        
      
#     def child_method(self):
#         print("child class method ...")
#         self.my_method()
        
        
# c = child(23)
# # c= Dad()
# c.child_method()


# class Grandfather():
#     def villa(self):
#         print("villaee")
# class father(Grandfather):
#     def Bmw(self):
#         print("bmw car ")
# class child(father):
#     def tvs(self):
#         print("tvs bike")
#         self.Bmw()
        
        
# c = child()
# c.tvs()
# c.Bmw()
# c.villa()




# class Dad :
#     def demo(self):
#         print("33")
# class Mom :
#     def demo(self):
#         print("45")
# class Child(Dad,Mom):
#     print("Child Class")

# x=Child()
# x.demo()
# print(Child.__mro__)

#(MRO)- method resolution order always Left to Right ----> how can we achieve multiple inheritence in python 
# cannot create a consistent MRO for bases A,B (classes in multiple inheritence)


# class Dad:
#     def amount(self):
#         print("2 lakh")
    
# class Child1(Dad):
#     def party1(self):
#         print("50 rs")
# class Child2(Dad):
#     def party2(self):
#         print("50K rs")
# x= Child1()
# y= Child2()
# x.party1()
# x.amount()
# y.party2()
# y.amount()



# class Dad:
#     def amount(self):
#         print("2 lakh")
    
# class Child1(Dad):
#     def __init__(self):
#         super().__init__()
#         print("50 rs")
#         # super().__init__()
# class Child2(Dad):
#     def __init__(self):
#         print("50K rs")
#         super().amount() 
             
# x= Child1()
# y= Child2()
# x.__init__()
# y.__init__()

# print(Child1.mro())



#hybrid
# single level inheritence
# class Person:
#     def show_person(self):
#         print("i am a person ")
        
# class Student(Person):
#     def show_student(self):
#         print("i am a student ")
    
    
#Hierarchical Inheritence
    
# class Person:
#     def show_person(self):
#         print("i am a person ")
        
# class Student(Person):
#     def show_student(self):
#         print("i am a student ")
        
# class Teacher(Person):
#     def show_Teacher(self):
#         print("i am a teacher")



#COMPLETE FINAL HYBRID form INHERITENCE


# class Person:                           # Simple Parent Class Created
#     def show_person(self):
#         print("i am a person ")
        
# class Student(Person):                  # Single Level Inheritence
#     def show_student(self):
#         print("i am a student ")
        
# class Teacher(Person):                  # Hierarchical Inheritence
#     def show_Teacher(self):
#         print("i am a teacher")

# class UgStudent(Student):               # Multi Level Inheritence
#     def show_ug_student(self):
#         print("i am a UG student")
        
# class Staff(Teacher):                   # Multi Level Inheritence
#     def show_staff(self):
#         print("i am a Staff")

# class Project(UgStudent,Staff):         # Multiple Inheritence
#     def show_project(self):
#         print("i am working in a Project")
        
# x= Project()
# x.show_project()
# x.show_student()
# x.show_staff()
# x.show_ug_student()
# x.show_staff()
# x.show_Teacher()
# x.show_person()






# CONSTRUCTOR CHAINING AND METHOD CHAINING ---> USING SUPER CLASS TO GET ATTRIBUTES FROM ANOTHER CLASS

# INSTANCE VARIABLE CAN BE AFFECTED THROUGH OBJECT NOT AFFECTED BY CLASS syntax ---> SELF.VAR_NAME = VALUE

#IS A RELATIONSHIP VS HAS A RELATIONSHIP 

#IS --->  ACQUIRING THE PROPERTIES FROM ONE CLASS INTO ANOTHER WITH USING INHERIENCE
#HAS ---> ACQUIRING THE PROPERTIES FROM ONE CLASS INTO ANOTHER WITHOUT USING INHERITENCE CALLED COMPOSITION 
# METHOD OVERLOADING IN PYTHONWE CAN ACHIVE THROUGH DEFAULT PARAMETERS NOT 100% ITS PARTIALLY 
# AND METHOD OVERRIDING 

# HAS A RELATIONSHIP ------->
# class Test :
#     sub = "python"
#     def __init__(self):
#         self.name= 100
#         self.loc = "pune"
# class Test2:
#     def demo(self):
#         print("its demo method")
#     def __init__(self):
#         print("init method called")
#         t=Test()
#         t.__init__()
#         print(t.sub)
#         print(t.name)
#         print(t.loc)
        
# t2=Test2()
# # t2.__init_
# t2.demo()






#                           Composition in Python (HAS-A Relationship)


# 1. Definition

# Composition is an object-oriented programming (OOP) concept.

# It represents a HAS-A relationship between classes.

# One class contains objects of another class as its attributes (data members).

# 👉 Example:

# A Car HAS-A Engine.

# A University HAS-A Department.


# 2. Difference Between Inheritance & Composition


# | Aspect       | Inheritance (IS-A)                    | Composition (HAS-A)                    |
# | ------------ | ------------------------------------- | -------------------------------------- |
# | Relationship | IS-A (child is a type of parent)      | HAS-A (object contains another object) |
# | Coupling     | Strongly coupled                      | Loosely coupled                        |
# | Reusability  | Code reused by extending parent class | Code reused by containing objects      |
# | Flexibility  | Less flexible, tightly bound          | More flexible, can swap objects easily |


# 3. When to Use Composition

# You want a part-whole relationship.
# One class cannot exist without the other.
# You want loose coupling and easy maintenance.

# Prefer composition over inheritance if:
# The relationship is not naturally "IS-A".
# You just need functionality, not a full hierarchy.

# eg.
# class Engine:
#     def start(self):
#         print("Engine starting...")
# class Car:
#     def __init__(self):
#         self.engine = Engine()   # Composition (HAS-A)

#     def drive(self):
#         self.engine.start()     # calling the method
#         print("Car is driving...")

# # Usage
# car = Car()
# car.drive()



# 5. Key Concepts in Composition

# Containment
# One class creates an object of another inside it.
# Example: Car contains Engine.

# Delegation
# One class delegates work to another.
# Example: Car asks Engine to start.

# Lifetime Dependency
# If the container object is destroyed, the contained object may also be destroyed.
# Example: If a Car is sold, its Engine goes with it.



# 6. Types of Composition

# Simple Composition – One object contains another.
# Example: Car HAS-A Engine.

# Aggregation (Weak Composition) – Objects can exist independently.
# Example: Team HAS-A Player (a Player can exist without Team).

# Strict Composition (Strong Composition) – Objects’ lifetimes are dependent.
# Example: Human HAS-A Heart (Heart cannot exist without Human).

# 7. Aggregation vs Composition

# | Feature    | Aggregation                            | Composition                          |
# | ---------- | -------------------------------------- | ------------------------------------ |
# | Dependency | Independent objects                    | Dependent objects                    |
# | Lifetime   | Contained object can outlive container | Contained object dies with container |
# | Example    | Library HAS-A Student                  | Human HAS-A Heart                    |


# class Player:
#     def __init__(self, name):
#         self.name = name

# class Team:
#     def __init__(self, team_name, players):
#         self.team_name = team_name
#         self.players = players  # Aggregation

#     def show_players(self):
#         print(f"Team {self.team_name} players:")
#         for p in self.players:
#             print(p.name)

# # Usage
# p1 = Player("Rohit")
# p2 = Player("Virat")
# team = Team("India", [p1, p2])
# team.show_players()


# 9. Benefits of Composition
# ✅ Promotes code reusability without tight coupling.
# ✅ More flexible than inheritance.
# ✅ Can easily replace/change components.
# ✅ Helps in modeling real-world relationships better.

# 10. Drawbacks of Composition
# ❌ Requires more boilerplate code (need to explicitly create contained objects).
# ❌ Not always suitable when there is a clear IS-A relationship.


# Top Composition in Python Questions
# 🟢 Basic Understanding

# Define composition in Python. How is it different from inheritance?

# What do we mean by "HAS-A" relationship in OOP? Give two real-life examples.

# Explain with an example the difference between aggregation and composition.

# When should you prefer composition over inheritance?

# Can a class have both IS-A (inheritance) and HAS-A (composition) relationships at the same time? Give an example.

# 🟡 Code-Oriented Questions

# Write a Python program to model:

# Car HAS-A Engine (composition)

# Show that when Car object is destroyed, Engine object also goes away.

# Implement Team HAS-A Players using aggregation (players exist even if team is deleted).

# Can you replace one component inside a class in composition? (Example: Replace Car’s Engine with ElectricEngine at runtime.)

# Write a Python program where University HAS-A Department HAS-A Professor (multi-level composition).

# Show composition by making a Person HAS-A Address.

# Address should have city and pincode.

# Print Person details with Address.

# 🔴 Tricky & Advanced Questions

# What happens if you create the same contained object for two container objects?

# Example: Same Engine assigned to two different Cars. Is this still composition or aggregation?

# How can you prove that composition creates strong dependency of object lifetime?

# Example: Delete Car → Engine also deleted.

# Delete Team → Players still exist.

# In Python, how would you implement composition if you want to swap an object at runtime?

# Example: Car initially has PetrolEngine. Later, replace it with ElectricEngine.

# Can composition be achieved without explicitly creating objects inside __init__?

# (Yes, by passing objects as arguments → aggregation). Write code for this.

# Is it possible to simulate inheritance behavior using composition? How?

# (Hint: delegation of method calls).

# 🟣 Scenario-Based Trick Questions

# Suppose you’re designing a Human class with a Heart object.

# Is this aggregation or composition? Why?

# What if you transplant the heart into another human? 🤔

# In a Library system:

# Library HAS-A Book (composition or aggregation?)

# Library HAS-A Librarian (composition or aggregation?)
# Explain with reasons.

# If you design a Laptop class with a Battery object:

# When should it be aggregation?

# When should it be composition?

# Can you implement multiple composition relationships inside a class?

# Example: A Car has Engine, Wheels, and MusicSystem. Show with Python code.

# Why do many experts say "Favor composition over inheritance"? Explain with an example in Python.

# ⚡ Bonus "Catch-you" Interview Tricky Ones

# If a class contains a list of objects of another class, is that composition or aggregation? (Depends on lifetime dependency).

# How do __del__ methods in Python affect object lifetime in composition?

# Can you make composition immutable (i.e., once set, the contained object cannot be replaced)?

# What’s the difference in UML notation for inheritance, aggregation, and composition?

# Write code where a class delegates method calls to another class (composition used for delegation).






 