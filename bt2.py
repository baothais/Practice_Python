# 01
# def maxSumOfBeautifulSubarray(arr):
#     l1=[]
#     for i in range(len(arr)):
#         s=0
#         for j in range(i, len(arr)):
#             s += arr[j]
#             l1.append(s)
#     for i in range(-len(arr), -1):
#         s=0
#         for j in range(i, -1):
#             s+=arr[j]
#             l1.append(s)
#
#     print(l1)
#     l2 = [i for i in list(set(l1)) if i%9==0]
#     if l2==[]:
#         return -1
#     return max(l2)
#
# if __name__=="__main__":
#     print(maxSumOfBeautifulSubarray(arr=[-3,5,-4,7]))
# from itertools import chain, combinations
# def maxSumOfBeautifulSubarray(arr):
#     return chain.from_iterable(combinations(arr, n) for n in range(len(arr)+1))
# print(list(maxSumOfBeautifulSubarray([-3, -4, 5, 7])))
# l2 = [i for i in l1 if i%9==0]
# if l2==[]:
#     print(-1)
# else:
#     print(max(l2))
# def reverseStringBase(str):
#     l=[]
#     for i in range(len(str)):
#         if str[i].isupper():
#             l.append(str[i].lower())
#         else:
#             l.append(str[i].upper())
#
#     print("".join(l))
# reverseStringBase("abcD")


# def max_square_in_triangle(n,a):
#     dt_tamgiac1 = 1/2*n**n
#     dt_hv = a**a
#     for x in range(1, n+1):
#         for y in range(x, n+1):
#             if x*dt_hv/2 + y*dt_hv==dt_tamgiac1:
#                 return x,y
#
# print(max_square_in_triangle(48, 4))

