import collections
import datetime

class Practise3:

    def showMenu(self):
        print("PRACTISE PYTHON".center(50, "="))
        print("1. Character Input")
        print("2. Odd Or Even")
        print("3. List Less Than Ten")
        print("4. Divisors")
        print("5. List Overlap")
        print("6. Palindrome")
        print("0. Exit")
        print("".center(50, "="))

    # 1
    def characterInput(self, name, age):
        n = int(input("=>Moi ban chon so lan muon in message: "))
        print()
        for _ in range(n):
            print(f"=>Your name is: {name}\Your age is: {age}")
            print(f"=>Nam ban 100 tuoi la: {datetime.datetime.now().year - age + 100}\n")

    # 2
    def odd_Or_Even(self, number):
        return number%2==0

    # 3
    def list_Less_Than_Ten(self, my_list):
        return " ".join(list([str(i) for i in my_list if i < 10]))

    # 4
    def divisors(self, number):
        return " ".join(list([str(i) for i in range(1, number+1) if number%i==0]))

    # 5
    import collections
    def list_Overlap(self, list_a, list_b):
        return " ".join(list(collections.OrderedDict.fromkeys((list([str(i) for i in list_a if i in list_b])))))

    # 6
    def palindrome(self, my_str):
        return my_str == my_str[::-1]







if __name__=="__main__":
    p = Practise3()
    p.showMenu()
    choose = int(input("==> Moi ban chon cong viec: "))
    print()
    while choose != 0:
        if choose == 1:
            print("Character Input".center(40, "-"))
            p.characterInput(name="Thai Bao", age=25)

        if choose==2:
            print("Odd Or Even".center(40, "-"))
            number = int(input("Enter number: "))
            if p.odd_Or_Even(number):
                print(f"{number} is Even")
            else:
                print(f"{number} is Odd")

        if choose==3:
            print("List Less Than Ten".center(40, "-"))
            my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
            print("List less than ten: ", end="")
            print(p.list_Less_Than_Ten(my_list))

        if choose==4:
            print("Divisors".center(40, "-"))
            number = int(input("Enter number: "))
            print("List divisors: ", end="")
            print(p.divisors(number))

        if choose==5:
            print("List Overlap".center(40, "-"))
            list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
            list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            while list_a == list_b or len(list_a) == len(list_b):
                list_a = [i for i in (input("Enter list a: ").split())]
                list_b = [i for i in (input("Enter list b: ").split())]
            print("List overlap: ",end="")
            print(p.list_Overlap(list_a, list_b))

        if choose==6:
            print("Palindrome".center(40, "-"))
            my_str = input("Enter your string: ")
            if p.palindrome(my_str):
                print("This word is a palindrome")
            else:
                print("This word is not a palindrome")

        print()
        choose = int(input("==> Moi ban chon cong viec: "))
        print()
    print("THOAT CHUONG TRINH".center(50, "="))