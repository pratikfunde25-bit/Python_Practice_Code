# File handling is an essential part of Python programming used to read, write, and manipulate files on disk (text, binary, etc.).
# Python uses built-in functions for file operations via the open() function.



# getcwd ()
# chdir ()
# mkdir()
# rmdir()
# remove()
# listdir()
# popen()
# rename()


#                                                File Handling 


# 📁 1. What is File Handling?
# File handling allows a program to read from and write data to files on the disk.
# It is useful for:
# Storing data permanently.
# Reading input from files.
# Logging, configuration files, databases, etc.


# 📄 2. Types of Files
# Text Files: Store data in human-readable format. Example: .txt, .csv
# Binary Files: Store data in binary (non-readable) format. Example: .jpg, .exe, .mp3


# 🧩 3. Basic File Operations
# Open a file
# Read from a file
# Write to a file
# Close a file

# 🪟 4. Opening a File
# Use the built-in open() function:

# Without Context Manager
# new_varname = open('file_name','mode')
# in this type we have to close our file manually by using close function

# | Mode| Description                                |
# | ----| ----------------------------------------   |
# | 'r' | Read (default). File must exist.           |
# | 'w' | Write. Creates a new file or overwrites.   |
# | 'a' | Append. Adds to file if exists.            |
# | 'x' | Create. Fails if file exists.              |
# | 'b' | Binary mode (e.g. 'rb', 'wb')              |
# | 't' | Text mode (default)                        |
# | '+' | Read and write ('r+', 'w+')                |


# Create a File 
# file = open('space.txt','r')
# print(file.mode)   # r
# print(file.name)   #space.txt
# print(file.closed) #False
# print(file.fileno()) # 3
# print(file.readable()) # False
# print(file.writable()) # True
# print(file.close())  # None
# print(file.closed)  # True 

# reading Operation
# 1) readline()  2) readlines()  3) read(n)   4) read()

# 📖 5. Reading from a File
# Assume we have a file example.txt:
# Hello World
# Welcome to Python


# a. Read entire file:
# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()

# b. Read line by line:
# file = open("example.txt", "r")
# line1 = file.readline()
# line2 = file.readline()
# print(line1,line2,sep='')
# file.close()

# c. Read all lines into a list:
# file = open("example.txt", "r")
# lines = file.readlines()
# for line in lines:
#     print(line.strip())
# file.close()




# ✍️ 6. Writing to a File
# a. Using 'w' (Overwrites):
# file = open("output.txt", "w")   # if file is not exists new file will create automatically 
# file.write("Hello, this is written to a file.\n")
# file.close()

# b. Using 'a' (Appends):
# file = open("output.txt", "a")
# file.write("This line will be added.\n")
# file.close()



# ✅ 7. Best Practice: Using with Statement
# Automatically closes the file, even if error occurs


# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)


# 🔄 8. Read and Write in One Go (r+, w+, a+)
# Example: r+ (Read and write, file must exist)

# with open("example.txt", "r+") as file:
#     data = file.read()
#     file.write("\nAppended line")

# Example: w+ (Write and read, file is overwritten)
# with open("example.txt", "w+") as file:
#     file.write("New content")
#     file.seek(0)
#     print(file.read())








# print(file.read())    # io.UnsupportedOperation: not readable  when we use (w mode ) -- whole file data will be printed  (without blank lines )
# print(file.readline())  # i 
# print(file.readline())  # am pratik
# print(file.readline())  # my name is pratik  ( after every output one blank line is there)
# print(file.readline()) # empty line 
# print(file.read())  # empty line
# print(file.read())  # empty line 


# print(file.readline(100))  # first 100 characters of first line will be printed
# print(file.readline(5))   # first 5 characters of second line will be printed
# print(file.readline())   # remaining characters of second line will be printed without blank line gap
# print(file.readline(2))  # first 2 chars of third line 
# print(file.readline(5))
# print(file.readline())

# print(file.readlines(3)) #['i \n', 'am pratik\n'] 
# print(file.readlines())  # ['my name is pratik.']


# print(file.read(15))  # char by char it will display the data 
# print(file.read(10))  
# print(file.read(10))

# print(file.buffer)  # <_io.BufferedWriter name='space.txt'>


# With Context Manager
# with open ('file_name','mode') as file:
#       pass
# in this type we dont have to close our file manually file will be closed automatially 










import os 
# print(os.getcwd())   # if we want to know the current location 
# print(os.chdir(r"C:\Users\Pratik\Desktop\Python Coding Prabhu Sir Class\Python day one 1"))  # to move from one loc to another to change the dir  
#  it will throw the unicode error we can avoid this error by 2 ways:
# 1) raw string  (r "path" or R "path")
# 2) double slash (\\ insted of \ ) both the ways avoid the special sequence code ( odd slash speical sequence & even slash normal way)
# print(os.getcwd())



