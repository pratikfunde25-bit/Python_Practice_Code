class Grand_Parent :
    def grandmethod(self):
        print('Hello Grand Parent ...')

class Father(Grand_Parent):
    def dadmethod(self):
        print("hello Father method...")

class Mother():
    def mothermethod(self):
        print("hello Mother method ....")
        
class Child (Father,Mother):
    
    def __init__(self):
        self.dadmethod()
        self.mothermethod()
        self.grandmethod()
    def Childmethod(self,name,age):
        print(f'my name is {name}, my age is {age}')
        
    

c = Child()
d = Child()
c.Childmethod('pratik',22)

