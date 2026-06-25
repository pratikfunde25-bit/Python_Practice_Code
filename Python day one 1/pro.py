# class Student :
#     def details(self, name,id, sal):
#         print(f"my name is {name},my id is {id},my salary is{sal}")
# s= Student()
# s.details("xyz",234,5555)
# Student.details("xyz",234,55)

# class College:
#     sal = 100000
#     def details(self):
#         print(f"my total fees is {College.sal}")
#         print(f"my total fees is {self.sal}")  
#         print(f"my total fees is {e.sal}")
        
# e=College()
# e.details()
# # Employee.details(self)# getting error self is not defined NameError 
# print(e.sal)

# class Pyspider:
#     mock = "*"
#     def python(self):
#         print(f'{self.mock}')
#     def SQL (self):
#         print(f'{self.mock}')
# p = Pyspider()
# p.mock= 12
# Pyspider.python(p)
# p.python()
# p.SQL()
# print(p.mock)   
# print(Pyspider.mock)    


# class Student :
#     def details (self, name ,id,  sal):
#         # name= 100
#         # id =1
#         # sal=10
#         print(f'my name is  {name } and my id is {id} and mine total salary is {sal}') 
# s = Student()
# s.details("xyz",101,99999)
# Student.details(s,"xyz",101,99999)




# WAP TO ACCEPT THE LIST FROM USER WHEN THE METHOD IS CALLED, FIRST INDEX ELEMENT IN THE LIST IF IT IS STRING THEN REVERSE THE STRING , THEN REPLACE IN SAME POSITION AND RETURN ELSE IF IT INTEGER THEN ASK FOR USER TO ADD A ELEMENT INTO A LIST AND RETURN THE UPDATED LIST ELSE REVERSE THE LIST AND RETURN 

# class list:
#     list_1 = eval(input("enter the list :"))
#     def method(self):
#         print(list.list_1)
#         print(type(list.list_1))
        
#         if(type(list.list_1[0])==str):
#             print(list.list_1[0][::-1])
            
#         elif(type(list.list_1[0]==int)):
#             data = eval(input("enter the  number :"))
#             list.list_1.append(data)
#             print(list.list_1)
#         else:
#             return list[::-1]
# obj1 = list()
# obj1.method()



# class test :
#      def __init__(self,a=0,b=0,c=0):
#          print(a+b+c)

# t1=test(1)
# t2= test(1,2)
# t3=test(1,2,3)


# class Bank :
#     def __init__(self):
#         self.bal = 0.0
#     def deposit(self,amount):
#         self.bal+=amount
#         print(f'total balance is {self.bal}')
# b = Bank()
# Bank.bal=5000
# print(b.bal)
# b.bal=5000
# b.deposit(5000)
# Bank.deposit(2000)
# Bank.__init__(2000)