# os.mkdir('pratik') # to create a new directory   [ when we dont comment this line or created another one again it will throw fileExitsError :]


# os.mkdir('pratik.txt') # again it will create a pratik.txt folder inside the main directory
# print(os.listdir())  #['composition_uml', 'inheritance_ questions.txt', 'my_filess', 'one.pkl', 'pratik', 'pratik.txt', 'Python day one 1']


# os.rmdir("pratik.txt")   #OSError: [WinError 145] The directory is not empty: 'pratik.txt'  ( because this folder is not empty ) it removes only blank dir folders
# os.rmdir('pratik')
# os.remove("pratik")   # by using folder deletion PermissionError: [WinError 5] Access is denied: 'pratik'
# os.remove('my_filess')  # to remove the particular file from the directory or folder 


# os.rename("pratik.txt",'akash')   # to rename the folder in directory 
# os.rename('one.pkl','two.pkl')      # to rename the file in directory 
# os.rename('composition_uml','pratik')  # to rename the only file with another file
# os.rename('pratik','pratik.txt')      # to rename and to convert the file into another file name or file format 




# print(os.chdir(r'D:\OS'))
# print(os.getcwd())
# print(os.getcwd())
# print(os.rmdir('pratik'))
# print(os.remove('pratik.txt.txt'))
# print(os.remove('new file.txt'))
# print(os.rename('new Text document.txt','my_file.txt'))
# print(os.rename('NEw FILE.txt','my_fileSS.txt',))
# print(os.listdir())
# os.popen('my_filess.txt') #open the file
# os.popen('python day one 1')  #error

# Without Context Manager (syntax --->)
# var_name = open('file_name','mode')

# file = open('my_filess','w')

# print(file.name)
# print(file.mode)
# print(file.writable())
# print(file.readable())
# # file.close()
# print(file.closed)
# print(file.writable())






# *********************************

# file = open('my_filess')
# print(file.read())
# print(file.readline()) # 1st line printed  -->good morning guys
# print(file.readline()) # 2nd line printed new line  --> welcome to python session
# print(file.readlines())  #['Room number - 6\n', 'Total count of the class - 60'] all lines in list format
# print(file.read(4))  # number of characters read from start ---> good

# file = open("think",'r')  # new file created if not exists in writable mode
# print(file.write("python class"))
# print(file.write("programming "))
# print(file.write("hello world!")) # everything will be overwrite new data is inseerted previous is deleted
# file.writelines(['pratik funde\n','pratik f','pratik']) #pratik funde \n pratik fpratik(pre delted data)
# file.write("java Class") # by usingg append new data is add in previous no loss 
# print(file.read())   



# ****************************  With using context manager method  ********************************

# with open ('think','r') as x:
#     print(x.read())
    
# print(x.closed)  # file is closed automatically when out of the operations 


# csv file handling 

# ✅ What is a CSV File?
# CSV stands for Comma-Separated Values.
# It stores tabular data (like spreadsheets) in plain text format.
# Each line in the file is a row, and values are separated by commas (,).

# 1.writer() 2)Dictwriter()


import csv
# step 1 -create a file 
# with open('data.csv', mode='x') as file:
#       ...

# step 2 - 
# with open('data.csv') as file:
#       ...
# os.popen('data.csv')   # we have to manually close the file 

# step 3 -
# Reading text files safely
# with open("data.csv", mode="r", encoding="utf-8", newline="") as f:
#     ...

# # Writing safely (overwrite)
# with open("out.csv", mode="w", encoding="utf-8", newline="") as f:
#     ...

# # Appending
# with open("out.csv", mode="a", encoding="utf-8", newline="") as f:
#     ...


# with open('data.csv','w',newline='') as file:
#       new = csv.writer(file)
      # new.writerow(['python','sql','java','deccan'])
      # new.writerow([['pratik'],['akash'],['priti']])
      # new.writerows([['pratik'],['akash'],['priti']])  # one by one line wise come but sinlge line gap 
      # new.writerows([['pratik','funde'],['akash','funde'],['priti','gite']])   # to avoid that line break we use the newline parameter in open function
      # os.popen('data.csv')


# with open('data.csv','r',newline='') as file:
#       new = csv.reader(file)
#       for i in new:
#             print(i)


# import csv

# fieldname = ["name", "age", "city"]

# with open("data.csv", "w", newline="") as file:
#     dw = csv.DictWriter(file,fieldname)
#     dw.writeheader()
#     dw.writerow({"name": "Pratik", "age": 22, "city": "Pune"})
#     dw.writerows([
#         {"name": "Anita", "age": 28, "city": "Mumbai"},
#         {"name": "Ravi", "age": 31, "city": "Nashik"}
#     ])
# os.popen('data.csv')



