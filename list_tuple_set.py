"""list"""
# l = [1, 2, 3, 4, 5]
# # l.insert(2, ["2", 2])
# # print(l)
# l[1:3]=[1, 12, 32, 123, 43, 23]
# print(l)
# l.remove(1)
# print(l)
# l.pop(5)
# print(l)
# del l[2]
# print(l)
# # del l
# l.clear()
# print(l)
# for i in l:
#     print(i)
# for i in range(len(l)):
#     print(l[i:len(l)])
# i=0
# while i<len(l):
#     print(l[i])
#     i+=1
# [print(i, i+1, sep=" ") for i in l]
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# fruit = fruits * 2
# print(fruit)
# fruits[1:4] = [1, 3]
# print(fruits)
# # a = "apple"
# # [print(i) for i in fruits if a in fruits]
# # fruit = [i if a in fruits else a=="apple" for i in fruits]
# fruits.sort(reverse=False)
# print(fruits)
# fruits.sort(reverse=True)
# print(fruits)
# # fruit = fruits
# fruit = fruits.copy()
# # fruit = list(fruits)
# print(fruit)
# for i in fruits:
#     fruit.append(i)
# print(fruit[0:len(fruit)])
# n = int(input("Enter n: "))
# lst = [int(input("Enter i: ")) for i in range(n)]
# lst.sort()
# # print(lst)
# name = "Bao"
# age = 25
# print("Hello "+name)
# import math
# print(math.pi)
"""tuple"""
# t = (1, 2, 3, "4", "5")
# print(type(t))
# print(t[1])
# t = tuple((i for i in range(10)))
# print(t)
"""set"""
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.add(1)
# print(thisset)
# thisset.update(tropical)                                    # Join Two Sets, NOT create new set
# print(thisset)
# thisset.update([1, 2])
# print(thisset)
# thisset.remove(1)
# print(thisset)
# thisset.discard(3)     # If the item to remove does not exist, discard() will NOT raise an error.
# print(thisset)
# thisset.pop()          # you do not know which item that gets removed.
# print(thisset)
# # thisset.clear()
# # del thisset
# print(thisset)
# both_set_1 = thisset.union(tropical)                         # Join Two Sets, BUT create new set
# print(both_set_1)
# thisset.intersection_update(tropical)                        # Keep ONLY the Duplicates, NOT create new set
# print(thisset)
# both_set_2 = thisset.intersection(tropical)                  # Keep ONLY the Duplicates, BUT create new set
# print(both_set_2)
# both_set_2.symmetric_difference_update(both_set_1)           # Keep All, But NOT the Duplicates and NOT create new set
# print(both_set_2)
# both_set_3 = both_set_2.symmetric_difference(both_set_1)     # Keep All, But NOT the Duplicates and BUT create new set
# print(both_set_3)
# from itertools import chain, combinations
# def maxSumOfBeautifulSubarray(arr):
#     return chain.from_iterable(combinations(arr, n) for n in range(len(arr)+1))
# l1 = [sum(i) for i in list(maxSumOfBeautifulSubarray([13,3,13,12,1,8]))]
# l2 = [i for i in l1 if i%9==0]
# if l2==[]:
#     print(-1)
# else:
#     print(max(l2))

# m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# [print("{}: {}".format(k, v)) for k, v in m.items()]
# def maxSumOfBeautifulSubarray(arr):
#     s = 0
#     print(type(s))
#     l1=[]
#     for i in range(len(arr)):
#
#
#     print(l1)
#     l2 = [i for i in l1 if i%9==0]
#     if l2==[]:
#         return -1
#     return max(l2)
# print(maxSumOfBeautifulSubarray(arr=[13,3,13,12,1,8]))
# [print(type(i)) for i in [13,3,13,12,1,8]]
