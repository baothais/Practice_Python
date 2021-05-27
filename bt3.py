# # # 1
# # Ít nhất 1 chữ cái nằm trong [a-z]
# def check_character1(s):
#     return any(s[i].islower() for i in range(len(s)))
# # Ít nhất 1 số nằm trong [0-9]
# def check_character2(s):
#     return any(s[i].isdigit() for i in range(len(s)))
# # Ít nhất 1 kí tự nằm trong [A-Z]
# def check_character3(s):
#     return any(s[i].isupper() for i in range(len(s)))
# # Ít nhất 1 ký tự nằm trong [$ # @]
# def check_character4(s):
#     return any(s[i] in ["$", "#", "@"] for i in range(len(s)))
# # Độ dài mật khẩu tối thiểu: 6 and Độ dài mật khẩu tối đa: 12
# def check_length(s):
#     return len(s)>=6 and len(s) <= 12
# def password(s):
#     l1 = s.split(",")
#     l2 = [l1[i] for i in range(len(l1)) if check_character1(l1[i]) and check_character2(l1[i]) and check_character3(l1[i]) and check_character4(l1[i]) and check_length(l1[i])]
#     if l2==[]: return -1
#     return ",".join(l2)
#
#
# s = input("Enter s: ")
# print(password(s))

# # 2
import math
import re


def is_prime(n):
    if n < 2: return False
    return all(n%i!=0 for i in range(2, int(math.sqrt(n))+1))
#
# n = int(input())
# print(is_prime(n))

# # 3
# import math
# def is_prime(n):
#     if n < 2: return False
#     elif n > 2 and n % 2 == 0:
#         return False
#     return all(n%i!=0 for i in range(3, int(math.sqrt(n))+1))
#
# dem = 0
# i = 0
# n = int(input("Enter n: "))
# while dem <= n:
#     if is_prime(i):
#         print(i, end= " ")
#         dem += 1
#     i += 1

# # 4
# for i in range(10000,100000):
#     if is_prime(i):
#         print(i, end=' ')

# # 5
# n = int(input("Enter n: "))
# l = []
# for i in range(2, n+1):
#     if is_prime(i):
#         while n % i == 0:
#             l.append(str(i))
#             n /= i
# print("x".join(l))

# # 6
# n = int(input("Enter n: "))
# s = 0
# while n!=0:
#     s += n % 10
#     n //= 10
#
# print(s)

# # 7
# def check(n):
#     return str(n) == str(n)[::-1]
#
# n = int(input("Enter n: "))
# if check(n): print(f"{n} la so thuan nghich")
# else: print(f"{n} khong phai so thuan nghich")

# # 8
# def Fibonacci(n):
#     if n==0 or n==1: return n
#     return Fibonacci(n-1) + Fibonacci(n-2)
#
# n = int(input("Enter n: "))
# i = 0
# while Fibonacci(i) < n:
#     if is_prime(Fibonacci(i)):
#         print(Fibonacci(i), end=" ")
#     i += 1

# for i in range(n):
#     if is_prime(Fibonacci(i)):
#         if Fibonacci(i) < n:
#             print(Fibonacci(i), end=" ")

# # 9 - UCLN
# def UCLN(a, b):
#     l = [i for i in range(1, min(a, b)+1) if a%i==0 and b%i==0]
#     return max(l)
#
# # 10 - BCNN
# def BCNN( a, b):
#     l = [i for i in range(1, a*b+1) if i%a==0 and i%b==0]
#     return min(l)

# def tong(n):
#     if n==0 or n==1: return n
#     return n+tong(n-1)
#
# print(tong(n=2))

# # 11
# def amendTheSentence(s):
#     l1 = [i for i in range(len(s)) if s[i].isupper()]    # Lấy index của những chữ cái viết hoa trong chuỗi
#
#     l2 = []
#     if l1[0]!=0:
#         l2.append(s[0:l1[0]])               # Nếu chữ cái đầu tiên ko viết hoa thì chèn chuỗi đến chữ cái viết hoa đầu tiên
#
#     for i in range(len(l1)):
#         for j in range(i+1, len(l1)):
#             l2.append(s[l1[i]:l1[j]])       # Chèn từng chuỗi theo từng index đến index tiếp theo
#             break                           # break vì 1 index chèn 1 chuỗi
#
#     l2.append(s[max(l1):])
#     l3 = [i.lower() for i in l2]
#     return " ".join(l3)
#
# print(amendTheSentence("iEiMCyKAdsfGMPa"))

# # 12
# def truncateString(s):
#     while s!="":
#         if int(s[0])%3==0: s = s[1:]
#         elif int(s[-1]) % 3 == 0: s = s[:-1]
#         elif (int(s[0]) + int(s[-1]))%3==0: s = s[1:-1]
#         else: break                   # Nếu không thoả mãn thì thoát khỏi vòng lặp và trả về s
#     return s
#
# print(truncateString("312248"))

# # 13
# def lineEncoding(s):
#     l = []
#     for i in range(len(s)):
#         x = s[i]
#         for j in range(i+1, len(s)):
#             if s[i]==s[j]:
#                 x += s[i]
#             else:
#                 break
#         l.append(x)
#     return l
#
# print(lineEncoding("aabbbc"))



