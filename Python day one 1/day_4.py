#  wap to check if num is 0 print as it is if it is even print square of num , if num is odd make cube of num


# num = eval(input("Enter a number :"))
# if num==0:
#     print(f'the number is {num}')
# elif num%2==0:
#     print(f'the number is even and square is  {num*num}')
# elif num%2==1:
#     print(f'the number is odd and cube is {num**3}')
# else:
#     print(f'the number  {num} is invalid')
    
    
    
#wap to check string is started with vowels print length of str elif print square of the length of str  (take user input)

# str1= input("Enter a String:")
# if str1[0] in ['a','e','i','o','u']:
#     print(len(str1))
# elif str1[0] in '0123456789':
#     print(len(str1)**3)
# elif str1[0] not in ['a','e','i','o','u'] : 
#     print(len(str1)**2)
    
#WAP to take age from user and check is it elible for marriage or 21 or greater 

# age = eval(input("enter your age :"))

# if age>50:
#     print("too young ")
# elif age > 21:
#     print("eligible ")
# elif age < 21:
#     print(f"not eligible wait for {21-age}")
    

#WAP 
# num = eval(input("enter a number :"))
# if num%2==0 and num%3==0  :
#     print("fizzbuzz")
# elif num%3==0:
#     print("fizz")
# elif num%2==0:
#     print("buzz")

#WAP to take one char from user if char is uppercase convert into lowercase  but if char is lowercase then convet into uppercase if char is number then print their ascii values 

# char = (input("enter a char :"))
# if char.islower():
#     print(char.swapcase())
# elif char.isupper():
#     print(char.swapcase())
# elif char.isdigit():
#     print(ord(char))

# char = (input("enter a char :"))
# asc = ord(char)
# if ord(char) in range(97,122):
#     print(ord(char)-32)
# elif ord(char) in range (65,91):
#     print(ord(char)+32)
# elif ord(char) in range (48,58):
#     print(ord(char))
    
  
ch = (input("enter a char :"))  
asc = ord(ch)
if 'A'<=ch<='Z':
    print(chr(asc+32))
elif 'a' <= ch <= 'z':
    print(chr(asc-32))
elif '0' <=ch<='9':
    print(ord(ch))
    



    
    

    


    
