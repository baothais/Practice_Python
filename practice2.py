import re


def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def multi(a, b):
    return a*b

def div(a, b):
    return round(a/b, 2)

if __name__=="__main__":
    print("MAY TINH PYTHON".center(50, "-"))
    print("1. Cong 2 so a va b")
    print("2. Tru 2 so a va b")
    print("3. Nhan 2 so a va b")
    print("4. Chia 2 so a va b")
    print("".center(50, "-"))
    chon = int(input("Moi ban chon chuc nang: "))
    while chon!=0:

        if chon==1:
            a = int(input("Moi ban nhap a: "))
            b = int(input("Moi ban nhap b: "))
            print(f"Tong 2 so {a} va {b} la: {add(a, b)}")

        if chon==2:
            a = int(input("Moi ban nhap a: "))
            b = int(input("Moi ban nhap b: "))
            print(f"Hieu 2 so {a} va {b} la: {sub(a, b)}")

        if chon==3:
            a = int(input("Moi ban nhap a: "))
            b = int(input("Moi ban nhap b: "))
            print(f"Tich 2 so {a} va {b} la: {multi(a, b)}")

        if chon==4:
            a = int(input("Moi ban nhap a: "))
            b = int(input("Moi ban nhap b: "))
            print(f"Thuong 2 so {a} va {b} la: {div(a, b)}")

        chon = int(input("Moi ban chon chuc nang: "))

    print("THOAT CHUONG TRINH".center(50, "-"))


