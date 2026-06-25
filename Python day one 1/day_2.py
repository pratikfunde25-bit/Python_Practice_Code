# Q1 WAP to check number is odd (take user Input)

# a = eval(input("Enter the number :"))
# if a%2==1:
#     print("The given number is Odd ") 
    
    
# Q2  WAP to check the number is even (take user Input)

# b= eval(input("Enter the number :"))
# if b%2==0:
#     print("The given number is Even")
    
# Q3  WAP to check if the student has scored 70% print "Good luck "(take user input)

# c= eval(input("Enter your Score :"))
# if c==70:
#     print("good luck")

#  Q4  WAP to check which number is greater using if condition 

# a=98
# b=67
# if a>b :
#     print(f'the number {a} is greater ')
# if b>a:
#     print(f'the number {b} is greater')

# Q5  WAP to check if the given string has even length of character
# s="hey guys you all are Osam"
# print(len(s))
# if len(s)%2==0:
#     print("Yes , given string has even length of character")
    
# Q6  WAP to check the given number is divisible by 5 (take user input)

# d=eval(input("Enter the number :"))
# if d%5==0:
#     print(f"The given number {d} is divisible by 5")

# Q7  WAP to chcek if the given programming is present in the list 

# p=["java","python","c","c++","RUBy","golang"]

# e=(input("Enter the Programming Language :"))
# if e in p:
#     print("The language is Present in the list ")

# Q8.WAP to check eligible to vote take user input as a age

# age= int(input("Enter Your Age :"))
# if age>=18:
#     print("Yes , You are eligible to vote ")

# Q9.wap to check if the given number is positive take user input

# num = int(input("Enter a number :"))
# if num>0:
#     print("Given number is positive")

#10.wap to check if the given string is palindrome (take user input)

# input_str = input("Enter a String :")
# if input_str.strip().lower() == input_str[::-1].strip().lower():
#     print("The given string is Palindrome") 
    
    
#11.wap to check if the first letter in the given string is consonant

# s="Lahari is a good student"
# if s[0].lower() not in ['a','e','i','o','u']:
#     print("The First letter of given string is consonant")

#12. .wap to check the given string is uppercase or not (take user input)

# str_1 = input("Enter a String :")
# if str_1.isupper():
#     print("The given string is uppercase")
    
# Q13.wap to check the given value is string (take user input)

# str_1 = eval(input("Enter a String :"))
# if isinstance(str_1,str):
#     print("The given value is String ")

# Q14.wap to display "Python Coding" if the number is greater than 1 and less than 5 (take user input)

# num = eval(input("Enter a Number :"))
# if num > 1 and num <5:
#     print("Python Coding")

#Q15.wap to check whether given number is negative and print "its negative guys"

# num = eval(input("Enter a number :"))
# if num < 0:
#     print("its negative guys")

#Q16.wap to check whether given input is divisible by 2 and 6 if condition is True ,convert the given number to complex number.(take user input)

# num = eval(input("Enter a number :"))
# if num%2==0 and num%6==0 :
#     print(complex(num))

#17.wap to check whether the given number is even or not,if even store the value inside the list (take user input)

# num = eval(input("Enter a number :"))
# if num%2==0:
#     l1= []
#     l1.append(num)
#     print(l1)

#Q 19.wap to check whether a given value is divisible by 5 and 7,if the value is divisible then display the square of the values (take user input)

# num = eval(input("Enter a number :"))
# if num%5==0 and num%7==0:
#     print(f'The square of the {num} is {num**2}')


# Q 20.wap to check whether a given value is present in between 45 and 200 and the number should be divisible by 4 and 5 ,if satisfied,display the ascii characters (take user input)

# num = eval(input("Enter a number :"))
# if num>45 and num<200 and num % 4 ==0 and num % 5 == 0:
#     print(f"the ascii character of given number is {chr(num)}")

# Q 21.wap to checking if a string contains a substring

# string="hello world"
# sub_string="world"
# if sub_string in string :
#     print("yes a string contains a substring")

#Q 22. wap to check whether a character is in the alphabet or not,if it is alphabet,store the value inside  a dict(key as a character and value as a ascii value)

# char = input("Enter a character :")
# if char.isalpha():
#     d = {char:ord(char)}
#     print(d)

# Q 23.wap to check whether a character is in uppercase or not,if uppercase,convert to lowercase and store the value inside the dictionary (character as key and ascii as value) take user input
# char = input("Enter a character :")
# if char.isupper():
#     char = char.lower()
#     d = {char:ord(char)}
#     print(d)
    
    
# word = input("Enter a word: ")
# char_dict = {}
# for char in word:
#     if char.isalpha(): 
#         char_dict[char] = ord(char)
# print(char_dict)
