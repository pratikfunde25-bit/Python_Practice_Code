# Pattern
# 1.Solid           2.Hollow

    # for i in  range()(no of rows)
    #   for j in range()(no of columns)
    
    
# for i in range(1,3):  # rows 2
#     for j in range(1,6): # column 5
#         print('*' , end=" ")
#     print()


# n=int(input("enter number of rows and columns:"))
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print('*',end=" ")
#         else:
#             print( ' ' , end=" ")
#     print()

# n=int(input("enter number of rows and columns:"))
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print('*',end="")
#         else:
#             print( ' ' , end="")
#     print()



# n=int(input("enter number of rows and columns:"))
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1 or i==j:
#             print('*',end="")
#         else:
#             print( ' ' , end="")
#     print()


# n=int(input("enter a number :"))
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

n=int(input("enter a number :"))
for i in range(n):
    for j in range(n):
        if i<=j or i+j<=n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



