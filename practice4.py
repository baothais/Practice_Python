"""Link practice: https://www.practicepython.org/"""
import json
import random


class Practice4:
    @staticmethod
    def show_menu():
        print("PYTHON PROGRAM".center(50,"="))
        print("1. Read From File")
        print("2. File Overlap")
        print("3. Draw A Game Board")
        print("4. Max Of Three")
        print("5. Pick Word")
        print("6. Guess Letters")
        print("7. Hangman")
        print("8. Birthday Dictionaries")
        print("9. Birthday Json")
        print("10. Search Birthday")
        print("11. Show Birthday")
        print("12. Birthday Months")
        print("13. Birthday Plots")
        print("0. Exit")
        print("".center(50, "="))

    def read_from_file(self):
        with open("file_txt/practice4.txt", "r") as f:
            """way 1"""
            # string = ""
            # for i in f.readlines():
                # string += i
            # print("==> There are {} names in file".format(len(string.split("\n"))))
            """way 2"""
            # print("==> There are {} names in file".format(len(f.readlines())))
            """way 3"""
            print("==> There are {} names in file".format(len(f.read().split("\n"))))
            f.close()

    def file_over_lap(self):
        with open("file_txt/one.txt", "r") as f1:
            # str_number1 = ""
            # for number in f1.readlines():
            #     str_number1 += number
            # list_number1 = str_number1.split("\n")
            str_number1 = f1.read()
            list_number1 = str_number1.split("\n")
            f1.close()

        with open("file_txt/two.txt", "r") as f2:
            # str_number2 = ""
            # for number in f2.readlines():
            #     str_number2 += number
            # list_number2 = str_number2.split("\n")
            str_number2 = f2.read()
            list_number2 = str_number2.split("\n")
            f2.close()

        for number in list_number1:
            if number in list_number2:
                print(number)

    def draw_a_game_board(self, board_size):
        for _ in range(board_size):
            print(" ---" * board_size)
            print("|   " * (board_size + 1))
        print(" ---" * board_size)

    def max_of_three(self, a, b, c):
        if a > b:
            if a > c:
                return a
            else:
                return c
        elif b > c:
            return b
        else:
            return c

    def pick_word(self):
        with open("file_txt/sowpods.txt", "r") as f:
            """ way 1: create list with f.read() """
            list_str = f.read().split()                 # clean data
            """ way 2: create list with f """
            # list_str = list(f)                        # not clean data
            f.close()
        choose_str = random.choice(list_str)
        return choose_str.strip()

    def guess_letters(self, com_guess, my_guess):
        # count = 0
        while True:
            if my_guess == com_guess:
                print("==> You guessed correct!")
                print("Guess Letters".center(40, "-"))
                break
            else:
                for i in range(len(com_guess)):
                    if my_guess == com_guess[i]:
                        print(my_guess, end='')
                    else:
                        print('-', end='')
                print()
                # count += 1
                # if count == 6:
                #     return "You guessed 6 times!"
            my_guess = input("Enter your guess: ").upper()

    def hangman(self, com_guess, my_guess):
        count = 0
        while True:
            if my_guess == com_guess:
                count = 0
                print("==> You guessed correct!")
                ask = input("==> You want to start a new game? (Y/N): ").upper()
                if ask != "Y":
                    print("Hangman".center(40, "-"))
                    break
            else:
                for i in range(len(com_guess)):
                    if my_guess == com_guess[i]:
                        print(my_guess, end='')
                    else:
                        print("-", end='')
                print()
                count += 1
                if 6 - count != 0:
                    print("==> You have {} guesses left".format(6-count))
                if count == 6:
                    count = 0
                    print("==> You guessed 6 times!")
                    ask = input("==> You want to start a new game? (Y/N): ").upper()
                    if ask != "Y":
                        print("Hangman".center(40, "-"))
                        break
            my_guess = input("\nEnter your guess: ").upper()

    def birthday_dictionaries(self, my_info):
        while True:
            print("Welcome to the birthday dictionary. We know the birthdays of:")
            for name in my_info.keys():
                print(name)
            name = input("Who's birthday do you want to look up? ").title()
            print("{}'s birthday is {}".format(name, my_info[name]))
            ask = input("Do you want to continue searching? (Y/N) ").upper()
            if ask != "Y":
                break

    def birthday_json(self, my_info):
        while True:
            name = input("Enter scientist’s name: ").title()
            birthday = input("Enter scientist’s birthday: ")
            my_info[name] = birthday
            with open("file_json/info_scientist.json", "w") as f:
                json.dump(my_info, f, indent=2)
            ask = input("\nDo you want to continue program? (Y/N) ").upper()
            if ask != "Y":
                break

    def search_birthday(self):
        while True:
            with open("file_json/info_scientist.json", "r") as f:
                date = json.load(f)
            name = input("Who's birthday do you want to look up? ").title()
            if name in date.keys():
                print('{}\'s birthday is {}'.format(name, date[name]))
            else:
                print("Sadly, we don\'t have {}\'s birthday".format(name))
            ask = input("\nDo you want to continue searching? (Y/N) ").upper()
            if ask != "Y":
                break

    def show_birthday(self):
        with open("file_json/info_scientist.json", "r") as f:
            date = json.load(f)
        for name, birthday in date.items():
            print("{}'s birthday is {}".format(name, birthday))

    def birthday_months(self):
        with open("file_json/info_scientist.json", "r") as f:
            data = json.load(f)
        items_months = []
        for name in data.keys():
            items_birthday = data[name].split("/")          # list birthday
            items_months.append(items_birthday[0])          # list all months of birthday
        dict_months = {i: items_months.count(i) for i in items_months}
        months = {
            "1": "January",
            "2": "February",
            "3": "March",
            "4": "April",
            "5": "May",
            "6": "June",
            "7": "July",
            "8": "August",
            "9": "September",
            "10": "October",
            "11": "November",
            "12": "December"
        }
        print("The months of all the birthdays: ", end="")
        # print(" ".join(dict.fromkeys(items_months)))
        # x = dict.fromkeys(items_months)
        # print(x)
        for x in list(dict.fromkeys(items_months)):
            if x in months.keys():
                print(months[x], end=" ")
        print()
        for x in dict_months.keys():
            if x in months.keys():
                print("{} has {} scientists".format(months[x], dict_months[x]))

