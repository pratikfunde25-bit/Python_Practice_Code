# class Myclass:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
        
#     def __getitem__(self,index):            #def __getitem__(self,item)
#         if index==0:
#             return self.a
#         elif index==1:
#             return self.b
#         elif index==2:
#             return self.c
#         else:
#             raise IndexError
        
# m=Myclass(10,20,30)
# print(m.__getitem__(2))


# class Student:
#     def __init__(self,marks,sub):
#         self.m=marks
#         self.s=sub
        
#     def __getitem__(self,index):
#         if index==0:
#             return self.m
#         elif index==1:
#             return self.s
#         else:
#             raise IndexError
# s=Student(78,'python')
# print(s.__getitem__(0))

# class Point():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
        
#     def __setitem__(self,index,value):
#         if index==0:
#             self.a=value
#         elif index==1:
#             self.b=value
        
#     def __getitem__(self,index):   # self, key (index is not necessary you can use any thing )
#         if index=='k':
#             return self.a
#         elif index==1:
#             return self.b
#         else:
#             raise IndexError
# p=Point(100,500)
# print(p.__getitem__('k'))
# print(p.__getitem__(1))
# p.__setitem__(0,1000)   #(key , value )
# p.__setitem__(1,5000)   # (key OR (index) ,value)
# print(p.__getitem__('k'))
# print(p.__getitem__(1))


# class Employee:
#     def __init__(self,name,id,sal):
#         self.name= name
#         self.id=id
#         self.sal=sal
#     def __getitem__(self,key):
#         if key=='name':
#             return self.name
#         elif key=='id':
#             return self.id
#         elif key=='sal':
#             return self.sal
#         else:
#             raise KeyError
#     def __setitem__(self,key,value):
#         if key=='name':
#             self.name = value
#         elif key=='sal':
#             self.sal = value
#         elif key =='id':
#             self.id = value
#         else:
#             print("not set the item")
# e = Employee('pratik',101,50000)
# print(e.__getitem__('sal'))
# print(e.__getitem__('name'))
# print(e.__getitem__('id'))
# (e.__setitem__('name','aishu'))
# (e.__setitem__('id',102))
# print(e.__getitem__('sal'))
# print(e.__getitem__('name'))
# print(e.__getitem__('id'))

        

# class Storage:
#     def __init__(self,*values):
#         self.list=[]
#         for i in values:
#             self.list.append(i)
#     def __len__(self):
#         return len (self.list)
#     def __contains__(self,item):
#         return item in self.list
#     def __delitem__(self,key):
#         # del self.list[key]  # delete the element using index
#         return self.list.remove(key)  # delete the element using element
#         pass
#     def __getitem__(self,index):
#         return self.list[index]
#     def __setitem__(self,key,value):
#         self.list[key] = value
        

    
# s=Storage(100,20,165,'sadlk' ,'asdlkf',True, False)
# print(s.list)
# print(s.__len__())
# print(s.__contains__(1000))
# (s.__delitem__(20))
# print(s.list)
# print(s.__getitem__(0))
# (s.__setitem__(1,200))
# print(s.list)



# Number Protocols 

# class Product:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self,other):
#         return Product(self.a+other.a,self.b+other.b)   # when we use Product str is mandatory
    
#     def __sub__(self,other):
#         return (self.a-other.a,self.b-other.b)
#     def __mul__(self,other):
#         return (self.a*other.a,self.b*other.b)
#     def __floordiv__(self,other):
#         return(self.a//other.a,self.b//other.b)
#     def __gt__(self,other):
#         return((self.a,self.b)>(other.a,other.b))
#     def __str__(self):
#         return f'{self.a} and {self.b}'    #not compulsory when we didnt mention class name
# p=Product(10,1)
# p1=Product(5,3)
# print(p.__add__(p1))
# print(p.__sub__(p1))
# print(p.__mul__(p1))
# print(p.__floordiv__(p1))
# print(p.__gt__(p1))





