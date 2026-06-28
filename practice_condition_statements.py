# WAP to check whether the first item of these two lists is either integer or not.
# If it is an integer, concatenate these two lists or else print the memory
# address of these two lists.

# l1 = [2,2,3,4,5,6,7]
# l2 = [22,56,1,2,3,6,5,4,7]
# # print(type(l2[0]))
# if type(l1[0])==int and type(l2[0])==int:
#     print(l1+l2)
# else:
#     print(id(l1))
#     print(id(l2))
    

# WAP to perform addition and subtraction operation by using list collection if the
# first and middle data items number are even performing addition operation, or
# else performing subtraction.

# l = [10, 25, 30, 45, 60]
# first = l[0]
# middle = l[len(l)//2]

# if first%2==0 and middle%2==0 :
#     for x in l:
#         print(x+5)
# else:
#     for x in l:
#         print(x-5)
    
    

# Ravi would like to buy a new cello or red pen. The cost of the pen should be 10.
# If the pen is available in the shop, he will buy the pen. If it is not there he will
# come out of the shop.
# is_available= True
# pen = input("enter the type of pen (cello/red):").lower()
# if pen in ['cello','red']:
#     cost = eval(input("enter the cost of pen :"))
#     if cost==10:
#         print("checking the pen is available or not")
#         if is_available:
#             print("buy the pen ")
#         else:
#             print("out of the shop come")
#     else:
#         print("the cost should be only 10")
# else:
#     print("wrong type of pen selected")





# 1.WAP to check whether a number is positive or negative. If Positive print positive
# message or else print Negative Number.

# a = int(input("enter a number :"))
# if a >= 0:
#     print("positive number")
# else :
#     print("negative number ")

# WAP to check whether a number is even or odd. If even, print message an even
# or else print message as odd.

# a = int(input("enter a number :"))
# if a%2==0:
#     print("even number")
# else:
#     print("odd number")

# Write a program to check whether a given number is greater than 10 or not. if it
# is greater than 10 print message as greater or else print that number with not a
# greater than.

# n = 15
# if n>10:
#     print(f"the number {n} is greater than 10")
# else:
#     print(f'the number {n} is smaller than 10')

# WAP to check whether the given two input numbers are divisible by 3 and 5. If it
# is divisible, print “Good Morning”, if it is not divisible print “Good Evening”.

# a = int(input("enter first  number :"))
# b = int(input("enter second number :"))
# if a%3==0 and a%5==0 and b%3==0 and b%5==0:
#     print("Good Morning")
# else:
#     print("Good Evening")

# WAP to accept two integers and check whether those two values are equal or not.
# If equal, multiply to value or else to display the quotation value.

# a = int(input("enter first  number :"))
# b = int(input("enter second  number :"))
# if a==b:
#     print(a*b)
# else:
#     print(a//b)

# WAP to find the largest of two numbers.

# a = eval(input("enter first  number :"))
# b = eval(input("enter second  number :"))
# if a>b:
#     print(f'{a} is greater than {b}')
# else:
#     print(f'{b} is greater than {a}')
    
# WAP to check whether the input number is greater than 10 or not if it is greater
# than 10 print messages as greater with number. if it is not a greater than 10 print
# that number.

# a = eval(input("enter the number :"))
# if a>10:
#     print(f'greater {a}')
# else:
#     print(a)

# WAP to the given number integer, if n is greater than 21,print the absolute
# difference between n and 21 otherwise print twice the absolute difference.

# n = eval(input("enter the number :"))
# if n>21:
#     print(abs(n-21))
# else:
#     # print(abs(2*(abs(n)-21)))
#     print(2*abs(n-21))


# WAP to find the smallest of two numbers.

# a = eval(input("enter first  number :"))
# b = eval(input("enter second  number :"))
# if a<b:
#     print(f'{a} is smallest than {b}')
# else:
#     print(f'{b} is smallest than {a}')


# WAP to check whether the given number is even or odd. If it is even then make
# it as an odd number, if it is an odd number then make it as even number.

# num = eval(input("Enter the number :"))
# if (num//2)*2==num:
#     print(f"Even number to make this number odd {num+1}")
# else:
#     print(f'Odd number {num} made it even {num+1}')

