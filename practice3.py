import collections
import datetime
import random

class Practise3:

    def showMenu(self):
        print("PRACTISE PYTHON".center(50, "="))
        print("1. Character Input")
        print("2. Odd Or Even")
        print("3. List Less Than Ten")
        print("4. Divisors")
        print("5. List Overlap")
        print("6. Palindrome")
        print("7. List Comprehensions")
        print("8. Rock Paper Scissors")
        print("9. Guessing Game One")
        print("10. List Overlap Comprehensions")
        print("11. List Remove Duplicates")
        print("12. Cows And Bulls")
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

    # 7
    def listComprehensions(self, a):
        return " ".join(list([str(i) for i in a if i%2==0]))

    # 8
    def RockPaperScissors(self, my_choose):
        items = ["rock", "paper", "scissors"]
        computer_choose = random.choice(items)
        while True:
            if my_choose == computer_choose:
                print(f"My choose: {my_choose}")
                print(f"Computer choose: {computer_choose}")
                print("==> You draw")
            else:
                if my_choose == "rock":
                    if computer_choose == "paper":
                        print(f"My choose: {my_choose}")
                        print(f"Computer choose: {computer_choose}")
                        print("==> You lose")
                    else:
                        print(f"My choose: {my_choose}")
                        print(f"Computer choose: {computer_choose}")
                        print("==> You win")
                elif my_choose == "scissors":
                    if computer_choose == "rock" :
                        print(f"My choose: {my_choose}")
                        print(f"Computer choose: {computer_choose}")
                        print("==> You lose")
                    else:
                        print(f"My choose: {my_choose}")
                        print(f"Computer choose: {computer_choose}")
                        print("==> You win")
                else:
                    if computer_choose == "rock":
                        print(f"My choose: {my_choose}")
                        print(f"Computer choose: {computer_choose}")
                        print("==> You lose")
                    else:
                        print(f"My choose: {my_choose}")
                        print(f"Computer choose: {computer_choose}")
                        print("==> You win")

            computer_choose = random.choice(items)
            print()
            accept = input("You want to start a new game? (Y/N): ")
            print()
            if accept.lower() != "y":
                break
            else:
                my_choose = input("What is your choose? ").lower()

    # 9
    def GuessingGameOne(self, my_number):
        com_number = random.randint(1, 9)
        if my_number == com_number:
            return "You guessed exactly!"
        while my_number != com_number:
            if my_number < com_number:
                print("You guessed to low")
            else:
                print("You guessed to high")

            my_number = int(input("Enter your number: "))
            if my_number == com_number:
                return "You guessed exactly!"

    # 10
    def ListOverlapComprehensions(self, a, b):
        return " ".join(list(dict.fromkeys([str(i) for i in a if i in b])))

    # 11
    def ListRemoveDuplicates(self, my_list):
        return list(dict.fromkeys(my_list))

    # 12
    def CowsAndBulls(self, my_number):
        count = 0                       # count the number of guesses
        com_number = random.randint(1000, 9999)
        print(com_number)
        com_str = str(com_number)       # convert com_number => str

        while True:
            # if my number = computer number => you guessed correct
            if my_number == com_number:
                return "You guessed the correct number with {} times".format(count + 1)
            else:
                my_str = str(my_number)  # convert my_number => str
                count_Cows = 0  # count cows
                count_Bulls = 0  # count bulls
                for i in range(len(my_str)):
                    if my_str[i] == com_str[i]:
                        count_Cows += 1
                    else:
                        count_Bulls += 1
                count += 1
                print("{} cows, {} bulls".format(count_Cows, count_Bulls))
                if count == 6:
                    return "You guessed 6 times"
            my_number = int(input("Enter your number: "))

if __name__=="__main__":
    p = Practise3()
    p.showMenu()
    choose = int(input("Please choose a job: "))
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

        if choose==7:
            print("List Comprehensions".center(40, "-"))
            a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
            print(p.listComprehensions(a))

        if choose==8:
            print("Rock Paper Scissors".center(40, "-"))
            my_choose = input("What is your choose? ").lower()
            p.RockPaperScissors(my_choose)

        if choose==9:
            print("Guessing Game One".center(40, "-"))
            my_number = int(input("Enter your number: "))
            print(p.GuessingGameOne(my_number))

        if choose==10:
            print("List Overlap Comprehensions".center(40, "-"))
            # a = range(1, 10)                                 # Create a list containing values from 1 to 9
            a = random.sample(range(1, 30), 12)                # https://www.w3schools.com/python/ref_random_sample.asp
            b = [i for i in range(1, random.randint(1, 100))]
            print("==> Your result: ", end="")
            print(p.ListOverlapComprehensions(a, b))

        if choose==11:
            print("List Remove Duplicates".center(40, "-"))
            # my_list = random.sample(range(1, 30), 10)
            my_list = [1, 1, 2, 3, 5, 5, 8, 13, 13, 21, 34, 34, 55, 89]
            print("My list: {}".format(my_list))
            print("List Remove Duplicates: {}".format(p.ListRemoveDuplicates(my_list)))

        if choose==12:
            print("Cows And Bulls".center(40, "-"))
            my_number = int(input("Enter your number: "))
            print(p.CowsAndBulls(my_number))

        choose = int(input("\nPlease choose a job: "))
        print()
    print("EXIT PROGRAM".center(50, "="))