#when we know the number of iteration then  we go for FOR LOOP

# SYNTAX ==> 
# for var_name in iterable:
    # statement
# for -> keyword var_name --> any character in --> keyword (membership operator) iterable --> collection data types 

# x="Hello"
# i=0
# while i<len(x):
#     print(x[i])
#     i+=1

# x="Hello"
# for i in x:
#     print(i)

# x=[11,12,13,14]
# for x in x:
#     print(x)

# s="Good Morning"
# for i in s:
#     print(i,end=" ")

# s=[1,2,3,4,5,6,7]
# for i in s:
#     if i%2==1:
#         print(i , end=" ")
#     # print(i)

# s=['python','snap','chatbot','epson','marker']
# for i in s:
#     if len(i)%2==0:
#         print(i)

    
# t = {1:2,78:900,45:12,67:77}
# for i in t.values():
#     print(i,end=" ")
# print()  
# for i in t:
#     print(t[i],end=" ")
# print()  
# for k in t.items():
#     print(k,end=" ")
# print()   
# for k in t:
#     print(k, t[k])
    

# k="Good day"
# d={}
# for i in k:
#     # print(i,ord(i))
#     # d.update({i:ord(i)})
#     d[i]=ord(i)
# print(d)


# t=[1,True,"abc",3+4j,89.90,[1,2,3],{4,5,6}]
# i=0
# while i < len(t):
#     if isinstance(t[i],(int,float,complex,bool)):
#         print(t[i])
#     i+=1

# for i in t:
#     if isinstance(i,(int , float, complex,bool)):
#         print(i)


    

#SYNTAX 2 

# for var_name in range(start,end/stop,stepvalue/skip):
#<----> statement 
# for i in range(1,10):
#     print(i)

# for i in range(5):
#     print(i)

# for i in range (21):
#     if (i%2==0):
#         print(i,end=" ")

# for i in range (0,21,2):
#     print(i)

# k="python"
# for i in range(len(k)):
#     print(i,k[i])
# 1.wap to print the number form 1 -20 segregate even and odd number into list

# even = []
# odd = []

# for i in range(1, 21):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("Even numbers:", even)
# print("Odd numbers:", odd)

# 2.wap to extract vowels and digits in a string
# y="hello1234"
# for i in y :
#     if i in "aeiouAEIOU" or i.isdigit():
#         print(i)

# 3.wap to capitalize only the first letter of every word in the given list
# l=["vaidegi","rahul","shivam","kapil","patil"]
# for i in l:
#     print(i.capitalize())
    
# 4.wap to extract only individual data types form the list

# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# for i in l:
#     if isinstance(i,(int,float,bool,complex)):
#         print(i)

# 5.wap to extract only individual data types from the list and sum all the individual data types

# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# sum=0
# for i in l:
#     if isinstance(i,(int,float,bool,complex)):
#         print(i)
#         sum+=i
    
# print(sum)

# 6.wap to print the count of alphabets and numbers and space in the given string

# s="india got the independence in the year 1947"
# alpha_count=0
# digit_count=0
# space_count=0
# for i in range(len(s)):
#     if s[i].isalpha():
#         alpha_count+=1
#     elif s[i].isdigit():
#         digit_count+=1
#     elif s[i].isspace():
#         space_count+=1
        
    
# print(alpha_count)
# print(digit_count)
# print(space_count)


# 7.wap to check how many words are present in the given sentence

# s="hello world sentence"
# count=1
# for i in s:
#     if  i.isspace():
#         count+=1
# total_words=0
# for i in s.split():
#     total_words+=1
# print(total_words)
        
# print(f'the number of words in given sentences are {count}')

# 8.wap to create a dictionary and print the characters 
# and its Ascii value pair
# output:--> {"h":ascii value,"e":ascii value........}
# s="hello world"
# d={}
# for i in s:
#     # d.update({i:ord(i)})
#     d[i]=ord(i)
# print(d)

# 9.wap to create a dictionary and traverse into it and if the length is even print as it else reverse it
# output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}
# names=["apple","google","yahoo","microsoft","gmail","walmart"]
# d={}
# for i in names:
#     if len(i)%2==0:
#         d[i]=i
#     else:
#         d[i]=i[::-1]
# print(d)

# 10.wap to print series of factorial(take user input)

# num = int(input("Enter the number of terms: "))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
#     print(f"Factorial of {i} is {fact}")

