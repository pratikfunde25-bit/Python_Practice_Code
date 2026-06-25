# i=0
# while i<=10:
#     print(i)
#     i+=1

# i = 10
# while i>=1:
#     print(i)
#     i-=1


# i = 65
# while i<=90:
#     print(chr(i) ,end=" ")
#     i+=1
# print()    
# j = ord('a')
# while j<= ord('z'):
#     print(chr(j),end=" ")
#     j+=1
    

# x=65
# y=97
# while x<=90 and y<=122:
#     print(chr(x), chr(y),end=" ")
#     x+=1
#     y+=1
# print()  
# s = ['python','sql','java','c++','webtech']

# i = 0
# while i<len(s):
#     if len(s[i])%2==0:
#         print(s[i],i)
#     i+=1
        
# s = [23,67,89,10,4,2,11]
# i = 0
# while i<len(s):
#     if s[i]%2==1:
#         print(f'the number {s[i]} is odd ')
#     i+=1

#wap to porint 0 to 20 even and odd number in seperate list 

# i = 0
# j = 1

# while i<=20 and j<=20:
#     if(i%2==0):
#         # print ("Even Numbers :")
#         print(i, end=" ")

#     i+=1
#     print()
#     if (j%2==1):
#         # print("Odd Numbers :")
#         print(j, end = " ")
#     j+=1


# i = 0
# even = []
# odd = []

# while i<=20:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
#     i+=1
# print(even)
# print(odd)


#wap to print only collection data types
# s = [23,45,89,[1,2,3],{45,67},{89,90},"hiiii"]

# i = 0
# while i<len(s):
#     if type(s[i])in [str,list,tuple,dict,set]:
#         print(s[i])
#     i+=1



# WAP to print 10 to 300 

# i =10
# while i<=300:
#     print(i)
#     i+=10


#WAP TO PRINT 1 TO 10 NUMBERS IN SQUARE FORMAT

# i=1
# while i<=10:
#     print(i,"=",i*i)
#     i+=1


# WAP TO PRINT FOLLOWING NUMBERS :

# i=105
# while i>=7:
#     print(i ,end=" ")
#     i-=7

# WAP TO PRINT 2 TABLES LIKE 2 X 1 = 2 , 2 X 2 = 4

# i = 1
# j = 2  
# `i<=10:
#     print(j ,"X" , i, "=" ,j*i) 
#     i+=1



#WAP TO PRINT EVEN POSTIONAL CHARACTER IN THE GIVEN STINR G
# s = "hello world"
# i = 0
# while i < len(s):
#     print(i, s[i])  # prints index and character with space in between
#     i += 2


#WAP TO PRINT THE NAMES ONLY IF THE LENGTH OF THE NAMES IF EVEN 

# l = ['vaidegi','ashwini','patil','srinidhi','susmitha','rahul','priyanka','usha']

# i=0
# while i<len(l):
#     if len(l[i])%2==0:
#         print(l[i])
#     i=i+1


# WAP TO PRINT THE NAME WHICH IS STARTING WITH VOWEL IN THE GIVEN LIST 

# names = ['agra','bangalore','mumbai','pune','indore','isha','eshwar','surat']
# i=0
# while i<len(names):
#     if names[i].lower.startswith (('a','e','i','o','u')): # if names[i][0] in 'aeiouAEIOU'
#         print(names[i])
#     i+=1

#WAP TO PRINT ONLY VOWELS AND NUMBERS 
# s='hello123'
# i=0
# while i<len(s):
#     if s[i].lower() in ('a','e','i','o','u') or s[i].isdigit():
#         print(s[i])
# i=i+1
# s = 'hello123'
# i = 0
# while i < len(s):
#     if s[i].lower() in ('a', 'e', 'i', 'o', 'u') or s[i].isdigit():
#         print(s[i])
#     i += 1

#WAP TO PRINT SUM OF THE LIST 

# s = [1,2,3,4,5,6]
# i=0
# sum=0
# while i<len(s):
#     sum +=s[i]
#     i+=1

# print(f'the sum of the list is {sum}')



    




#WAP IF A NAMES ENDS WITH VOWELS THEN REVERSE A NAMES ELSE PRINT ITS LENGHT