# import csv

# with open("data.csv", "r",  newline="") as f:
#     dr = csv.DictReader(f)           # keys from header row
#     for row in dr:                   # row is an OrderedDict-like mapping
#       #   print(row)
#         if int(row["age"]) > 30:
#             print(row["name"], row["city"])



# from collections import deque
# with open('output.txt','r') as file:
#       new = deque(file,1)   # this function will print the lines by reverse format last line to first line depend on no we pass ( last 5 lines will be printed) # deque([], maxlen=0) in 0 format
#       print(new)

# from itertools import islice
# with open('output.txt','r') as file:
#       new1 = islice(file,1)
#       # print(new1)   #  <itertools.islice object at 0x000001ECFAE19CB0>
#       print(list(new1))
#       for i in new1:
#             print(i)




# with open('output.txt','r') as file:
#       print(file.tell())        # used to get the current position of the cursor  ( 0 )
#       print(file.readline(),end='')   # first line will be read fully   
#       print(file.tell())        # end of first line (35)
#       file.seek(4)              # used to navigate the position of the cursor to that number(4)
#       print(file.tell())        # get current position (4)   
#       print(file.readline())    # now the lines will be read or printed from position 5 inclusive 
#       # This is due to print() adding a newline, and readline() returning a line with a newline already. So you get a double newline effect

#                                                      Collection MOdule 


# from collections import deque
# x = deque([1,2,3,4,4,5])
# print(x)
# x.rotate(0) # when we use 0 no rotation will happen
# print(x)
# x.rotate(-2)  # when we use -ve number it will rotate from left these numbers (n)
# print(x)
# x.rotate(2)  # when we use +ve number it will rotate from right these numbers (n)
# print(x)





#####################  EXCEPTION HANDLING   ####################

# l = [1,2,3]
# # print(l[3])
# try:
#     print(l[3])
# except:
#     print("Index Error handled ....")





    
    
# try :
#     with open('new.txt','r') as file:
#         print(file.read())
# except:
#     print('FileNotFoundError Handled ....!')
    
# in except block there are 4 types 
# 1. Default  --> when we dont know what type of the error will happen then go for default exception handling 
# 2. Specific --> when we know the error type we specifically mention the name of the error 
# 3. Multiple --> by using single try block we can execute multiple except block 
# 4. Generic -->  
  
  
  
# 1. Default Error handling 

# try:
#       a = [1,2,3,4,5] 
#       print(a.upper())   # AttributeError: 'list' object has no attribute 'upper'
# except:
#       print("Error Handling ...")

# 2. Specific Error handling 

# try:
#       a = [1,2,3,4,5] 
#       print(a.upper())   # AttributeError: 'list' object has no attribute 'upper'
# except AttributeError:
#       print("Error Handling ...")
      



# 3 Multiple error hanlding 

# Syntax 1:
# try:
#       errorline
      
# except Error_name :
#       statement 
# except Error_name :
#       statement 
# except Error_name :
#       statement 


# Syntax 2:
# try:
#      errorline
# except Error_name1 , Error_name2, error_name3 , Error_name 4 ... Error_name N :
#      statement 

# we cant handle IndentationError and SyntaxError in Python 



# try:
#       r={34:56,78:89,89:99}
#       print(r[340])
# except TypeError:
#       print("type error handled")
# except AttributeError:
#       print("Attribute error handled")
# except SyntaxError:
#       print("Syntax Error handled" )    #  SyntaxError: ':' expected after dictionary key   
# except KeyError :
#       print("key error is handled by me pratik")   # ouput line 
      
      
      
# try:
#       r={34:56,78:89,89:99}
#       print(r[340])
# except (TypeError , NameError , ZeroDivisionError , AttributeError,FileNotFoundError,KeyboardInterrupt,KeyError):
#       print('error is handling ')
      
      

  
# 4. Generic Error handling 

# here we can handled all types of the errros 
# if we want to know why this type of error occured reason then we go for the Generic Error handling 


# try:
#       a = [1,2,3,4,5] 
#       print(a.upper())   # AttributeError: 'list' object has no attribute 'upper'
# except Exception as msg:
#       print("Error Handling ...")
#       print('msg')  
#       print(msg)   # 'list' object has no attribute 'upper'  
      
      
# try:
#       a = [1,2,3,4,5] 
#       print(a.upper())   # AttributeError: 'list' object has no attribute 'upper'
# except BaseException as msg:
#       print("Error Handling ...")
#       print('msg')  
#       print(msg)   # 'list' object has no attribute 'upper' 
      
      