# WAP to check whether the given number is divisible by 3 or not if yes, print the
# number or else print the cube of the numbers.

# num = eval(input("Enter the number :"))
# if num%3==0 :
#     print(num)
# else:
#     print(num**3)

# WAP to check whether the given input is divisible by 3 and 5. If yes print the
# actual number or else print string of that number.

# num = eval(input("Enter the number :"))
# if num%3==0 and num%5==0:
#     print(num)
#     print(type(num))
# else:
#     a = str(num)
#     print(a)
#     print(type(a))


# WAP to check whether the given number lies between 1 to 19, if it is true square
# that number or else false cube that number and display the number.

# num = eval(input("Enter the number :"))
# if 1<=num<=19:
#     print(num*num)
# else:
#     print(f'cube of {num} = {num**3}')


# WAP to check whether the student has passed or failed. If the student got more
# than 40 marks, print ‘PASS’ along with those marks, if it is not printed ‘FAIL’ along
# with those marks.

# marks = eval(input("Enter the marks :"))
# if marks > 40 :
#     print(f"PASS you got {marks} marks")
# else:
#     print(f'FAIL you got {marks} marks')
    
    
# WAP to check whether a given value is even and in range of 47 to 58 and not in 0
# or odd. if condition is True, to perform display the ascii character. or else to
# perform floor division with 5 and display it.


# num = eval(input("Enter the number :"))
# if num%2==0 and 47<=num<=58 and num !=0 :
#     print(f'the number {num} has ascii character {chr(num)}')
# else:
#     print(num//5)


# WAP to check whether a given value is less than 125 and in between 47 to 125 or
# not. if condition is True, to perform store the given value as key and value as a
# character into the dict or else to append the value in list and display it.
    
# num = eval(input("Enter the number :"))
# if num <125 and 47<=num<=125 :
#     a={}
#     a.update({num:chr(num)})
#     print(a)
# else:
#     l = []
#     l.append(num)
#     print(l)

# WAP to check whether a given character is in the alphabet or not. if alphabet,
# display the alphabet with character or else display the not alphabet with
# character.

# char = input("enter the character :")
# if char.isalpha():
#     print(f'your char {char} is in alphabet')
# else:
#     print(f'your char {char} is not in alphabets')

# WAP to check whether a given character is uppercase or other character. if 
# uppercase, display the uppercase with character or else display the other 
# character with character. 
# char = input("enter the character :")
# if char.isupper():
#     print(f'its a upper case character {char}')
# else:
#     print(f'its lower case {char}')


# WAP to check whether a given character is lowercase or other character. if 
# lowercase, display the lowercase with character or else display the other 
# character with character. 
# char = input("enter the character :")
# if char.islower():
#     print(f"lowercase {char}")
# else:
#     print(f'character {char}')


# WAP to check whether a given character is uppercase or other character. if 
# uppercase, convert to lowercase .or else display the ascii number.

# char = input("enter the character :")
# if char.isupper():
#     print(f'converted to lower {char.lower()}')
# else:
#     print(f'the ascii number of first character {char[0]} is {ord(char[0])}')

# WAP to check whether the given character is in lowercase or uppercase. If it is 
# in lowercase, convert it into uppercase, or else it is in uppercase and convert it 
# into lowercase. Display the value.

# char = input("enter the character :")
# if len(char)==1:
#     if char.isupper():
#         print(char.lower())
#     else:
#         print(char.upper())
# else:
#     print("enter single character")

# WAP to check whether the given string of the first character is a special symbol 
# or not. If a special symbol, to extract and display the middle character or else to 
# reverse the string and display the half of the string. 
 
# str = input("enter a string :")
# if not str[0].isalnum():
#     print(f'the middle character of strig is {str[len(str)//2]}')
# else:
#     rev = str[::-1]
#     print(f"the string is reversed and first half string is {rev[0:len(rev)//2:1]} ")

# WAP to check whether the input character is a vowel or not. If it is vowel print 
# ‘VOWEL’ along with that character, if it is not just print ‘CONSONANT’. 

# str = input("enter a character :")
# if len(str)==1 and str.isalpha():
#     if str.lower() in "aeiou":
#         print(f"char {str} is a VOWEL")
#     else:
#         print("CONSONANT")
# else:
#     print("only one character(alphabet) is valid ...")

