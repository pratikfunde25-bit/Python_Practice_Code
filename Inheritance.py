#                                  INHERITANCE  ( Is A Relationship )
# Acquiring the properties or characteristics from one class to another class
# from parent class to child class


# Types of Inheritance 

# 1. Single Level Inheritance
# 2. Multi Level Inheritance
# 3. Multiple Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance 
# 6 .Cyclic Inheritance # ( not supported in python )





# 1. Single Level Inheritance
# def : Child Class will take the properties from its parent class 
# here only 2 classes will be present 
# 1. Parent Class ( Base Class , Super Class)
# 2. Child Class ( Derived Class, Subclass)
# print(dir(x)) -- whatever the things present inside the class it will show 



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


# Super()  function
# it is used to :
# 1) avoid the method overriding in python 
# 2) access the data from parent class to child class

# syntax 
# super().method_name_parent ( we can use both positional ,keywords arguments , or directly pass the  values while calling )




#   2 class class 1 const

# class A:
#     def __init__(self,name,age):
#         print('hello')
#         self.age = age
#         self.name = name
#     def info(self):
#         print(f'my name is {self.name} and my age is {self.age}')
 
 
# class B(A):
#     def __init__(self,id,price,name,age):
#         self.id = id
#         self.price = price
#         super().__init__(name,age)
#     def demo(self):
#         print(f'my id is {self.id} and my mobile price is {self.price}')
#         print(A)
        
# b = B(101,50000,'pratik',21)
# b.info()
# b.demo()





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







# 2)  MULTI LEVEL INHERITANCE 

# child class will take the properties from its father inturn father will take the properties from its father 
# here multiple classes can be present 


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




#multilevel-inheritance---> step1

# class Grandpa:
#     def Tvs(self):
#         print("TvS--->1")
# class Father(Grandpa):
#     def Land(self):
#         print("Agrii-->land")
# class Child(Father):
#     def Phone(self):
#         print("Iphone--->17")

# c=Child()
# c.Tvs()
# c.Land()
# c.Phone()




#in multilevel-inheritance to avoid method overiding ---> step2

# class Grandpa:
#     def Tvs(self):
#         print("TvS--->1")
# class Father(Grandpa):
#     def Land(self):
#         print("Agrii-->land")
#     def Tvs(self):
#         super().Tvs()
#         print("TVS--->2")
# class Child(Father):
#     def Phone(self):
#         print("Iphone--->17")

#     def Land(self):
#         super().Land()
#         print("40-->*")

# c=Child()
# c.Tvs()
# c.Land()
# c.Phone()




#in multilevel-inheritance to avoid method overiding along with
#  useing parameters---> step3


# class Grandpa:
#     def Tvs(self,TVS_price):
#         print(f'TVs_total price is {TVS_price}')
# class Father(Grandpa):
#     def Land(self,total_land):
#         print(f'total land is {total_land}')

#     def Tvs(self,TVS_model):
#         super().Tvs(TVS_price=1000)
#         print(f'Tve_model is ---> {TVS_model}')
# class Child(Father):
#     def Phone(self):
#         print("Iphone--->17")

#     def Land(self,land_loc):
#         super().Land(total_land=100)
#         print(f'land current location is {land_loc}')

# c=Child()
# c.Tvs(2025)
# c.Phone()
# c.Land("pune")




# class GreatGrandpa:
#     def Tvs(self,Tvs_date):
#         self.a=10
#         print(f'Tvs buying date is {Tvs_date}')

# class Grandpa(GreatGrandpa):
#     def Tvs(self,TVS_price):
#         print(f'TVs_total price is {TVS_price} {self.a}')
# class Father(Grandpa):
#     def Land(self,total_land):
#         print(f'total land is {total_land}')

#     def Tvs(self,TVS_model):
#         super(Grandpa,c).Tvs('01-jan-2005')
        
#         super().Tvs(TVS_price=1000)
#         print(f'Tve_model is ---> {TVS_model}')
# class Child(Father):
#     def Phone(self):
#         print("Iphone--->17")

#     def Land(self,land_loc):
#         super().Land(total_land=100)
#         print(f'land current location is {land_loc}')

# c=Child()
# c.Tvs(2025)
# c.Phone()
# c.Land("pune")
# print(c.a)




#                       MULTIPLE INHERITANCE

# a single child class will take the properties from multiple parents 
# eg . Child Class will take the properties from Mom and Dad Class

# syntax:
#     class A:
#         pass
#     class B:
#         pass
#     class C(A,B):
#         pass





















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