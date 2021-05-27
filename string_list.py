# a, b, c = 10, 20, 30
# print(a, b, c)
# print('{} {} {}'.format(a, b, c))
# d = """dsdad dasdasd
# asdasdasd
# asdas
# da
# sda
# sd
# a"""
# print(d)
# e = input("Enter e: ")
# print(e)
# f = input("Enter f: ")
# print(f)
# l = [str(i) for i in range(3)]
# print(l)
# x, y = [int(i) for i in input("Enter x,y: ").split(", ")]
# print(type(x))
# l = [1, 2, 3]
# for i in l:
#     print(i)
# # print(l[:-1])
# import random
# secret_number = random.randint(1,500)
# print("Pick a number between 1 to 500")
# while True:
#     res = int(input("Guess the number: "))
#     if res>=secret_number:
#         print("You win")
#         break
#     else:
#         print("You lose")
#         continue
# l= [str(i) for i in range(1,6)]
# print(" ".join(l))
# a = 10
# b = 5
# print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")
# a, b = input("Enter a, b: ").split()
# s = input("Enter s: ")
# print(s[::-1])
# for i in s:
#     if i.isalpha():
#         print(i, end=' ')
#
# print()
"""String"""
# a, b = input("Enter string a,b: ").split(", ")
# c = 25
# for i in a:
#     print(i)
# for x in range(len(a)):
#     print(a[x])
# print(a[:4])
# print(a[-5:])
# print(a.upper())
# print(a.lower())
# print(a.title())
# print(a.strip())
# l = a.split()
# l.sort()
# print(l)
# print(a.replace("a", "b"))
# print(a+"\n"+b+"\n")
# print(a, b, sep="\n")
# print("\n{}\n{}".format(a, b))
# d = a + b + str(c)
# print(d)
# print("Your age: {}".format(c))
# a = "Hello, And Welcome To My World!"
# print(a.capitalize())
# print(a.casefold())
# print(a.lower())
# print(a.center(5, '0'))
# l = [i for i in a if a.count(i)==1]
# print(" & ".join(l))
# a = 10
# print(a%2==0)
# def sumary(a):
#     return a%2==0
#
# if __name__=="__main__":
#     if sumary(10):
#         print("Thai Bao handsome!")
# s = {1, '2', 3, 3}
# print(s)
# print(type(s))
l1 = [1, 2, '3', '4', '3']
l2 = [2, 3, 5, 6]
l3 = list([1, 2, 4, 5, 6])
# print(l1)
# print(l1[1])
# print(l1[:3])
# print(l1[::-1])
# print(l1[-3:])
# l1.append([5, 4])
# print(l1)
# print(len(l1))
# print(l1[:len(l1)])
# print(l1+l2)
# print(l3)
# l1[1]=10
# l2[:2] = [4, 10, 20]
# print(l1)
# print(l2)
# l2[1:3]=[1]
# print(l2)
# l2.insert(4, 'Thai Bao')
# # print(l2)
t1 = (1, 2 , 3)
l1.extend(t1)
l2.append(t1)
print(l1)
print(l2)