# WAP to check whether a given character is a vowel or consonant. if vowel, to 
# print the next character of a given character or else print previous characters. 


# char = input("enter a character :")
# if len(char)==1 and char.isalpha():
#     if char.lower() in "aeiou":
#         print(f'the next char of vowel {char} is {chr(ord(char)+1)}')
#     else:
#         print(f'the previous char of  {char} is {chr(ord(char)-1)}')


# WAP to check whether a given string of first character is alphabet or not 
# if the alphabet prints, reverse the string or else print the middle character.

# str = input("enter a string :")
# if str[0].isalpha():
#     print(str[::-1])
# else:
#     print(str[len(str)//2]) 


# WAP to check whether the given input character is uppercase or lowercase. If 
# the input character is upper case convert into lower case and vice versa.  

# char = input("enter a character :")
# if char.isupper():
#     print(char.lower())
# else:
#     print(char.upper())  

# WAP to check whether a given string is less than 3 characters, to print the entire 
# string otherwise to print after third positions to the remaining string.   


# str = input("enter a string :")
# if len(str)<3:
#     print(str)
# else:
#     print(str[3::]) 
        
# WAP to check whether a given length of the string is even or not. if even, to 
# append the new string called "bye" or else print the first and last characters.


# str = input("enter a string :")
# if len(str)%2==0:
#     l=[str]
#     l.append("bye")
#     print(l)
# else:
#     print(str[0],  str[-1])

# WAP to check whether a given length of the string is odd or not. if odd, to append 
# the new string("Haii") from the starting of the given string, or else to avoid the 
# starting character and ending character of the given 
#  string and to display the remaining characters.
    

# str = input("enter a string :")
# if len(str)%2==1:
#     l="Haii "+str
#     print(l)
# else:
#     print(str[1:-1:1])    

# WAP to check whether the last of the given string is a special character or not, if 
# the special character prints reverse the string except the last character or else to 
# check if the length of the string is odd or not, if odd to extract the middle 
# character to the end of the string.


# str = input("enter the string :")
# if not str[-1].isalnum():
#     print(str[:-1][::-1])
# else:
#     if len(str)%2==1:
#         print(str[len(str)//2::])
#     else:
#         print('YZ neat odd len tak')
         
# WAP to check whether a given year is a leap year or not. if leap year, print leap 
# year or else not a leap year.

# year = int(input("enter the year :"))
# if year%4==0 :
#     print("leap year")
# else:
#     print("not a leap year")

# WAP to find out the greatest of two numbers and display the greatest number. if 
# the greatest number, display the greatest message with value. 
    
# WAP to check whether the given value is present inside the given collection or 
# not.if value is present, display the value is available or else the value is not 
# present.


# val = eval(input("enter the value :")) 
# tup  = (10,20,20.00,20.00,'20.000','pratik',"A",True)
# if val in tup:
#     print(f'the value {val} is present in collection')
# else:
#     print(f'the value {val} is not present in collection')


# WAP whether a given string, if string length is more than 2, then it displays a new 
# string with the first and last characters switched, otherwise the display the 3 
# copies of given string.

# from copy import deepcopy
# str = input("enter the string :")
# if len(str)>2:
#     f=str[0]
#     l=str[-1]
#     print(l+str[1:-1:1]+f)
# else:
#     print(str)
#     print(str)
#     print(str)


# WAP to check whether a given value is a list and first and last values should be 
# integer if condition is satisfied first value is True division by 3 and perform the 
# bitwise not for last value and those result values are stored in same positions in 
# given list or else, to perform length of the collection power by 2 and display 
# value.
    
# v = eval(input("Enter a value: "))
# if isinstance(v, list) and len(v) >= 2 and isinstance(v[0], int) and isinstance(v[-1], int):
#     v[0], v[-1] = v[0] / 3, ~v[-1]
#     print(v)
# else:
#     try: print(len(v) ** 2)
#     except: print("Invalid input")


# WAP to check whether a given value is a string or not and length of the value 
# should be more than 7, if condition is satisfied to append the new string in the 
# middle of the given string or else to perform the replications with 3 and display 
# the result. 

# value = input("Enter a value: ")