# names = ['kumar','lakita','umesh a','priyanka']

# i=0
# while i<len(names):
#     if names[i].lower().endswith(('a','e','i','o','u')):
#         print(names[i][::-1])
    
#     else:
#         print(len(names[i]))
#     i+=1
    
    
        
        
    
# year = int (input("enter the yaer :"))
# if year % 4 ==0 and year % 100!=0:
#     print('this is the leap year')
# else:
#     print(f'the year {year } is not a leap year')
     
#wap to print first 1 to 10 number and squares using while loop

# i=1
# while i<=10:
#     print(f'{i}^2 == {i*i}')
#     i+=1

#wap to print sum of first  10  even numbers

# i=0
# sum=0
# while i<20:
#     print(i)
#     sum+=i
#     i+=2
# print(sum)

# Write a program to display all the numbers which are divisible by 13 but
# not by 3 between 100 and 500.(exclusive both numbers)

# i=101
# while i<500:
#     if i%13==0 and i%3!=0:
#         print(i)
#     i+=1

# Write a python program to get the following output

# 1-----49
# 2-----48
# 3-----47
# 4-----46 
# ...
# 47-----3
# 48-----2
# 49-----1

# i=1
# while i<50:
#     print(f'{i}----{50-i}')
#     i+=1

# Write a Program to separate positive and negative number
# from a list.
# a=[1,2,3,4,-90,-45,-33,-87]
#output
# Positive=[1,2,3,4]
# Negative=[-90,-45,-33,-87]

# a=[1,2,3,4,-90,-45,-33,-87]
# i=0
# Positive=[]
# Negative=[]
# while i<len(a):
#     if a[i]>0: 
#         Positive.append(a[i])
#     elif a[i]<0:
#         Negative.append(a[i])
#     else:
#         print("invalid value")
#     i+=1
# print("positive  = ",Positive)
# print("negative = " ,Negative)
    
# .Write a program that appends the type of
# elements from a list.
# n = [23, 'Python',23.98]
#output:-->[<class 'int'>, <class 'str'>, <class 'float'>]
        
# n = [23, 'Python',23.98]
# i=0
# output=[]
# while i <len(n):
#     output.append(type(n[i]))
#     i+=1
# print(output)


# w = [1, 2, 3, 4, 5, ['hii', 90.34, 123], 900, 123, 9+4j]
# output = []

# i = 0
# while i < len(w):
#     if isinstance(w[i], list):  # If the element is a list
#         j = 0
#         while j < len(w[i]):
#             output.append(w[i][j])  # Append inner elements
#             j += 1
#     else:
#         output.append(w[i])  # Append single value directly
#     i += 1

# print("Flattened output:", output)



# i=0
# while i<len(w):
#     if isinstance(w[i],list):
#         x=w.pop()
     
     
######################################################################################
#                       WHILE LOOP PRACTICE QUESTIONS 

# Q1.Write a program to print the following using while loop 
# First 10 Even numbers 
# 1.
# i=0
# while i<20:
#     print(i)
#     i+=2
# 2.
# i=0
# count=1
# while count<=10:
#     print(i)
#     i+=2
#     count+=1

# Q2.First 10 Odd numbers 
# i=1
# count=1
# while count<=10:
#     print(i)
#     i+=2
#     count+=1
# Q3. First 10 Natural numbers 

# i=1
# while i<=10:
#     print(i)
#     i+=1
    
# Q4. First 10 Whole numbers  

# i=0
# while i<10:
#     print(i)
#     i+=1   

#Q5. Write a program to print first 10 integers and their squares using while loop. 

# i=1
# while i<=10:
#     print(f'{i} ---> {i*i}')
#     i+=1

# Q6. Write while loop statement to print the following series: 10, 20, 30 … … 300 

# i=10
# while i<=300:
#     print(i)
#     i+=10

# Q7. Write a while loop statement to print the following series 105, 98, 91 ………7. 

# i=105
# while i>=7:
#     print(i, end=" ")
#     i-=7

# Q8. Write a program to print the first 10 natural number in reverse order using while loop. 
# i=10
# while i>=1:
#     print(i,end=' ')
#     i-=1

# Q9. Write a program to print sum of first 10 Natural numbers.

