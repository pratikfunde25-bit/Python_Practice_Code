##REVERSED

##ENUMERATE
#  if we want to print both position as well as character without using range funciton

# a="python"
# for i in enumerate(a):
#     print(i)
# print(enumerate(a))  # <enumerate object at 0x000002205A9D9D00>

# print(list(enumerate(a)))



### ZIP inbuilt class

# if we want to match position to position
# in zip inbuilt class we can use all iterable (str,list,tuple,set,dict)
# in zip while passing iterable length should be equal (otw data will be lossed)

# syntax zip(var_name , var_name2 , ...)
# if we directly print this it will show object address
# to avoid obj add we have 2 methods 1. typecast 2. Looping

# a=[1,2,3,4,5]
# b={1,2,3,5,5}
# print(dict(zip(a,b)))


# for i in zip(a,b):
#     print((i))


##ZIP LONGEST - inbuilt class
"""
  From itertools import zip_longest 
  syntax : zip_longest(iterable1, iter2, iter3...)   
    
"""
# from itertools import zip_longest
# a="Good"
# b=[1,2]
# c=(2,2)
# print(list(zip_longest(a,b,c)))
# print(tuple(zip_longest(a,b,c,fillvalue="NR")))
# # print(dict(zip_longest(a,b,c)))

# for i in zip_longest(a,b,c,fillvalue='novalue'):
#     print(i)
    



