# num=int(input("enter a number :"))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
        
# if count==2:
#     print(f'{num} is prime number ')
# else:
#     print(f'{num} is not prime number')


# num=int(input("enter a number :"))
# for i in range(2,num):
#     if num%i==0 :
#         print(f'the number {num} is not a prime number')
#         break
# else:
#     print(f'the number {num} is a prime number')


# st=input(("enter a string :"))
# rev=''
# for i in st:
#     rev=i+rev
# print(rev)

# num=int(input("enter a number :"))
# rev=0
# rem=0
# while num >0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
    
# print(rev)


# n=int(input("enter the number of rows in patterns :"))
# for i in range(n):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print()

# n=int(input("enter the number of rows in patterns :"))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()


# n=int(input("enter the number of rows in patterns :"))
# for i in range(n):
#     for j in range(65,65+n):
#         print(chr(j),end=" ")
#     print()


# n=int(input("enter the number of rows in patterns :"))
# count=0
# for i in range(n):
#     for j in range(n):
#         count+=1
#         print(count,end=" ")
#     print()


# n=int(input("enter the number of rows in patterns :"))
# for i in range(n):
#     for j in range(1,n+1):
#         print(i*n+j,end=" ")
#     print()

# n=int(input("enter the number of rows in patterns :"))
# for i in range(n):
#     for j in range(65,n+65):
#         print((chr(i*n+j)),end=" ")
#     print()

# n=int(input("enter the number of rows in patterns :"))
# for i in range(1,n+1):
#     for j in range(i):
#         print('*',end=" ")
#     print() 

# n=int(input("enter the number of rows in patterns :"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print() 
    
#  OUTPUT   --->
# 1 
# 1 2
# 1 2 3
# 1 2 3 4


# n=int(input("enter the number of rows in patterns :"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()
# 1 
# 2 2
# 3 3 3
# 4 4 4 4



# n=int(input("enter the number of rows in patterns :"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(64+i),end=" ")
#     print()
# A 
# B B
# C C C
# D D D D


# n=int(input("enter the number of rows in patterns :"))
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print() 
# 1 
# 2 1
# 3 2 1
# 4 3 2 1

# n=int(input("enter the number of rows in patterns :"))
# count=0
# for i in range(n):
#     for j in range(i+1):
#         count+=1
#         print(count,end=" ")
#      print()
# 1 
# 2 3
# 4 5 6
# 7 8 9 10

# n=int(input("enter the number of rows in patterns :"))
# count=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(64+count),end=" ")
#         count+=1
#     print()
# A
# B C
# D E F
# G H I J

# n=int(input("enter the number of rows in patterns :"))
# count=1
# for i in range(1,n+1):
#     for j in range(64+i,64,-1):
#         print(chr(j),end=" ")
#         count+=1
#     print()
# A 
# B A
# C B A
# D C B A

# n=int(input("enter the number of rows in patterns :"))
# for i in range(1,n+1):
#     for j in range(i-1):
#         print(" " ,end=" ")
#     for k in range(n-i+1):
#         print(i,end=" ")
#     print()
# 1 1 1 1 
#   2 2 2
#     3 3
#       4

# n=int(input("enter the number of rows in patterns :"))
# for i in range(n):
#     for j in range(i):
#         print(" " ,end=" ")
#     for k in range(1,n-i+1):
#         print(k,end=" ")
#     print()
# 1 2 3 4 
#   1 2 3
#     1 2
#       1


# n=int(input("enter the number of rows in patterns :"))
# for i in range(n):
#     for j in range(i):
#         print(" " ,end=" ")
#     for k in range(n-i):
#         print(i+1,end=" ")
#     print()
# 1 1 1 1 
#   2 2 2
#     3 3
#       4


# n=int(input("enter the number of rows in patterns :"))
# for i in range(n):
#     for j in range(i):
#         print(" " ,end=" ")
#     for k in range(n-i):
#         print(chr(i+65),end=" ")
#     print()
# A A A A 
#   B B B 
#     C C 
#       D 


# n=int(input("enter the number of rows in patterns :"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     for l in range(i-1,0,-1):
#         print(l,end=" ")
#     print()
#       1 
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1


# n=int(input("enter the number of rows in patterns :"))
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1):
#         print("*",end=" ")
#     for l in range(i+(n-1)):
#         print(" ",end=" ")
#     for m in range(1):
#         print("*",end=" ")
#     print()

# n = int(input("enter the number of rows in patterns :"))
# for i in range(n):
#     print(" " * (n - i - 1)*2 , end=" ")
#     for j in range(2 * i + 1):
#         if j==0 or j==2*i:
#             print('*',end=" ")
#         else:
#             print(' ',end=" ")

#     print()      

# # Lower half
# for i in range(n - 2, -1, -1):
#     print(" " * (n - i - 1) * 2, end=" ")  # Leading spaces
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2 * i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
    
    
    
# n = int(input("Enter the number of rows: "))

# # Upper half
# for i in range(1, n + 1):
#     print("* " * i + "  " * (n - i) * 2 + "* " * i)

# # Lower half
# for i in range(n, 0, -1):
#     print("* " * i + "  " * (n - i) * 2 + "* " * i)





# n = int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print("* " * i+"  " *(n-i)*2+"* "* i)
# for i in range(n,0,-1):
#     print("* " * i+"  " *(n-i)*2+"* "* i)
# *             * 
# * *         * *
# * * *     * * *
# * * * * * * * *
# * * * * * * * *
# * * *     * * *
# * *         * *
# *             *

















        
    
    






    
        