x=[11,12,13,14,15,16,17]
# x=[1,2,3,3,4,5,5,6,7,7,7]
# key=14
# # key=150
# def Binary_search(x,key):
#     li=0
#     hi=len(x)-1
#     while li<=hi:
#         mid = (li+hi)//2
#         if key==x[mid]:
#             return f'key is present at index {mid}'
#         elif key>x[mid]:
#             li=mid+1
#         elif key<x[mid]:
#             hi=mid-1
#     return 'key is not present in the collection'
# print(Binary_search(x,key))




##################### BUBBLE SORT ########################
# l=[20,10,30,15,25,50]
# def Bubble_sort(l):
#     for i in range(1,len(l)):
#         for j in range(0,len(l)-i):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1] = l[j+1],l[j]
#     return l

# print(Bubble_sort(l))



###########################  SELECTION SORT  ##################################
# l=[3,7,10,1,2]
# def Selection_sort(l):
#     for i in range(1,len(l)):
#         minpos=i-1
#         for j in range(i,len(l)):
#             if l[minpos]>l[j]:
#                 minpos=j
#         l[i-1],l[minpos]=l[minpos],l[i-1]
#     print(l)
        
# Selection_sort(l)
        
        

