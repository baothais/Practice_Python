# Inheritance allows us to define a class that inherits all the methods and properties from another class

# Create a Parent Class
class Person(object):
    def __init__(self, lastname, firstname, age):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
    def printPerson(self, sex):
        return f"Your name's {self.firstname} {self.lastname}\nYour age's {self.age}\nYour sex's {sex}\n"

p = Person(lastname="Bao", firstname="Thai", age=25)
print("=> Information Parent Class:")
print(p.printPerson(sex="Male"))

# Create a Child Class
class Student(Person):
    def printStudent(self, myclass, school):
        return f"Your school's {school}\nYour class's {myclass}\n"

s = Student(lastname="Y", firstname="Huynh Nhu", age=20)
print("=> Information Child Class:")
print(s.printPerson(sex="Female"))
print(s.printStudent(myclass="K23TPM6", school="Duy Tan University"))

# Add the __init__() Function
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
class Student(Person):
    def __init__(self, lastname, firstname, age):
        Person.__init__(self, lastname, firstname, age)

s = Student(lastname="Y", firstname="Huynh Nhu", age=20)
print("=> Information Child Class:")
print(s.printPerson(sex="Female"))

# Use the super() Function
# super() function that will make the child class inherit all the methods and properties from its parent
class Child(Person):
    def __init__(self, lastname, firstname, age):
        super().__init__(lastname, firstname, age)

c = Child(lastname="Tits", firstname="Thai", age=0)
print("=> Information Child Class:")
print(c.printPerson(sex="Male"))

# Add Properties into Child Class
class Me(Person):
    def __init__(self, lastname, firstname, age):
        super().__init__(lastname, firstname, age)
        self.graduationyear = 2021

m = Me(lastname="Bao", firstname="Thai", age=25)
print(m.graduationyear)

class Me(Person):
    def __init__(self, lastname, firstname, age, graduationyear):
        super().__init__(lastname, firstname, age)
        self.graduationyear = graduationyear
    def printPerson(self, sex):
        return f"Your name's {self.firstname} {self.lastname}\nYour age's {self.age}\nYour sex's {sex}\nYour graduationyear's {self.graduationyear}\n"

m = Me(lastname="Bao", firstname="Thai", age=25, graduationyear=2021)
print(m.printPerson(sex="Male"))

# Add Methods into Child Class
class Student(Person):
    def __init__(self, lastname, firstname, age, graduationyear):
        super().__init__(lastname, firstname, age)
        self.graduationyear = graduationyear
    def welcome(self):
        return f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}"

s = Student(lastname="Bao", firstname="Thai", age=25, graduationyear=2021)
print(s.welcome())