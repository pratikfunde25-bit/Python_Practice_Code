##################################################################################################
#                                           MODULE

# module is nothing but a python file which we import in any other file by using import keyword

#  There are 2 Types of modules :  1) Built-in Module   2) User Defined Module
# USER DEFINED MODULE
# syntax:
# import file_name  (without.py extension)
#       OR
# import file_name as alias
#       OR
# from file_name import function_name 



# along with the syntax we can use the functions ....
#  file_name.function_name()
# or directly ... function_name()


import datetime  
# print(datetime)
# <module 'datetime' from 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.1520.0_x64__qbz5n2kfra8p0\\Lib\\datetime.py'>
print(datetime.datetime.now().year)   #2025
print(datetime.datetime.now().strftime('%Y'))   #2025
print(datetime.datetime.now().strftime('%m'))