# i=1
# sum=0
# while i<=10:
#     sum+=i
#     i+=1    
# print(f'the sum of first 10 Natural numbers is {sum}')


# Q10. Write a program to print sum of first 10 Even numbers.

# i=2
# sum=0
# while i<=20:
#     sum+=i
#     i+=2
# print(sum)

# i=2
# count=1
# sum=0
# while count<=10:
#     if i%2==0:
#         sum=sum+i    
#         count+=1
#     i+=1
# print(sum)

#Q11. Write a program to print table of a number entered from the user. 

# number = int(input("enter the number :"))
# i=1
# while i<=10:
#     print(number*i)    
#     i+=1

#Q12. Write a program to print all even numbers that falls between two numbers (exclusive 
# both numbers) entered from the user using while loop. 

# _start_= int(input("enter starting number :"))
# end = int (input("enter the last number :"))
# current= _start_ +1

# while current<end:
#     if current%2==0:
#         print(current)
    
#     current+=1
 
# _start_= int(input("enter starting number :"))
# end = int (input("enter the last number :"))
# _start_+=1
# while _start_<end:
#     if _start_%2==0:
    
#         print(_start_)
#     _start_+=1

# Q13. Write a program to check whether a number is prime or not using while loop. 

# num = int(input("enter the number :"))
# i=2
# while i<num:
#     if num%i==0:
#         print('the number is not prime' ,num)
#         break
#     i+=1
# else:
#     print('the number is prime' ,num)


# Q14. Write a program to find the sum of the digits of a number accepted from the user. 
    
# num = eval(input("enter the number :"))
# num1= str(num)
# i=0
# sum=0
# while i<len(num1):
#     print(num1[i])
#     sum=sum+int(num1[i])
#     i+=1
# print(sum)

# a='hello'
# i=0
# while len(a)>i:
#     print(a[i],i)
#     i+=1

# Q15. Write a program to find the product of the digits of a number accepted from the user. 

# num = eval(input("enter the number :"))
# num1= str(num)
# i=0
# product=1
# while i<len(num1):
#     print(num1[i])
#     product=product*int(num1[i])
#     i+=1
# print(product)

# Q16. Write a program to reverse the number accepted from user using while loop. 

# num = eval(input("enter the number :"))
# num1= str(num)
# i=0
# rev= ''
# while i<len(num1):
#     rev=num1[i]+rev
#     i+=1
# print(rev)

# Q17. Write a program to display the number names of the digits of a number entered by 
# user, for example if the number is 231 then output should be Two Three One 

# number = int(input("enter the number :"))
# num1= str(number)
# i=0
# while i < len(num1):
#     if num1[i]=='0':
#         print("Zero",end=" ")
#     elif num1[i]== '1':
#         print("One",end=" ")
#     elif num1[i]=='2':
#         print("Two",end=" ")
#     else:
#         print (" 012 tak")
#     i+=1

# Q18. Write a program to print the Fibonacci series till n terms (Accept n from user) using 
# while loop. 

# n = int(input("enter the number till n terms fibo:"))
# a =0
# b = 1

# i =0
# while i < n:
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
#     i+=1
# print()

# Q19. Write a program to print the factorial of a number accepted from user. 

# i=1
# fact=1
# num=int(input("enter the number :"))
# while i<=num:
#     fact*=i
#     i+=1
# print(fact)

# Q20. Write a program to check whether a number is Armstrong or not. (Armstrong number is 
# a number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.) 

# num=153
# num1=str(num)
# sum=0
# i=0
# while i<len(num1):
#         # print(num1[i],"--->", int(num1[i])**3)
#         sum=sum+int(num1[i])**3
#         i+=1
# if num==sum:
#     print("number is armstrong ")
         
# else:
#     print("number is not armstrong ")
        
# Q21. Write a program to add first n terms of the following series using a while loop: 
# 1/1! + 1/2! + 1/3! + …….. + 1/n! 
# n = int(input("Enter the number of terms: "))
# i = 1
# sum = 0
# while i <= n:
#     fact = 1
#     j = 1
#     while j <= i:
#         fact *= j
#         j += 1
#     sum += 1 / fact
#     i += 1
# print("Sum of the series is:", sum)




    
    
        
        
    










        



