#                                       REGULAR EXPRESSION 


# if we want to represent group string according to particular pattern match that time we have to go for the regular exp concept
# it will be working only through string data type 

# step 1  import re 

# ✅ What is a Regular Expression?
# A regular expression (regex) is a sequence of characters that defines a search pattern. 
# It is used for matching strings or parts of strings using a specific pattern.
# In Python, regex is handled by the re module.

# 📦 Importing the Regex Module
import re

# 🔤 Basic Functions in the re Module

# | Function      | Description                                                           |
# | --------------| --------------------------------------------------------------------- |
# | re.match()    | Determines if the RE matches at the **beginning** of the string       |
# | re.fullmatch()| Determines if the RE matches at the full size same  of the string     |
# | re.search()   | Scans through a string, looking for **any location** where RE matches |
# | re.findall()  | Returns a **list** of all non-overlapping matches in the string       |
# | re.finditer() | Returns an **iterator** yielding match objects over all matches       |
# | re.sub()      | Replaces occurrences of the RE with a different string                |
# | re.subn()     | Replaces occurrences of the RE with a different string                |
# | re.split()    | Splits the string by the occurrences of the RE                        |
# | re.compile()  | Compiles a RE into a regex object for repeated use                    |


import re

# match()
# new_var_name = re.match('pattern','source_of_string )
x = 'afternoon'
# y = re.match('ghjk',x)
# print(y)
# y1 = re.match('afternoon',x)
# print(y1)
# y2 = re.match('after',x)
# print(y2)
# print(y2.start())  # 0
# print(y2.end())    # 5
# print(y2.span())   # (0,5)
# print(y2.group())  # after
# print(y2.pos)

# y3 = re.match('a',x)
# print(y3)



# FULLMATCH()
# y2 = re.fullmatch('afternoon',x)   # <re.Match object; span=(0, 9), match='afternoon'>
# print(y2)
# y3 = re.fullmatch('aftern',x)
# print(y3)



# SEARCH ()
# always it will consider the first occurance of pattern substring if no match returns none 

# new_var_name = re.search('pattern',source_string)
# y1 = re.search('a;sldkjf',x)   
# print(y1)   # None

# y2 = re.search(64535,x)   #  TypeError: first argument must be string or compiled pattern
# print(y2)

# y3 = re.search('n',x)
# print(y3)   # <re.Match object; span=(5, 6), match='n'>

# y4 = re.search('after',x)
# print(y4)
# print(y4.start())
# print(y4.end())



# Finditer() 

# new_var_name = re.finditer('pattern',source)

# w = re.finditer('o',x)
# print(w)  # <callable_iterator object at 0x0000018724D26D40>
# print(list(w))
# for i in w :
#     print(i)
    
    
# SUB()

# t = re.sub('n','***',x,1000)   # return type string 
# print(t)

# t1 = re.sub('n','***',x,1)
# print(t1)


# SUBN()

# s1= re.subn('n','***',x,1000)    # return type tuple
# print(s1)

# s2= re.subn('n','***',x,1)    # return type tuple
# print(s2)


# SPLIT()

# n_var = re.split('pattern','source)    # return type will be list

# a='good morning'
# r = re.split('o',a)
# print(r)


# FINDALL()

# new_var = re.findall('pattern',source of string)
w = 'HeLlo PYThOn054'
q = re.findall('[A-Z]',w)
print(q)  # ['H', 'L', 'P', 'Y', 'T', 'O']

q1 = re.findall('[a-z]',w)
print(q1)  # ['e', 'l', 'o', 'h', 'n']

q2 = re.findall('[A-Za-z]',w)
print(q2)  # ['H', 'e', 'L', 'l', 'o', 'P', 'Y', 'T', 'h', 'O', 'n']

q3 = re.findall('[a-zA-Z0-9]',w)
print(q3) # ['H', 'e', 'L', 'l', 'o', 'P', 'Y', 'T', 'h', 'O', 'n', '0', '5', '4']

q5 = re.findall('[0-9]',w)
print(q5)   # ['0', '5', '4']
q4 = re.findall(r'\d',w)
print(q4)  # ['0', '5', '4']

q6 = re.findall('\D',w)   # D -- apart from the number everything it will give the  output as match
print(q6)  # ['H', 'e', 'L', 'l', 'o', ' ', 'P', 'Y', 'T', 'h', 'O', 'n']


q7 = re.findall(' ',w)
print(q7)  # [' ']


q8 = re.findall('\s',w) # \s --- it will consider the only the white spaces
print(q8) # [' ']

q9 = re.findall('\S',w)  # \S --- apart from white space it will consider all 
print(q9)










#  🧱 Basic Regex Syntax

# 🔹 Metacharacters

# |Character| Description                                |             |
# | --------| -----------------------------------------  | ----------- |
# | .       | Any character except newline               |             |
# | ^       | Beginning of string                        |             |
# | $       | End of string                              |             |
# | *       | 0 or more repetitions                      |             |
# | +       | 1 or more repetitions                      |             |
# | ?       | 0 or 1 repetition (optional)               |             |
# | {n}     | Exactly n repetitions                      |             |
# | {n,}    | At least n repetitions                     |             |
# | {n,m}   | Between n and m repetitions                |             |
# | []      | Set of characters                          |             |
# | \        | \                                         | OR operator |
# | ()      | Grouping                                   |             |
# | \       | Escape special characters or use sequences |             |





# 🔢 Special Sequences

# |Sequence| Description                        |
# | -------| ---------------------------------- |
# | \d     | Digit (0–9)                        |
# | \D     | Not a digit                        |
# | \w     | Word character (a-z, A-Z, 0-9, \_) |
# | \W     | Non-word character                 |
# | \s     | Whitespace character               |
# | \S     | Non-whitespace character           |
# | \b     | Word boundary                      |
# | \B     | Not a word boundary                |
# | \\     | Backslash character                |



# 🎯 Character Sets and Ranges
# [abc]: Matches either 'a', 'b', or 'c'
# [a-z]: Matches any lowercase letter
# [A-Z]: Matches any uppercase letter
# [0-9]: Matches any digit
# [^a-z]: Negation — any character except lowercase letters


# 🧪 Raw Strings in Python Regex
# To avoid escaping backslashes, use raw strings (r'...'):
# #Without raw string
# re.search("\\\\", "\\")

# # With raw string
# re.search(r"\\", "\\")



    
    
    