# if isinstance(value, str) and len(value) > 7:
#     new_str = input("Enter the new string to insert: ")
#     mid = len(value) // 2
#     result = value[:mid] + new_str + value[mid:]
#     print("Modified string:", result)
# else:
#     print("Replicated string:", value * 3)


# WAP to check if the given string of first and second character should be sequence 
# or not. if the sequence prints the first, second and last two characters, or else the 
# first half string is reversed and the remaining half string should be normal and 
# display it. 

# str = input("enter the string :")
# if chr(ord(str[0])+1) == chr(ord(str[1])):
#     print(str[0],str[1],str[-2::])
# else:
#     print(str[(len(str)//2)-1::-1],str[len(str)//2::1])


# WAP to check whether a given value is present inside the collection or not. If 
# present, print the value or else print value is not found. 


# val = eval(input("enter the value :")) 
# tup  = [10,20,20.00,20.00,'20.000','pratik',"A",True]
# if val in tup:
#     print(f'the value {val} is present in collection')
# else:
#     print(f'the value {val} is not present in collection')
    
    
# WAP to check whether a given key is present in the dict or not. if key is present: 
# display the value or else add key and new value inside the dict. 

# d1 = {'a':67,
#       'b':58,
#       10:20,
#       20:30,
#       40:80}
# val = eval(input("enter the key :"))
# if val in d1:
#     print(d1[val])
# else:
#     val2=eval(input("enter the value "))
#     d1.update({val:val2})
#     print(d1)


# WAP to check whether a given collection is set or not. if set, append the new 
# value, or else eliminate the duplicate values in collection. final results should be 
# set type. 

# a = [10,20,30,40,50,60,10.00,10.20,10,10,'pratik',True]
# if isinstance(a,set):
#     Val= input("enter the value to append in set :")
#     a.add(Val)
#     print(a)
# else:
#     print("you choosen another data type")
#     print(set(a))


# WAP to read the age of a candidate and determine whether it is eligible for 
# his/her own vote or not.it eligible print age and eligible messages or else print 
# not eligible. 

# WAP to check whether a given value is even and in between 47 to 58 and not in 
# 0 or odd. if condition is True, to perform display the ascii character or else to 
# perform floor division with 5 and display it.


# WAP to check whether the given string is palindrome or not if it is a palindrome 
# string palindrome along with the string if it is not a palindrome print not 
# palindrome 
    
# str = input("Enter the string :")
# if str == str[::-1]:
#     print(f"palindrome ----> {str}")
# else:
#     print(f"not palindrome  ---->{str}")

# WAP to check length of both string collections are equal or not. if both are equal 
# print the concat the two strings and display, or else if any one of the collection 
# not equal print both the collections with lengths  

# str1= input("enter first string :")
# str2= input("enter second string :")
# if len(str1)==len(str2):
#     print(str1+str2)
# else:
#     print(len(str1))
#     print(len(str2))


# WAP to check whether both given values point to the same memory location or 
# not. if it is true print the middle item of the second collection, or else if it is false 
# print the first item and last item of the first collection along with the memory 
# address.  

# a=[10,15,30]
# b=[10,20,35]
# b=a
# if id(a)==id(b):
#     print(a[len(a)//2])
# else:
#     print(a[0],a[-1],id(a))
    
# WAP to  check whether a given string collection is more than ten, and the first + 
# last character of the ascii values should be divisible by 5, if condition is satisfied 
# print first, middle, last characters ASCII values or else print the string three 
# times. 

# a='dabcdefghijklmn'
# if len(a)>10 and ord(a[0])%5==0 and ord(a[-1])%5==0:
#     print(ord(a[0]),ord(a[len(a)//2]),ord(a[-1]))
# else:
#     print(a*3)
#     print(ord('a'))


# WAP to check whether the middle of the item present in the list is string data type 
# or not if it is string print that list or else if it is not string  then print that middle 
# item.

# a=[10,'15',30]
# if isinstance(a[len(a)//2],str):
#     print(a)
# else:
#     print(a[len(a)//2])


# WAP Given a string, return a new string where the first and last characters have 
# been exchanged. 

# s = input("Enter a string: ")

# if len(s) < 2:
#     print("Swapped string:", s)  # No change for short strings
# else:
#     swapped = s[-1] + s[1:-1] + s[0]
#     print("Swapped string:", swapped)

