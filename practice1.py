# show menu
def showMenu():
    print("CHUONG TRINH PYTHON".center(50, "="))
    print("1. Tinh tong 2 so")
    print("2. Kiem tra so chan hay le")
    print("3. Tong 2 so phuc")
    print("4. Tich 2 so")
    print("5. Tinh nam nhuan")
    print("6. Kiem tra nguyen am va phu am")
    print("7. Tinh lai kep")
    print("8. Tim boi chung nho nhat cua 2 so")
    print("9. Tim uoc chung lon nhat cua 2 so")
    print("10. Tinh day Fibonacci")
    print("11. Kiem tra so nguyen to")
    print("12. In n so nguyen to dau tien")
    print("13. In cac so nguyen to tu 1 den n")
    print("14. Kiem tra mat khau hop le")
    print("15. Tinh tan suat cac tu trong input")
    print("16. Ham print Yes or No")
    print("17. Ham loc so chan bang filter")
    print("18. Ham tinh các giá trị bình phương bang map()")
    print("19. Ham check ma co dung dinh dang khong")
    print("20. Tro cho dam-la-keo")
    print("21. Game \"Cows and Bulls\"")
    print("0. Thoat chuong trinh")
    print("".center(50, "="))

# tong 2 so
def tong(a, b):
    return a+b

# Kiem tra so chan hay le
def chanle(n):
    return n%2==0

# Cong 2 so phuc
def sophuc(a, b):
    return a+b

# Nhan 2 so
def tich(a, b):
    return a*b

# Tinh nam nhuan
def namnhuan(year):
    if (year%4==0 and year%100!=0) or year%400==0: return True
    return False

# Kiem tra nguyen am va phu am
import re
def check_NguyenAm_PhuAm(character):
    # return character in ["a", "i", "u", "o", "e"]
    return re.search("[a, i, u, o, e]", character)

# Tinh lai kep
def laikep(p, r, n, t):
    return round(p*((1+(r/100)/n)**(n*t)) - p, 2)

# Tim boi chung nho nhat
def BCNN(a, b):
    return min(i for i in range(max(a, b), a*b+1) if (i%a==0 and i%b==0))

# Tim uoc chung lon nhat
def UCLN(a, b):
    return max(i for i in range(1, min(a, b)) if (a%i==0 and b%i==0))

# Tinh day fibonacci
def Fibonacci(n):
    if n==0 or n==1:
        return n
    return Fibonacci(n-1) + Fibonacci(n-2)

# Kiem tra so nguyen to
import math
def isPrime(n):
    if n < 2:
        return False
    return all(n%i!=0 for i in range(2, int(math.sqrt(n)+1)))

# Tim n so nguyen to dau tien
def searchPrime1(n):
    i = 2
    list_prime = []
    while len(list_prime) < n:
        if isPrime(i):
            list_prime.append(str(i))
        i += 1
    return " ".join(list_prime)

# Tim so nguyen to tu 1 den n
def searchPrime2(n):
    list_prime = [str(i) for i in range(n) if isPrime(i)]
    return " ".join(list_prime)

# Kiem tra mat khau hop le
import re
def checkPassword(my_str):
    list_str = []
    for i in range(len(my_str)):
        if len(my_str[i]) >=6 and len(my_str[i]) <= 12:
            if re.search("[a-z]", my_str[i]):
                if re.search("[A-Z]", my_str[i]):
                    if re.search("[0-9]", my_str[i]):
                        if re.search("[$, #, @]", my_str[i]):
                            list_str.append(my_str[i])

    return ", ".join(list_str)

# Tinh tan xuat cac tu trong input
def frequency(my_str):
    my_dict = {i:my_str.count(i) for i in my_str if not i.isspace()}
    return my_dict

# Ham print Yes or No
def printString(my_str):
    if my_str in ["yes", "Yes", "YES"]:
        return "Yes"
    else:
        return "No"

