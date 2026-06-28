                        # 🐍 Python Error & Exception Handling – Beginner to Advanced
                        
# 📌 1. Introduction to Errors in Python

# Python has two types of issues:
# 1. Syntax Errors (Parsing errors),(compile time error)
# These are detected before code runs at compilation time .
# print("Hello"  # SyntaxError: unexpected EOF while parsing   '(' was never closed




# 2. Exceptions (Runtime Errors)
# These are raised during execution.
# x = 5 / 0  # ZeroDivisionError: division by zero



# | Exception Name      | Description                     |
# | ------------------- | ------------------------------- |
# | `ZeroDivisionError` | Division by zero                |
# | `TypeError`         | Operation on incompatible types |
# | `ValueError`        | Invalid value                   |
# | `IndexError`        | Index out of range              |
# | `KeyError`          | Dict key not found              |
# | `FileNotFoundError` | File not found                  |
# | `AttributeError`    | Attribute not found             |
# | `ImportError`       | Module can't be imported        |
# | `NameError`         | Variable not defined            |
# | `IOError`           | I/O operation failed            |



# 📌 3. Basic Exception Handling
# Using try-except

# try:
#     x = int(input("Enter a number: "))
#     result = 10 / x
# except ZeroDivisionError:
#     print("You cannot divide by zero.")
# except ValueError:
#     print("Invalid input. Enter a number.")
    
# 📌 4. Using else, finally

# try:                                                                # always it will execute first try block 
#     x = int(input("Enter a number: "))
#     result = 10 / x
# except ZeroDivisionError:                                           # when it will be zero division error it will execute this except block 
#     print("Cannot divide by zero.")
# else:                                                               # when there is no error it will execute else block 
#     print(f"Result is {result}")
# finally:                                                            # it will be always executed whether the error will raised or not 
#     print("This will run no matter what.")


# 📌 5. Catching Multiple Exceptions

# try:
#     # some code
#     x = int(input("Enter a number: "))
#     result = 10 / x
# except (ValueError, TypeError) as e:
#     print(f"Error occurred: {e}")



# try:
#     x = 0
#     result = 10 / x
# except Exception as e:
#     print(f"{type(e).__name__}: {e}")

# 📌 6. Using Exception Object

# try:
#     x = 0
#     result = 10 / x
#     # risky code
# except Exception as e:
#     print(f"Exception: {e}")

# 📌 7. Raising Exceptions Manually

# def set_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative BRO...")
#     print(f"Age is {age}")
# set_age(-20)


# 📌 8. Custom Exceptions (Advanced)

# class NegativeAgeError(Exception):
#     pass

# def set_age(age):
#     if age < 0:
#         raise NegativeAgeError("Negative age not allowed")

# try:
#     set_age(-5)
# except NegativeAgeError as e:
#     print(e)


# 📌 9. Exception Chaining (raise ... from)

# try:
#     int("abc")
# except ValueError as e:
#     raise RuntimeError("Failed to convert string") from e


# 📌 10. Logging Exceptions (Best Practice in Industry)

 
# import logging

# logging.basicConfig(filename='app.log', level=logging.ERROR)

# try:
#     1 / 0
# except ZeroDivisionError as e:
#     logging.error("ZeroDivisionError occurred", exc_info=True)


# 📌 12. Exception Handling in Loops

# data = ["5", "0", "ten", "3"]

# for val in data:
#     try:
#         result = 10 / int(val)
#     except ZeroDivisionError:
#         result = 0
#     except ValueError:
#         result = -1
#     print(result)



# 📌 13. Real-World Use Cases
# ✅ 1. Web Scraping (Requests/BeautifulSoup)


# import requests

# try:
#     response = requests.get('https://example.com', timeout=5)
#     response.raise_for_status()
# except requests.exceptions.Timeout:
#     print("Request timed out.")
# except requests.exceptions.HTTPError as err:
#     print(f"HTTP error: {err}")



# ✅ 2. File Handling in Data Pipelines
# def load_file(path):
#     try:
#         with open(path, 'r') as f:
#             return f.read()
#     except FileNotFoundError:
#         return "File not found."
# print(load_file('pratik.....txt'))


# ✅ 3. Database Operations

# import sqlite3

# try:
#     conn = sqlite3.connect('data.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM users')
# except sqlite3.DatabaseError as e:
#     print(f"DB error: {e}")
# finally:
#     conn.close()


# ✅ 4. Machine Learning Pipelines
def preprocess(data):
    if not isinstance(data, list):
        raise TypeError("Data must be a list")
    # further steps



# 📌 14. Best Practices in Exception Handling (Used in Industry)
# ✅ Catch specific exceptions
# ✅ Use finally for cleanup
# ✅ Avoid bare except: unless absolutely necessary
# ✅ Use logging instead of print
# ✅ Don't silence exceptions (e.g., empty except blocks)
# ✅ Validate data before risky operations
# ✅ Raise exceptions where appropriate in your libraries
# ✅ Chain exceptions when re-raising (raise from)
# ✅ Use retry mechanisms (e.g., with APIs)


# 📌 16. Exception Hierarchy (Simplified)

# BaseException
#  ├── SystemExit
#  ├── KeyboardInterrupt
#  ├── Exception
#       ├── ArithmeticError
#       │    ├── ZeroDivisionError
#       ├── LookupError
#       │    ├── IndexError
#       │    ├── KeyError
#       ├── ...


# 📌 17. Tools to Monitor Exceptions in Production
# | Tool          | Purpose                         |
# | ------------- | ------------------------------- |
# | **Sentry**    | Real-time error tracking        |
# | **New Relic** | Application performance monitor |
# | **Logstash**  | Collect & analyze logs          |
# | **Datadog**   | Monitoring + alerting           |


# ✅ 1. What is assert?

# assert is used to test if a condition is True, and if not, it raises an AssertionError.
# assert condition, "Optional error message"

# If condition is False, Python raises
# AssertionError: Optional error message


# ✅ 2. Basic Example
# x = -5
# assert x > 0, "x must be positive"
# # # AssertionError: x must be positive

# def process_data(data):
#     assert isinstance(data, list), "Data must be a list"
#     assert len(data) > 0, "Data list cannot be empty"
#     # process data

# process_data((1,2,3,4))  # data must be a list

# 📌 4. Full Example: Custom Exceptions in a Program
# class InvalidEmailError(Exception):
#     pass

# def validate_email(email):
#     if "@" not in email:
#         raise InvalidEmailError("Email must contain '@'")

# try:
#     validate_email("pratikgmail.com")
# except InvalidEmailError as e:
#     print(f"Invalid email: {e}")


# 📌 6. Real-World Use Case: Banking System
# class InsufficientBalanceError(Exception):
#     pass

# def withdraw(balance, amount):
#     if amount > balance:
#         raise InsufficientBalanceError("Not enough balance")
#     return balance - amount

# try:
#     balance = withdraw(1000, 1500)
# except InsufficientBalanceError as e:
#     print("Transaction failed:", e)























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





# Try block -----> Except Block -----> Else Block -----> Finally Block 

# if there is any error in try block code always it will go for except block execution 
# and if there is no error handled in except block then always it will execute the else block 
# if there is error handled in except block then else block will never executed

#  Finally block is always executed whether there is any error handled or not by any block 


# if there is no error found else block will be executed and finally block will also executed 




