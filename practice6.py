import math
import random


class Practice6:

    @staticmethod
    def show_menu():
        print("PRACTICE PYTHON".center(50, "="))
        print("1. Hello World")
        print("2. Fahreneit To Celsius")
        print("3. Sum Of Squares")
        print("4. Total Cost")
        print("5. Max Of Two Number")
        print("6. Max Of Four Number")
        print("7. Check Triangle")
        print("8. first degree equation".title())
        print("9. quadratic".title())
        print("10. greatest common divisor".title())
        print("11. least common multiple".title())
        print("12. separate digit".title())
        print("13. convert hex".title())
        print("14. convert binary".title())
        print("15. find Armstrong number".title())
        print("16. factorial".title())
        print("0. Exit")
        print("".center(50, "="))

    def hello_world(self):
        return "Hello World"

    def fahreneit_to_celsius(self, f):
        c = (5 * (f - 32)) / 9
        return "Celsius is {}oC".format(round(c, 2))

    def sum_of_squares(self, a, b):
        return a**2 + b**2

    def total_cost(self, n):
        if n < 1:
            return False
        return 1/n + self.total_cost(n-1)

    def max_of_two_number(self, a, b):
        if a > b:
            return a
        return b

    def max_of_four_number(self, a, b, c, d):
        # if a > b:
        #     if a > c:
        #         if a > d:
        #             return a
        #         else:
        #             return d
        #     else:
        #         if c > d:
        #             return c
        #         else:
        #             return d
        # elif b > c:
        #     if b > c:
        #         return b
        #     else:
        #         if c > d:
        #             return c
        #         else:
        #             return d
        # elif c > d:
        #     return c
        # else:
        #     return d
        return self.max_of_two_number(self.max_of_two_number(a, b), self.max_of_two_number(c, d))

    def check_triangle(self, a, b, c):
        if a + b > c and b + c > a and a + c > b:
            return True
        return False

    def first_degree_equation(self, a, b):
        if a == 0:
            if b == 0:
                return "Wealth of counter"
            else:
                return "No solution"
        return round(-b / a, 2)

    def quadratic(self, a, b, c):
        if a == 0:
            return self.first_degree_equation(b, c)
        else:
            delta = b ** 2 - 4 * a * c
            if delta < 0:
                return "No solution"
            elif delta == 0:
                return round(-b / (2 * a), 2)
            else:
                return round((-b + math.sqrt(delta)) / (2 * a), 2), round((-b + math.sqrt(delta) / (2 * a)), 2)

    def greatest_common_divisor(self, a, b):
        max = 1
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0 and max < i:
                max = i
        return max

    def least_common_multiple(self, a, b):
        min = a * b
        for i in range(max(a, b), a * b + 1):
            if i % a == 0 and i % b == 0 and min > i:
                min = i
        return min

    def separate_digit(self, number):
        list_digit = []
        while number != 0:
            list_digit.append(number % 10)
            number //= 10
        return " ".join(list(map(str, list_digit[::-1])))

    def convert_hex(self, number):
        hex = ""
        while number != 0:
            a = number % 16
            number = number // 16
            if a == 10:
                hex += "A"
            elif a == 11:
                hex += "B"
            elif a == 12:
                hex += "C"
            elif a == 13:
                hex += "D"
            elif a == 14:
                hex += "E"
            elif a == 15:
                hex += "F"
            else:
                hex += str(a)
        return hex[::-1]

    def convert_binary(self, number):
        binary = ""
        while number != 0:
            a = number % 2
            number = number // 2
            binary += str(a)
        return binary[::-1]

    def find_Armstrong_number(self, number):
        copy_number = number
        x = len(str(number))
        sum = 0
        while number != 0:
            a = number % 10
            number = number // 10
            sum += a**x
        return sum == copy_number

    def factorial(self, number):
        product = 1
        if number == 0:
            return product
        while number != 0:
            product *= number
            number -= 1
        return product