# Ham loc so chan bang filter()
def filterEvenNumber(my_list):
    return " ".join(list(map(str, list(filter(lambda x: x%2==0, my_list)))))

# Ham tinh các giá trị bình phương bang map()
def mapNumber(my_list):
    return " ".join(list(map(str, list(map(lambda i: i**2, [i for i in my_list if i%2==0])))))

# Ham check ma co dung dinh dang khong
import re
def checkCode(list_code):
    for i in range(len(list_code)):
        if int(list_code[i][0]) == 0 \
                and int(list_code[i][1]) == 0 \
                and list_code[i][3] == "L" \
                and re.search("[2-5]", list_code[i][2]) \
                and re.search("[0-9]", list_code[i][4]) \
                and re.search("[0-9]", list_code[i][5]) \
                and re.search("[0-9]", list_code[i][6]) \
                and re.search("[0-9]", list_code[i][7]):
            print(f"{list_code[i]} dinh dang Dung")
        else:
            print(f"{list_code[i]} dinh dang Sai")

# Tro choi dam-la-keo
import random
def game(my_choose):
    list_choose = ["dam", "la", "keo"]
    while True:
        x = random.choice(list_choose)
        if my_choose == x:
            print(f"You select: {my_choose}")
            print(f"Computer select: {x}")
            print("You draw")
        elif my_choose == "dam":
            if x == "keo":
                print(f"You select: {my_choose}")
                print(f"Computer select: {x}")
                print("You win")
            elif x == "la":
                print(f"You select: {my_choose}")
                print(f"Computer select: {x}")
                print("You lose")
        elif my_choose == "keo":
            if x == "dam":
                print(f"You select: {my_choose}")
                print(f"Computer select: {x}")
                print("You lose")
            elif x == "la":
                print(f"You select: {my_choose}")
                print(f"Computer select: {x}")
                print("You win")
        else:
            if x == "dam":
                print(f"You select: {my_choose}")
                print(f"Computer select: {x}")
                print("You win")
            elif x == "keo":
                print(f"You select: {my_choose}")
                print(f"Computer select: {x}")
                print("You lose")

        x = input("\nBan co muon tiep tuc tro choi khong? (Y/N): ")
        if x.upper() == "Y":
            my_choose = input("Moi ban nhap lua chon cua minh (dam-la-keo): ").lower()
        else:
            break

# Game "Cows and Bulls"
import random
def Cows_and_Bulls(number, my_number):

    str_number = str(number)
    str_mynumber = str(my_number)

    count_Cows = 0
    count_Bulls = 0

    dem = 0

    if my_number == number:
        print(f"Your number is: {my_number}")
        print(f"Computer's number is: {number}")
        print(f"{count_Cows + 2} Cows, {count_Bulls} Bulls\n")
        return f"You win with {dem+1} correct guess!"
    else:
        while my_number != number:
            print(f"Your number is: {my_number}")
            # print(f"Computer's number is: {number}")

            for i in range(len(str_number)):
                if str_mynumber[i] == str_number[i]:
                    count_Cows += 1
                else:
                    count_Bulls += 1
            dem += 1
            print(f"{count_Cows} Cows, {count_Bulls} Bulls\n")

            my_number = int(input("Moi ban du doan so: "))
            str_mynumber = str(my_number)

            count_Cows = 0
            count_Bulls = 0

            if my_number == number:
                print(f"Your number is: {my_number}")
                print(f"Computer's number is: {number}")
                return f"You win with {dem+1} correct guesses!"







