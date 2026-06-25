#WAP to check a data is a sequence / iterable / individual data types 
# a=10
# data = eval(input("enter the data :"))
# if type(data) in [int , bool , complex,float]:
#     print("the data is of individual data type")
# elif isinstance(data,(str,list,tuple)):
#     print("the data is the sequence data type")
# elif isinstance(data,(dict,set)):
#     print("the data is the iterable data type")
 
#Wap if input is string return length if list pop the element if tuple reverse the tuple else print invalid input
   
# input = eval(input("enter the input:"))
# if type(input)in [str]:
#     print(len(input))
# elif type(input)==list:
#     input.pop()
#     print(input)
    
# elif type(input)==tuple:
#     print(input[::-1])
# else:
#     print("invalid data")

    
# age = eval(input("Enter your age :"))
# if 0<=age<=17:
#     print("child ")
# elif 18<=age<=30:
#     print("adult")
# elif age>30 and age <=60:
#     print("senior citizen")
# else:
#     print("INVALID")

# 5 wap to check which is the smallest value among 3 numbers 
# a =65
# b=34
# c=76
# if b>a<c:
#     print("A is smaller")
# elif a>b and c>b:
#     print("B is smaller")
# else :
#     print("C is smaller")


#wap to take marks of 5 sub calculate the average if avg is bw 90-100 print Distinction if 75-89 first class 60-74 second class 50-59 print third class

# s1=eval(input ("enter marks :"))
# s2= eval(input ("enter marks :"))
# s3= eval(input ("enter marks :"))
# s4= eval(input ("enter marks :"))
# s5= eval(input ("enter marks :"))

# avg= (s1+s2+s3+s4+s5)/5
# if  100>=avg>=90:
#     print("Distinction")
# elif 89>=avg>=75:
#     print("First Class")
# elif 60<=avg<=74:
#     print("second Class")
# elif avg >50 and avg <60:
#     print("third Class")



# s1=eval(input ("enter marks :"))
# s2= eval(input ("enter marks :"))
# s3= eval(input ("enter marks :"))
# total = s1+s2+s3
# if total < 1000:
#     print("No Discount ")
# elif total >=1000 and total <=3000:
#     print(total-500)
# elif total >=3001 and total <=5000:
#     print(total-1000)
# elif total >5000 :
#     print(total =1200)



# wap to book a ticket in book my show 

# Theater = ["PVR","Cinipolo","max","inox"]
# user = (input("enter the theater name :"))
# if user in Theater :
#     print(f'user is selected the theater {user}')
#     movies = ["RRR","animal","KGF"]
    
#     user2 = input("enter the movie name :")
#     if user2 in movies :
#         print(f'user on is selected the theater is {user} and user2 is selected the movie is {user2}')
#         amount = eval (input("enter the amount :"))
#         ticket_amount = [1000,2000,3000]
#         if amount==ticket_amount[0]:
#                     print(f'user on is selected the theater is {user} and user2 is selected the movie is {user2} and the amount of show is {amount}')
#         elif amount==ticket_amount[1]:
#                     print(f'user on is selected the theater is {user} and user2 is selected the movie is {user2} and the amount of show is {amount}')
#         elif amount==ticket_amount[2]:
#                     print(f'user on is selected the theater is {user} and user2 is selected the movie is {user2} and the amount of show is {amount}')
#         else:
#             print("wrong price")
#     else:
#         print("wrong movie ....")
# else:
#     print("wrong theatre name ...")


            
