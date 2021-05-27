# # 01
# l = [str(i) for i in range(2000, 3201) if i%7==0 and i%5!=0]
# print(", ".join(l))

# # 02
# def giaiThua(n):
#     if n==0:
#         return 1
#     return n*giaiThua(n-1)
# print(giaiThua(8))

# # 03
# thisdict = {i: i*i for i in range(1,int(input("Enter n: "))+1)}
# # [print(x, y) for x, y in thisdict.items()]
# print(thisdict)

# # 04
# thistuple = tuple(map(int, input("Enter serial number: ").split(", ")))
# print(thistuple)
# thistuple1 = tuple(i for i in range(10) if i%2==0)
# print(thistuple1)

# # 05
# class InputOutString:
#     def __init__(self):
#         self.str = ""
#     def getString(self):
#         self.str = input("Enter your str: ")
#     def printString(self):
#         print(f"Your str is \"{self.str}\"")
#
# i = InputOutString()
# i.getString()
# i.printString()

# # 06
# def square(n):
#     return f"Your square of value is {n**2}"
# print(square(10))

# # 07
# from math import sqrt
# def square(D, C=50, H=30):
#     # round() là hàm làm tròn
#     return round(sqrt((2*C*D)/H))
# # D = list(map(int, input("Enter D: ").split(", ")))
# D = [int(x) for x in input("Enter D: ").split(", ")]
# for i in range(len(D)): print(f"{square(D[i])}", end=", ")

# 08
# def arrays_2_dimensional(row, col):
#     arr=[]
#     for i in range(row):
#         thislist=[]
#         for j in range(col):
#             thislist.append(int(input(f"Enter arr[{i}][{j}]= ")))
#         print()
#         arr.append(thislist)
#     return arr
#
# print(arrays_2_dimensional(3, 5))

# def arrays_2_dimensional(row, col):
#     arr=[]
#     for i in range(row):
#         thislist=[]
#         for j in range(col):
#             thislist.append(i*j)
#         print()
#         arr.append(thislist)
#     return f"arrays_2_dimensional is: {arr}"
#
# print(arrays_2_dimensional(3, 5))

# arr=[]
# row = int(input("Enter row: "))
# col = int(input("Enter col: "))
# for i in range(row):
#     thislist=[]
#     for j in range(col):
#        thislist.append(i*j)
#     arr.append(thislist)
#
# print(f"arr_2_inmensional is: {arr}")

# # 09
# list_str = input("Enter your string: ").split(",")
# list_str.sort()
# print("Your string is: "+", ".join(list_str))
#
# def mystring(str):
#     list_str = str.split(",")
#     list_str.sort()
#     return "Your string is: "+(", ").join(list_str)
#
# print(mystring(str=input("Enter your string: ")))

# 10
# str = input("Enter your string: ")
# print(f"Your ordered is: {str.upper()}")
#
# def mystring(str): return f"Your ordered is: {str.upper()}"
# print(mystring(str=input("Enter your string: ")))
#
# my_string = lambda str: str.upper()
# print(my_string(str=input("Enter your string: ")))

# 11
# from math import sqrt
# def ptBac1(a, b):
#     if a==0:
#         if b==0:
#             return "pt vo so nghiem"
#         return "pt vo nghiem"
#     else:
#         return f"pt co nghiem x = {-b/a}"
#
# def ptBac2(a, b, c):
#     if a==0:
#         return ptBac1(b, c)
#     else:
#         delta = b**2 - 4*a*c
#         if delta < 0:
#             return "pt vo nghiem"
#         elif delta > 0:
#             x1 = (-b+sqrt(delta))/(2*a)
#             x2 = (-b-sqrt(delta))/(2*a)
#             return f"pt co 2 nghiem phan biet: x1 = {x1}, x2 = {x2}"
#         else: return f"pt co nghiem kep: x1 = x2 = {-b/(2*a)}"
#
# print(ptBac2(a=4, b=8, c=4))