if __name__ == "__main__":
    showMenu()
    chon = int(input("Moi ban chon chuong trinh: "))
    while chon!=0:
        if chon == 1:
            a = int(input("Moi ban nhap so a: "))
            b = int(input("Moi ban nhap so b: "))
            print("Tong 2 so la:", tong(a, b))

        if chon==2:
            n = int(input("Moi ban nhap so n: "))
            if chanle(n):
                print(f"{n} la so chan")
            else:
                print(f"{n} la so le")

        if chon==3:
            a = complex(input("Moi ban nhap so a: "))
            b = complex(input("Moi ban nhap so b: "))
            print("Tong 2 so phuc la:", sophuc(a, b))

        if chon==4:
            a = int(input("Moi ban nhap so a: "))
            b = int(input("Moi ban nhap so b: "))
            print("Tich 2 so la:",tich(a, b))

        if chon==5:
            year = int(input("Moi ban nhap nam: "))
            if namnhuan(year):
                print(f"{year} la nam nhuan")
            else:
                print(f"{year} khong phai la nam nhuan")

        if chon==6:
            character = input("Moi ban nhap ki tu: ")
            while len(character) != 1 or (not character.isalpha()):
                character = input("Moi ban nhap lai ki tu: ")
            else:
                if check_NguyenAm_PhuAm(character):
                    print(f"{character} la nguyen am")
                else:
                    print(f"{character} la phu am")

        if chon==7:
            p = int(input("Moi ban nhap so tien can gui: "))
            r = float(input("Moi ban nhap lai xuat hang nam: "))
            n = int(input("Moi ban nhap so lan lai duoc gop: " ))
            t = int(input("Thoi gian dau tu: "))
            print(f"Lai kep sau {t} nam la: {laikep(p, r, n, t)}")

        if chon==8:
            a = int(input("Moi ban nhap so a: "))
            b = int(input("Moi ban nhap so b: "))
            print(f"BCNN cua {a} va {b} la: {BCNN(a, b)}")

        if chon==9:
            a = int(input("Moi ban nhap so a: "))
            b = int(input("Moi ban nhap so b: "))
            print(f"UCLN cua {a} va {b} la: {UCLN(a, b)}")

        if chon==10:
            n = int(input("Moi ban nhap n: "))
            print(f"Day Fibonacci {n} dau tien la: ", end='')
            for i in range(10):
                print(Fibonacci(i), end=' ')

        if chon==11:
            n = int(input("Moi ban nhap n: "))
            if isPrime(n):
                print(f"{n} la so nguyen to")
            else:
                print(f"{n} khong phai so nguyen to")

        if chon==12:
            n = int(input("Moi ban nhap n: "))
            print(f"{n} so nguyen to dau tien la: {searchPrime1(n)}")

        if chon==13:
            n = int(input("Moi ban nhap n: "))
            print(f"Cac so nguyen to tu 1 den {n} la: {searchPrime2(n)}")

        if chon==14:
            my_str = input("Moi ban nhap day password can kiem tra: ").split(",")
            print("Day password hop le la:", checkPassword(my_str))

        if chon==15:
            my_str = input("Moi ban nhap chuoi: ")
            [print(f"{x}: {y}") for x, y in frequency(my_str).items()]

        if chon==16:
            my_str = input("Moi ban nhap chuoi: ")
            print(printString(my_str))

        if chon==17:
            my_list = [i for i in range(1, 11)]
            print(filterEvenNumber(my_list))

        if chon==18:
            my_list = [i for i in range(1, 11)]
            print(mapNumber(my_list))

        if chon==19:
            # list_code = input("Nhap day ma: ").split()
            list_code = ["001L1234", "002L1234", "003L1234", "004L1234", "005L1234", "006L1234"]
            checkCode(list_code)

        if chon==20:
            my_choose = input("Moi ban nhap lua chon cua minh (dam-la-keo): ").lower()
            game(my_choose)

        if chon==21:
            number = random.randint(1000, 9999)
            my_number = int(input("\nMoi ban du doan so: "))
            while len(str(my_number)) != 4:
                my_number = int(input("\nBan phai nhap dung so co 4 chu so. Moi ban du doan so: "))
            print(Cows_and_Bulls(number, my_number))

        chon = int(input("\nMoi ban chon chuong trinh: "))

    print("THOAT CHUONG TRINH".center(50, "="))








