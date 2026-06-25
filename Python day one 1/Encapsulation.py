###                                 ENCAPSULATION

#WRAPING OR BINDING OF THE DATA AND METHODS IN A SINGLE UNIT (we cant achieve 100%)
#access specifiers : 1)Public 2)Protected 3)Private 
# p=10
# _p=10
# __p=10
# # print(id(_p),id(__p),id(p))   #140714266281160 same id address for all the access specifiers

# class Student:
#     def __init__(self,name,marks,location):
#         self.name = name
#         self._marks=marks
#         self.__loc = location
#         print(f'my name is {name} , marks : {marks},location :{location}')
#     def getter(self):
#         return self.name,self._marks,self.__loc  
    
#     def setter(self,name,marks,location):
#         self.name=name
#         self._marks=marks
#         self.__loc=location
#     def deleter(self):
#         del self.name 
#         del self._marks
#         del self.__loc
        
        
# s=Student("pratik",90,'pune')
# print(s.name)
# print(s._marks)
# print(s._Student__loc)
# print(Student._Student__loc)
# print(s.getter())
# print(s.setter('aish','95','abc'))
# print(s.getter())
# print(s._Student__loc)
# s.deleter()
# # print(s.name)

 



#                             *********** ENCAPSULATION ********

# 🔹 1. What is Encapsulation?
# Encapsulation is one of the 4 main pillars of Object-Oriented Programming (OOP) (others are Inheritance, Polymorphism, and Abstraction).
# It means binding (combining) data and the methods that operate on that data into a single unit (a class).
# It also helps restrict access to some parts of the data to protect it from accidental changes.

# 🔹 2. Why Use Encapsulation?
# To protect data from being accessed or modified directly.
# To increase code security, maintainability, and modularity.
# Helps in hiding internal implementation details.

# 3. How is Encapsulation Achieved in Python?
# ACCESS SPECIFIERS: restriction on variable or methods access 
# Encapsulation is implemented using access modifiers:
# Public – accessible from anywhere
# Protected – accessible within the class and its subclasses
# Private – accessible only within the class

# 🔹 4. Access Modifiers in Python
# Python doesn't have real "private" or "protected" keywords, but uses naming conventions:

# | Access Type | Syntax Example | Access Level                      |
# | ----------- | -------------- | --------------------------------- |
# | Public      |   self.name    | Everywhere (default)              |
# | Protected   |   self._name   | Within class and subclasses       |
# | Private     |   self.__name  | Within class only (name mangling) |

# 🔹 5. Public Members
# Declared without any underscore.
# Accessible from outside the class.
# class Person:
#     def __init__(self, name):
#         self.name = name  # public

# p = Person("Alice")
# print(p.name)  # ✅ Accessible


# 🔹 6. Protected Members
# Prefix with a single underscore _.
# By convention, should not be accessed directly from outside, but it's not enforced by Python. we can access outside but not legally

# class Person:
#     def __init__(self, name):
#         self._name = name  # protected

# p = Person("Bob")
# print(p._name)  # ⚠️ Possible, but discouraged


# 🔹 7. Private Members
# Prefix with double underscore __.
# Python does name mangling, so it cannot be accessed directly.
# Can still be accessed using _ClassName__membername (not recommended).

# class Person:
#     def __init__(self, name):
#         self.__name = name  # private

# p = Person("Charlie")
# # print(p.__name)  # ❌ Error
# print(p._Person__name)  # ✅ But discouraged


# eg.
# class Bank:
#     name = 'pratik'
#     _acc_num =12345
    
#     def Details(self):
#         print(self.name)
#         print(self._acc_num)
    
# b=Bank()
# b.Details()
# print(b.name)
# print(b._acc_num)
# b.name='aniket'
# b._acc_num=67890
# print(b.name)
# print(b._acc_num)
        









# 🔹8. Getters and Setters
# Special methods used to access (get) and modify (set) private data safely.
# Useful for data validation.

# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary  # private

#     def get_salary(self):         # getter
#         return self.__salary

#     def set_salary(self, amount):  # setter
#         if amount > 0:
#             self.__salary = amount
#         else:
#             print("Invalid salary")
#     def del_salary(self):           #deleter
#         del self.__salary

# e = Employee(5000)
# print(e.get_salary())  # 5000
# e.set_salary(6000)
# print(e.get_salary())  # 6000
# e.del_salary()
# print(e.get_salary())  # AttributeError


# class Student:
#     def __init__(self,name,sub):
#         self._name  = name
#         self._sub = sub
#     def getter(self):
#         return self._name,self._sub
#     def setter(self,name,sub):
#         self._name=name
#         self._sub=sub
#     def deleter(self):
#         del self._name,self._sub
        
# t = Student('abc','java')
# print(t.getter())
        


# 9. Using @property Decorators (Advanced Pythonic Way)
# Python provides the @property decorator to turn a method into a property.
# Cleaner syntax for getters and setters.

# class Product:
#     def __init__(self, price):
#         self.__price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value > 0:
#             self.__price = value
#         else:
#             print("Invalid price")
#     @price.deleter
#     def price(self):
#         del self.__price

# p = Product(100)
# print(p.price)  # Getter
# p.price = 150   # Setter
# print(p.price) 
# del p.price     # deleter 
# print(p.price)






# class Product:
#     def __init__(self, price,model):
#         self.__price = price
#         self._model = model
        
#     @property
#     def price(self):
#         return self.__price,self._model

#     @price.setter
#     def price(self, value):
#         self.__price, self._model = value
#     @price.deleter
#     def price(self):
#         del self.__price,self._model

# p = Product(100,'realme 14 pro')
# print(p.price)  # Getter
# p.price = (9999,'iphone 16')  # Setter
# print(p.price) 
# del p.price     # deleter 
# print(p.price)



# class Product:
#     def __init__(self, price,model):
#         self.__price = price
#         self._model = model
        
#     @property
#     def price(self):
#         return self.__price,self._model

#     @price.setter
#     def price(self, value):
#         self.__price, self._model = value

# p = Product(1000,'iphone')
# price,model = p.price  # ValueError: not enough values to unpack (expected 3, got 2) when we use one more variable 
# print(p.price)
# print("Phone price is:", price)
# print("Phone model is:", model)




class Marks:
    def __init__(self,std_id,std_yr_of_study,clg_name):
        self.ID = std_id
        self._yop = std_yr_of_study
        self.__cname = clg_name
    
    @property
    def GetData(self):
        return self.ID,self._yop,self.__cname
    
    @GetData.setter
    def GetData(self,value):
        self.ID ,self._yop,self.__cname= value
              
    @GetData.deleter
    def GetData(self):
        del self.ID, self.__cname, self._yop
        
m = Marks(101,2025,'Pyspiders')
print(m.GetData)
m.GetData = (102,2024,'Qspiders')
print(m.GetData)
id,yop,classname = m.GetData
print(id,yop,classname)

    
        
















# 🔹 10. Encapsulation vs Abstraction (Quick Comparison)

# | Feature        | Encapsulation                      | Abstraction                            |
# | -------------- | ---------------------------------- | -------------------------------------- |
# | Focus          | Hiding data                        | Hiding implementation details          |
# | Level          | Class level                        | Design level (what vs how)             |
# | Tool in Python | Private variables, getters/setters | Abstract classes, interfaces (via ABC) |


# 🔹 11. Real-life Analogy of Encapsulation
# Think of a TV remote:
# You only press buttons (public interface).
# You don’t know (or care) how the internal circuit works (private data/methods).
# This is encapsulation — hiding complexity and exposing only what is needed.

# 🔹 12. Key Benefits of Encapsulation
# Prevents accidental data modification
# Adds control over data using getters/setters
# Makes code more flexible and maintainable
# Helps in debugging and future enhancements