# 12
# def convert2(n):
#     list_2=[]
#     while n != 0:
#         a = n % 2
#         n //= 2
#         list_2.append(str(a))
#     return "".join(list_2[::-1])
#
def covert16(n):
    list_16=[]
    while n != 0:
        a = n % 16
        n //= 16
        if a==10:
            list_16.append("A")
        elif a==11:
            list_16.append("B")
        elif a==12:
            list_16.append("C")
        elif a==13:
            list_16.append("D")
        elif a==14:
            list_16.append("E")
        elif a==15:
            list_16.append("F")
        else:
            list_16.append(str(a))

    return "".join(list_16[::-1])
#
n = int(input("Nhap so can chuyen: "))
# print(f"Co so 2: {convert2(n)}")
print(f"Co so 16: {covert16(n)}")

# # 13
# def Fibonacci(n):
#     if n==0 or n==1: return n
#     return Fibonacci(n-1)+Fibonacci(n-2)
#
# for i in range(10): print(Fibonacci(i))

# # 14
# def mystring(number):
#     thislist = number.split(",")
#     thistuple = tuple(thislist)
#     return f"{thislist} {thistuple}"
#
# number = input("Enter number: ")
# print(mystring(number))

# # 15
# # no func()
# my_str = input("Enter my_str: ").split(",")
# list_numbers = []
# for i in range(len(my_str)):
#     x=0
#     for j in range(len(my_str[i])):
#         x += int(my_str[i][j])*(2**(len(my_str[i])-j-1))
#     if x%5==0: list_numbers.append(my_str[i])
#
# print(",".join(list_numbers))

# # func()
# def mystring(my_str):
#     list_number = []
#     for i in range(len(my_str)):
#         x = 0
#         for j in range(len(my_str[i])):
#             x += int(my_str[i][j])*(2**(len(my_str[i])-j-1))
#         if x%5==0: list_number.append(my_str[i])
#     return ",".join(list_number)
#
# my_str = input("Enter my_str: ").split(",")
# print(mystring(my_str))
# int(1010, 2) => Hàm chuyển nhị phân sang thập phân

# 16
# no func()
# list_str = [str(i) for i in range(2000, 4001)]
# list_num = []
# for i in range(len(list_str)):
#     s=0
#     for j in range(len(list_str[i])):
#         if int(list_str[i][j])%2==0:
#             s += 1
#     if s==4: list_num.append(list_str[i])
#
# print(",".join(list_num))

# # function()
# def mystring():
#     my_str = [str(i) for i in range(2000, 5001) if all(int(str(i)[j])%2==0 for j in range(len(str(i))))]
#     return ",".join(my_str)
#
# print(mystring())

# # 17
# def mystring(my_str):
#     s1 = 0
#     s2 = 0
#     for i in my_str:
#         if i.isalpha(): s1 += 1
#         elif i.isdigit(): s2 += 1
#     return f"So chu cai trong chuoi la: {s1}\nSo chu so trong chuoi la: {s2}"
#
# print(mystring(my_str="hello world! 123"))

# # 18
# def mystring(my_str):
#     s1 = 0
#     s2 = 0
#     for i in my_str:
#         if i.islower(): s1 += 1
#         elif i.isupper(): s2 += 1
#     return f"So chu thuong trong chuoi la: {s1}\nSo chu IN HOA trong chuoi la: {s2}"
#
# print(mystring(my_str="Cafedev – Kênh Thông Tin IT"))

# # 19
# def mystring(a):
#     return f"{int(a)+int(a)*11+int(a)*111+int(a)*1111}"
#
# print(mystring(a=5))

# # 20
# def my_num(n):
#     thislist = [i for i in n.split(",") if int(i)%2!=0]
#     return ",".join(thislist)
#
# n = input("Enter n: ")
# print(my_num(n))

# thislist = list(filter(lambda x: int(x)%2!=0, input("Enter number: ").split(",")))
# print(",".join(thislist))

# # 21
# def printMoney(s,S):
#     M = s.split(" ")
#     D = 0
#     W = 0
#
#     for i in range(len(M)):
#         if M[i]=="D": D += int(M[i+1])
#         elif M[i]=="W": W += int(M[i+1])
#
#     return S+D-W
#
# S = int(input("So tien ban dau trong tai khoan: "))
# s = input("Enter s: ")
# print(f"So tien trong tai khoan: {printMoney(s, S)}$")