# Write a program to find out such numbers which are divisible by 7 but are not a 
# multiple of 5. Both the conditional is satisfied and print actual value. if one 
# condition is not satisfied actual number is multiply by 4 and print result 

# num = int(input("Enter a number: "))

# if num % 7 == 0 and num % 5 != 0:
#     print("Condition satisfied:", num)
# else:
#     print("Condition not satisfied, result =", num * 4)

# WAP to check whether two values are pointing to the same memory address or 
# not. If the same memory displays the address or else displays the two values 
# addresses. 

# a = eval(input("Enter first value: "))
# b = eval(input("Enter second value: "))

# if a is b:
#     print("Both variables point to the same memory address.")
#     print("Memory address:", id(a))
# else:
#     print("Variables have different memory addresses.")
#     print("Address of first value (a):", id(a))

# WAP to check whether a given input character is a special symbol or not if it is a 
# special symbol then print that character three times and tell print that character 
# 5 times.
# ch = input("Enter a character: ")

# if not ch.isalnum():
#     print("Special symbol found:")
#     print(ch * 3)
#     print(ch * 5)
# else:
#     print("Not a special symbol.")


# WAP to check length of both string collections equal or not if it is equal print the 
# connection of any one of the collections if it is not equal print both the collection. 

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# if len(str1) == len(str2):
#     print("Lengths are equal. Any one collection:", str1 + str2)
# else:
#     print("Lengths are not equal. Both collections:")
#     print("First:", str1)
#     print("Second:", str2)

# WAP To check whether both input variables point to the same memory location 
# or not if it is true print the last item of the second collection, if it is false print the 
# first item of the first collection along with the memory address. 

# a = eval(input("Enter first collection (e.g. [1,2,3]): "))
# b = eval(input("Enter second collection (e.g. a or [1,2,3]): "))

# if a is b:
#     print("Same memory. Last item of second collection:", b[-1])
# else:
#     print("Different memory.")
#     print("First item of first collection:", a[0])
#     print("Memory address of a:", id(a))


# WAP to print the string collection five times when the length of the string 
# collection should be more than 3 and the middle character of the string should 
# be vowel and the first character ASCII value should be even, to print the previous 
# character of middle character, or else if ASCII value is odd then print the string 
# three times as print that string.

# s = input("Enter a string: ")

# if len(s) > 3:
#     middle = s[len(s) // 2]
#     if middle.lower() in 'aeiou':
#         if ord(s[0]) % 2 == 0:
#             prev_char = chr(ord(middle) - 1)
#             print("Previous character of middle:", prev_char)
#         else:
#             print("String repeated 3 times:", s * 3)
#     else:
#         print("Middle character is not a vowel.")
# else:
#     print("Length is not greater than 3.")



    
    
# 1.wap to check whether the given number is even and greater than 5

# n= 16
# if n%2==0:
#     if n>5:
#         print("even and more than 5")
#     else:
#         print("even but less than 5")
# else:
#     print("not even")    

# 2.wap to check the number is odd and check if the number is divisible by 5 and 7 both 
# n=35
# if n%2==1:
#     if n%5==0 and n%7==0:
#         print("the number is odd and divisible by 5 and 7")
#     else:
#         print("odd number not divisible by 5 and 7")
# else:
#     print("even number ")


# 3.wap to validate facebook username and password
# condition is:---> username-->"python" and password="python masters"

# username = input("enter username :")
# password = input("enter password :")
# if username=="python":
#     if password=="python masters":
#         print("login successfully")
#     else:
#         print("incorrect password")
# else:
#     print("username not found ")


# 4.wap to find middle element is even or odd take list from user | first check that there is any
# middle element is there or not
# s=[3,4,6,7,9,1,5] for example

# s=[3,4,6,7,9,1,5]
# if len(s)%2==1:
#     print('the given list has middle element ')
#     if s[len(s)//2]%2==0:
#         print("middle element is even")
#     else:
#         print("middle element is odd")
# else:
#     print('the given list has no middle element')


# 5. wap to check that the input is tuple then check it have any middle value or not then middle
# element is of string datatype , it should be a palindrome string and it should have length > 8 
    
# 6. wap to check that the input is tuple then check it have any middle value or not then middle
# element is of string datatype and starting with vowel and it should have length > 8    

    
