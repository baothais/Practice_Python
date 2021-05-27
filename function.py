# In Python a function is defined using the def keyword
def myfunc(name):
    print("Hello", name)
myfunc("Thai Bao")
# Arguments
def myfunc(name, age): print("Hello {}. Your age is {}".format(name, age))
myfunc("Thai Bao", 25)
# If the number of arguments is unknown, add a * before the parameter name, *args sẽ phải đặt ở cuối cùng nếu không sẽ gặp lỗi ngay
def myfunc(age, *name): print("Hello {}, your age is {}".format(name[2], age))
myfunc(25, "Nhu Y", "Thai Tits", "Thai Bao")
# You can also send arguments with the key = value syntax
def myfunc(name, age): print("Hello {}, your age is {}".format(name, age))
myfunc(age=25, name="Thai Bao")
# *args => Thay thế cho 1 đối số. Kiểu data của args là tuple()
def myfunction(*name):
    for i in range(len(name)): print(name[i])
myfunction(1, 2, 3 ,4 ,5)
# The phrase Keyword Arguments are often shortened to kwargs in Python documentations (**kwargs) => Thay thế cho nhiều đối số. Kiểu data của kwargs là dict()
def myfunc(**kwargs):
    for x, y in kwargs.items(): print(x, y)
myfunc(brand= "Ford", model= "Everest", price= "50,000$")
# Default Parameter Value
def myfunc(name="Thai Bao"): print("Hello", name)
myfunc()
myfunc("Nhu Y")
myfunc("Thai Tits")
# Passing a List as an Argument
def myfunc(food):
    for i in range(len(food)): print("It's", food[i])
fruits = ["apple", "banana", "kiwi"]
myfunc(fruits)
# NOT unpack
def myfunc(*food):
    for i in range(len(food)): print("It's", food[i])
fruits = ["apple", "banana", "kiwi"]
myfunc(fruits)
# unpack
def myfunc(*food):
    for i in range(len(food)): print("It's", food[i])
fruits = ["apple", "banana", "kiwi"]
myfunc(*fruits)                        # Nếu không để * thì coi như food = (["apple", "banana", "kiwi"],). len(food) = 1
food = (["apple", "banana", "kiwi"],)  # Có 1 giá trị là list của fruits
# To let a function return a value, use the return statement
def myfunc(name, age):
    return f"Hello {name}, your age is {age}"
print(myfunc(name="Thai Bao", age=25))
# The pass Statement
def myfunc():
    pass
# Recursion
def tri_recursion(k):
  if k < 0:
        return 0
  return k+tri_recursion(k-1)
print("\n\nRecursion Example Results:",tri_recursion(6))



