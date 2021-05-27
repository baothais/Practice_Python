# To create a class, use the keyword class
class Person:
    x = 5

# Create Object
class Person:
    x = 5
p = Person()
print(p.x)

# The __init__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person(name="Thai Bao", age=25)
print(p.name)

# Object Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self, school):
        return f"Hello {self.name}, your age is {self.age} and your school is {school}"

p = Person(name="Thai Bao", age=25)
print(p.myfunc(school="Duy Tan University"))

# The self Parameter
class Car:
    # It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
    def __init__(loveyourself, brand, model, price):
        loveyourself.brand = brand
        loveyourself.model = model
        loveyourself.price = price
    def myfunc(loveyourself):
        return f"brand is {loveyourself.brand}, model is {loveyourself.model} and price is {loveyourself.price}"

c = Car(brand="Ford", model="Everest", price=50000)
print(c.myfunc())

# Modify Object Properties
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def myfunc(self):
        return f"brand is {self.brand}, model is {self.model}"

c = Car(brand="Vinfast", model="Lux SA_2.0")
print(c.myfunc())
c.brand = "Mecerdes"
c.model = "G63 AMG"
print(c.myfunc())

# Delete Object Properties
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c = Car(brand="Mecerdes", model="G63")
del c.model

# Delete Objects
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c = Car(brand="Mecerdes", model="G63")
print(type(c))
del c
print(c)

# The pass Statement
class Car:
    pass