# 11.wap to create a dictionary with element and its count pair

# l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
# d={}
# for i in l:
#     d[i] =l.count(i)
# print(d)
# output:--> {'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}


# 12.wap to find the length of the string without using inbuilt function
# s="Never Give Up"
# count=0
# for i in range(len(s)):
#     count+=1
# print(f'length of string is {count}')

# 13.wap to reverse a string without using inbuilt function
# x="you did it guys"
# for i in range(1,len(x)+1):
#     print(x[-i],end="")


# x = "you did it guys"
# rev = ""
# for ch in x:
#     rev = ch + rev
# print("Reversed string:", rev)

# 14.wap to print alternative character from a given string
# s="hello python"
# for char in range(0,len(s),2):
#     print(s[char],end="")


#15.wap to create a dictionary index and word pair 
# s="tomorrow is weekend and non-veg special"
# d={}
# for i , j in enumerate(s.split()):
#     d[i]=j
# print(d)
# for i in s.split():
#     count+=1
#     [count]=d[i]

#16.wap to create a dict words and its lenth pair
# s="tomorrow is weekend and non-veg special"
# w={}
# for i in s.split():
#     w[i]=len(i)
#     w.update({i:len(i)})
    
# print(w)


#17.wap to create a dict char and its corresponding upper case chart
# s = "sunday"
# d={}
# for i in s:
#     d[i]=i.upper()
# print(d)

#18.wap to create a dict ascii and char pair

# l = [89,51,111,71,108,120]
# d={}
# for i in l:
#     d.update({i : chr(i)})
#     d[i]=chr(i)
    
# print(d)

#19.wap to create a list of char and its ascii values pair 
# s="sunday"
# l=[]
# for i in s :
#     l.append((i,ord(i)))
# print(l)

# 20.wap to create a dict with letter and its words starting with that letter pair 
# s = "hi hello good morning welcome to python session"
# d={}
# for i in s.split():
#     d.update({i[0]:[i]})
# print(d)

# s = "hi hello good morning welcome to python session"
# d = {}

# for i in s.split():
#     key = i[0]
#     if i[0] not in d:
#         # d[key].append(i)
#         d[i[0]]=[i]
#     else:
#         # d[key] = [i]
#         d[i[0]]+=[i]
        

# print(d)

#23.wap to create a dict of char and its indices pair 

# s="hello python"
# d={}
# # for i in range(len(s)):
# #     if s[i] not in d:
# #         d[s[i]]=[i]
# #     else:
# #         d[s[i]]+=[i]
# # print(d)


# NESTED FOR LOOP 
# syntax ---> for variable in iterable :
            #  <---> for variable in iterable :
                    # <---> statement 
                    
# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in a :
#     # print(i)
#     for j in i:
#         print(j, end = " ")
        
# x=[[1,55,78,100,24,44,12]]
# for i in x:    # First outer loop will execute 
#     for j in i:    # then inner loop will pointing to outer iterable variable 
#         if j%2==0:
#             print(j,end=" ")
    
        
# Q24 wap to create dict word and reverse word pair 

# s = "tommarow is weekend and non-veg special"
# d={}
# for i in s.split():
#     d[i]=i[::-1]
# print(d)
    
#Q25. Reverse a list without using any built in functions and  slicing ( 4 ways)

l=[1,2,3,4]
# for i in range(-1,-5,-1):
#     print(l[i])

# for i in reversed(l):
#     print(i)

# for i in l[::-1]:
#     print(i)

# k=[]
# for i in  l:
#     k=[i]+k
# print(k)

# 1.wap to sum of numbers 
# s='Sony12India567pvt21ltd'
# sum=0
# for i in s:
#     if  i.isdigit():
#         i=int(i)
#         sum+=i
#         continue
# print(sum)

#2.print all the missing numbers from 1 to 10 in the below list 

# l=[1,2,3,4,6,7,10]
# k=[]
# for i in range(1,11):
#     if i not in l:
#         k.append(i)
# print(k)
        
# l=[1,2,3,4,6,7,10]
# for i in range(1,11):
#     if i==l[i-1]:
#         continue
#     print(i)


# Q3. WAP to remove duplicates from the list without using inbuilt function 


