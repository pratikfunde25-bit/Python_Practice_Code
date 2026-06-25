##########################################################################################
# 1.List Comprehension
# 2.Set  Comprehension
# 3.Dict Comprehension


# s = [12,45.67,True,False,"hii",[1,2,3],{3,4,5}]
# l=[]
# for i in s :
#     (l.append(type(i)))
# print(l)

# print([type(i) for i in s])

# 1.wap to check even numbers in a list and return a list containing only even numbers

# l=[2,32,1,52,31,24,56,75]
# print([i for i in l if i%2==0])

# 2.wap to check elements inside the collection are even or odd,if it is even
# make it square of that numbers,if it is odd make it as cube of that numbers

# l=[2,3,5,1,7,2,3]
# print([i**2 if i%2==0 else i**3 for i in l] )


# 3.wap to return a list containing 10 multiples of 2
# print([i*2 for i in range(1,11)])

# 4.wap to return a list containing 10 multiples of given value(take user input)

# num = int(input("enter the number :"))
# print([i*num  for i in range(1,11)])

# 5.wap to take two lists as input and add that elements and return a single lists

# l1 = eval(input("enter first list :"))
# l2 = eval(input("enter second list :"))
# print([l1[i]+l2[j] for i in range(len(l1)) for j in range(len(l2))])
# print([i+j for i,j in zip(l1,l2)])

# 6.wap to create a list containing tuples having two elements that is index and value of list
# a=[10,20,30,40]
# l=["hey","hello","good","evening","python"]
# print([(i,l[i]) for i in range(len(l))])

# 7.wap to check length of strings present in tuple,if length is even append as it is ,else reverse it and append

# l=("hey","hello","good","evenings","python")

# print([i if len(i)%2==0 else i[::-1] for i in l])



# set comprehension example

# 1.wap to remove repeated values and return in set
# l=[2,3,4,2,5,6,2,3]
# print({i for i in l})

# 2.wap to take two lists and return a set by adding elements present same index

# l1=[2,3,4,5,6,7,8,9]
# l2=[5,6,7,8,9,1,2,3]

# print({i+j for i,j in zip(l1,l2)})



#    Dict comprehensions

# 1.wap to create a dictionary keys by taking from list,values are square of that key

# l=[2,3,4,1,6,2,7,8,4]

# print({i : i**2 for i in l})

# 2.wap to create a dictionary of values and index pair

# l=["google","apple","python","orange"]

# print({i :l[i] for i in range(len(l))})

# 3.wap create a dictionary having first char of word and word pair if word having even length

# l=["google","apple","python","orange"]

# print({i[0]:i for i in l if len(i)%2==0})

# 4.wap to check length of words and create a dict
# having word and word pair if it is even odd as it is else reverse 

# l=["google","apple","python","orange"]

# print({i:i if len(i)%2==0 else i[::-1] for i in l})

# 5.wap to check elements is palindrome key and value should be same else value is reverse of key

# l=["banana","malayalam","madam","sir","mom","dad"]

# print({i:i if i==i[::-1] else i[::-1] for i in l})




s = ['python','walmart','snap','whatsapp','back','space','hi']
#  wap to print all the element in the inside tthe list

print([i for i in s])
# ['python', 'walmart', 'snap', 'whatsapp', 'back', 'space', 'hi']


#  wap to print only odd length element inside the list
print([i for i in s if len(i)%2==1])



# wap to print  if it is odd length reverse it else print as it is inside the list
print([i[::-1] if len(i)%2==1 else i for i in s ])