if __name__=="__main__":
    p = Practice6()
    p.show_menu()
    choose = int(input("Enter your choose: "))
    print()
    while choose != 0:
        if choose == 1:
            print("Hello World".center(40, "-"))
            print("result = {}".format(p.hello_world()))

        if choose == 2:
            print("Fahreneit To Celsius".center(40, "-"))
            f = float(input("Enter fahreneit: "))
            print("result = ".format(p.fahreneit_to_celsius(f)))

        if choose == 3:
            print("Sum Of Squares".center(40, "-"))
            a, b = random.sample(range(1, 10), 2)
            print("Given a = {}, b = {}".format(a, b))
            print("result = {}".format(p.sum_of_squares(a, b)))

        if choose == 4:
            print("Total cost".center(40, "-"))
            n = random.randint(5, 10)
            print("Given n = {}".format(n))
            print("result = {}".format(round(p.total_cost(n), 2)))

        if choose == 5:
            print("Max Of Two Number".center(40, "-"))
            a, b = random.sample(range(50), 2)
            print("Given a = {}, b = {}".format(a, b))
            print("result = {}".format(p.max_of_two_number(a, b)))

        if choose == 6:
            print("Max Of Four Numbers".center(40, "-"))
            a, b, c, d = random.sample(range(50), 4)
            print("Given a = {}, b = {}, c = {}, d = {}".format(a, b, c, d))
            print("result = {}".format(p.max_of_four_number(a, b, c, d)))

        if choose == 7:
            print("Check Triangle".center(40, "-"))
            a, b, c = random.sample(range(20), 3)
            print("Given a = {}, b = {}, c = {}".format(a, b, c))
            print("result = {}".format(p.check_triangle(a, b, c)))

        if choose == 8:
            print("first degree equation".title().center(40, "-"))
            a, b = random.sample(range(-10, 10), 2)
            print("Given a = {}, b = {}".format(a, b))
            print("result = {}".format(p.first_degree_equation(a, b)))

        if choose == 9:
            print("quadratic".title().center(40, "-"))
            a, b, c = random.sample(range(-20, 20), 3)
            print("Given a = {}, b = {}, c = {}".format(a, b, c))
            print("result = {}".format(p.quadratic(a, b, c)))

        if choose == 10:
            print("greatest common divisor".title().center(40, "-"))
            a, b = random.sample(range(50), 2)
            print("Given a = {}, b = {}".format(a, b))
            print("result = {}".format(p.greatest_common_divisor(a, b)))

        if choose == 11:
            print("least common multiple".title().center(40, "-"))
            a, b = random.sample(range(1, 20), 2)
            print("Given a = {}, b = {}".format(a, b))
            print("result = {}".format(p.least_common_multiple(a, b)))

        if choose == 12:
            print("separate digit".title().center(40, "-"))
            numbers = random.randint(100, 999)
            print("Given number = {}".format(numbers))
            print("result = {}".format(p.separate_digit(numbers)))

        if choose == 13:
            print("convert hex".title().center(40, "-"))
            numbers = random.randint(200, 300)
            print("Given number = {}".format(numbers))
            print("result = {}".format(p.convert_hex(numbers)))

        if choose == 14:
            print("convert binary".title().center(40, "-"))
            number = random.randint(1, 50)
            print("Given number = {}".format(number))
            print("result = {}".format(p.convert_binary(number)))

        if choose == 15:
            print("find Armstrong number".title().center(40, "-"))
            # number = random.randint(10, 1000)
            # print("Given number = {}".format(number))
            for number in range(10, 10000):
                if p.find_Armstrong_number(number):
                    print("result = {}".format(number))

        if choose == 16:
            print("factorial".title().center(40, "-"))
            number = random.randint(0, 20)
            print("Given number = {}".format(number))
            print("result = {}".format(p.factorial(number)))

        choose = int(input("\nEnter your choose: "))
        print()
    print("EXIT PROGRAM".center(50, "="))