if __name__=="__main__":
    p = Practice4()
    p.show_menu()
    my_info = {}
    try:
        choose = int(input("Enter your job: "))
        print()
        while choose!=0:
            if choose==1:
                print("Read From File".center(40, "-"))
                list_name = ["Bao\n", "Y\n", "Tits\n", "John\n", "Russia\n", "Biden\n", "Trump\n", "Obama\n", "Book\n",
                             "Putin"]
                with open("file_txt/practice4.txt", "w") as f:
                    for name in list_name:
                        f.write(name)
                    f.close()
                p.read_from_file()

            if choose==2:
                print("File Overlap".center(40, "-"))
                list_number1 = random.sample(range(1, 50), 20)
                list_number2 = random.sample(range(1, 50), 25)
                with open("file_txt/one.txt", "w") as f:
                    for number in list_number1:
                        # f.write(str(number) + "\n")
                        f.write("{}\n".format(number))
                    f.close()
                with open("file_txt/two.txt", "w") as f:
                    for number in list_number2:
                        f.write(str(number) + "\n")
                    f.close()
                p.file_over_lap()

            if choose==3:
                print("Draw A Game Board".center(40, "-"))
                board_size = int(input("What size of game board? "))
                p.draw_a_game_board(board_size)

            if choose==4:
                print("Max Of Three".center(40, "-"))
                a, b, c = random.sample(range(1, 10), 3)
                print("a = {}\nb = {}\nc = {}".format(a, b, c))
                print("==> Max Of Three is: {}".format(p.max_of_three(a, b, c)))

            if choose==5:
                print("Pick Word".center(40, "-"))
                print("==> My choose: {}".format(p.pick_word()))

            if choose==6:
                print("Guess Letters".center(40, "-"))
                with open("file_txt/sowpods.txt", "r") as f:
                    items = f.read().split("\n")
                    f.close()
                com_guess = random.choice(items)
                my_guess = input("Enter your guess: ").upper()
                print(p.guess_letters(com_guess, my_guess))

            if choose==7:
                print("Hangman".center(40, "-"))
                with open("file_txt/sowpods.txt", "r") as f:
                    list_str = f.read().split("\n")
                    f.close()
                com_guess = random.choice(list_str)
                print("==> Computer's result: {}".format(com_guess))
                my_guess = input("Enter your guess: ").upper()
                p.hangman(com_guess, my_guess)

            if choose==8:
                print("Birthday Dictionaries".center(40, "-"))
                # my_info = dict()
                # for _ in range(3):
                #     name = input("Enter name: ")
                #     age = (input("Enter birthday: "))
                #     my_info[name] = age
                # my_info = {}
                # my_info["Albert Einstein"] = "03/14/1879"
                # my_info["Benjamin Franklin"] = "01/17/1706"
                # my_info["Ada Lovelace"] = "12/10/1815"
                my_info = {
                    "Albert Einstein": "03/14/1879",
                    "Benjamin Franklin": "01/17/1706",
                    "Ada Lovelace": "12/10/1815",
                    'Donald Trump': '06/14/1946',
                    'Rowan Atkinson': '01/6/1955'
                }
                p.birthday_dictionaries(my_info)

            if choose==9:
                print("Birthday Json".center(40, "-"))
                p.birthday_json(my_info)

            if choose==10:
                print("Search Birthday".center(40, "-"))
                p.search_birthday()

            if choose==11:
                print("Show Birthday".center(40, "-"))
                p.show_birthday()

            if choose==12:
                print("Birthday Months".center(40, "-"))
                p.birthday_months()


            try:
                print()
                print("".center(50, "="))
                choose = int(input("Enter your job: "))
                print()
            except Exception as e:
                print("Has a wrong: {}".format(e))
    except Exception as e:
        print("Has a wrong: {}".format(e))
    print("EXIT PROGRAM".center(50, "="))