# 1.wap to print first and last char of each name in the list
# a=["Sunil","anil","Suresh","Mahesh","Dinesh"]
# b=[]
# for i in a :
#         b.append((i[0],i[-1]))
# print(b)
        
# 2.wap to create a new list as square of each number of below list
# b=[2,4,5,6,7,1]
# c=[]
# for i in b:
#     c.append(i**2)
# print(c)

# 3.wap if number is even the print its square else print its cube

# c=[2,4,5,3,7,9]
# for i in c:
#     if i%2==0:
#         print(i**2, end=" ")
#     else:
#         print(i**3 , end=" ")

# 4.wap to create a list with square and cube of each numbers
# d=[2,4,5,1,8,9,10]
# o/p-->[(4, 8), (16, 64), (25, 125), (1, 1), (64, 512), (81, 729), (100, 1000)]
# l=[]
# for i in d:
#     l.append((i**2,i**3))
# print(l)

# 5.wap to create a new list of reversing each name from the list
# names=["prince","Rekha","Madhu","Sindhu","denga","manga"]
# l=[]
# for i in names:
#     l.append(i[::-1])
# print(l)


# 6.wap to create a new list, of individual and collection data type from list
# data=[20.12,True,[10,20],"super",{1,2},{"a":10},100,(8,9)]
# single_value =[]
# collection_type=[]
# for i in data:
#     if isinstance(i,(int,float,bool,complex)):
#         single_value.append(i)
#     else:
#         collection_type.append(i)
        
# print("single value data types =",single_value)
# print("collection data types = ", collection_type)

# 7.wap to print author name in books dictionary
books={"love story":["Harish",30],"biography":["padam",150],"animals":["vimala",75]}
# for i in books.values():
#     print(i[0])

# for i , j in books.items():
#     print(f"author name of {i} is {j[0]}")
                
# 8.wap to create a dictionary characters and its count pair
# char=["a","M","i","A","M","I","i","H","a","H"]
# d = {}
# for i in char:
#     if i not in d:
#         d.update({i: char.count(i)})
# print(d)

# 9.wap to group fruit name and country pair
# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# p={"Kashmir":"India","America":"us","UK":"Toronto","Africa":"Uganda"}

# a={}
# for i,j in zip(d.keys(),p.values()):
#     a[i]=j
# print(a)


# 10.wap to group fruit name and country pair only if a fruit is even length
# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# a={}
# p={"Kashmir":"India","America":"us","UK":"Toronto","Africa":"Uganda"}
# for i , j in zip(d.keys(),p.values()):
#     if len(i)%2==0:
#         a[i]=j
# print(a)

# 11.wap to sum of same index element from l1,l2,l3
# l1=[10,20,30,40]
# l2=[78,44,11,99]
# l3=[1,2,3,4]

# for i in zip(l1,l2,l3):
#     print(sum(i),end=" ")

# 12.wap to pair values of both dictionary
d={"apple":45,"mango":67,"cherry":90,"berry":23}
p={"Kashmir":"india","America":"us","UK":"Toronto","Africa":"Uganda"}

# a={}
# for i, j in zip(d.values(),p.values()):
#     a[i]=j
# print(a)

# result = list(zip(d.values(),p.values()))
# print(result)

# 13.WAP to print sum of internal and external list
# l = [[1,2,3], [4,5,6], [7,8,9]]
# output:-->
   #internal = 6, 15, 24
   #external --> 45
# internal = []
# for i in l:
#     internal.append(sum(i))
# print("internal =",internal)
# print("external =", sum(internal))

# 14.wap to using this list get the below output

l = ['sun flower', 'Lilly flower', 'Marigold flower', 'lion animal', 'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
# o/p:-->{'flower': ['sun', 'Lilly', 'Marigold', 'lotus'], 'animal': ['lion', 'tiger', 'snake'], 'bird': ['eagle', 'pigeon']}
# d={}
# for i in l:
#     i,j =i.split()
#     if j not in d:
#         l1=[]
#         d.update({j:[l1].append(i)})
#     else:
#         l1.append(i) 
        

output = {}

for item in l:
    word, category = item.split()  # split into two parts
    if category not in output:
        output[category] = []  # create list if category not present
    output[category].append(word)  # add word to correct category list

print(output)


# d={}
# for i in l:
#     print(i.split())
#     d.update({i.split()[1]:i.split()[0]})
#     print(i.split()[0])
# print(d)



      
    





    



              
              
    




