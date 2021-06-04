""" url practice: "https://pynative.com/python-basic-exercise-for-beginners/ """
import random
import re


class Practice5:

    @staticmethod
    def show_menu():
        print("PRACTICE 5 PYTHON".center(50, "="))
        print("1. Multiplication Or Sum")
        print("2. Sum Of Number")
        print("3. Print Even Index Character")
        print("4. Remove Characters")
        print("5. Is First And Last Same")
        print("6. Find Divisible")
        print("7. Count Of Sub String")
        print("8. Print Range Number")
        print("9. Reverse Number")
        print("10. Merge List")
        print("11. Extract Each Digit")
        print("12. Calculate Income Tax")
        print("0. Exit")
        print("".center(50, "="))

    def generate_string(self):
        string = input("Enter your string: ")
        return string

    def generate_number(self):
        number = int(input("Enter your number: "))
        return number

    def multiplication_or_sum(self, a, b):
        print("a = {}, b = {}".format(a, b))
        if a * b > 1000:
            return a + b
        return a * b

    def sum_number(self, number_list):
        for i in range(len(number_list) - 1):
            print(number_list[i]+number_list[i+1])

    def print_even_index_char(self, string):
        for i in range(0, len(string) - 1, 2):
            print("index = {}, character = {}".format(i, string[i]))

    def remove_chars(self, string, number):
        return string[(len(string) - number):]

    def is_first_and_last_same(self, number_list):
        return number_list[0] == number_list[-1]

    def find_divisible(self, number_list):
        for i in number_list:
            if i % 5 == 0:
                print(i)

    def count_of_sub_string(self, string):
        return "Emma appeared {} times".format(string.count("Emma"))

    def range_number(self, number):
        for i in range(1, number + 1):
            print(str(i) * i)

    def reverse_number(self, number):
        # return int("".join([i for i in str(number)])[::-1]) == number
        return int(str(number)[::-1]) == number

    def merge_list(self, list1, list2):
        mergeList = []
        mergeList.extend(filter(lambda x: x % 2 != 0, list1))
        mergeList.extend(filter(lambda x: x % 2 == 0, list2))
        # for i in list1:
        #     if i % 2 != 0:
        #         mergeList.append(i)
        # for i in list2:
        #     if i % 2 == 0:
        #         mergeList.append(i)
        return mergeList

    def extract_digit(self, number):
        return " ".join(re.findall("[0-9]", str(number)[::-1]))

    def income_tax(self, income):
        if income <= 10000:
            return 0
        elif income > 10000 and income <= 20000:
            return (income - 10000) * 0.1
        else:
            return 10000 * 0.1 + (income - 20000) * 0.2


if __name__=="__main__":
    p = Practice5()
    p.show_menu()
    choose = int(input("Enter your choose: "))
    while choose != 0:
        if choose == 1:
            a, b = random.sample(range(1, 100), 2)
            print("result is {}".format(p.multiplication_or_sum(a, b)))

        if choose == 2:
            number_list = random.sample(range(1, 100), 10)
            print("Printing current and next number sum in a range:")
            p.sum_number(number_list)

        if choose == 3:
            string = p.generate_string()
            print("Orginal String is {}".format(string))
            print("Printing only even index chars:")
            p.print_even_index_char(string)

        if choose == 4:
            string = p.generate_string()
            number = p.generate_number()
            print("Removing number of chars:")
            print(p.remove_chars(string, number))

        if choose == 5:
            number_list = [0, 20, 30, 40, 10]
            print("Given list is {}".format(number_list))
            print("result is {}".format(p.is_first_and_last_same(number_list)))

        if choose == 6:
            number_list = random.sample(range(1, 100), 15)
            print("Given list is {}".format(number_list))
            print("Divisible of 5 in a list:")
            p.find_divisible(number_list)

        if choose == 7:
            string = p.generate_string()
            print(p.count_of_sub_string(string))

        if choose == 8:
            number = p.generate_number()
            print("Print the following pattern:")
            p.range_number(number)

        if choose == 9:
            number = p.generate_number()
            print("original number is {}".format(number))
            if p.reverse_number(number):
                print("The original and reverse number is the same")
            else:
                print("The original and reverse number is the not same")

        if choose == 10:
            list1 = random.sample(range(1, 100), 12)
            list2 = random.sample(range(1, 100), 15)
            print("list1 = {}\nlist2 = {}".format(list1, list2))
            print("result list is {}".format(p.merge_list(list1, list2)))

        if choose == 11:
            number = p.generate_number()
            print("Given number", number)
            print("result is {}".format(p.extract_digit(number)))

        if choose == 12:
            money = int(input("Enter your income: "))
            print("Your income is {}$".format(money))
            print("Your income tax is {}$".format(p.income_tax(money)))

        choose = int(input("\nEnter your choose: "))
    print("EXIT PROGRAM".center(50, "="))
