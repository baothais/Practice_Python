a = 20
b = 30
c = 40
if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a=b")
# One line if statement
if a==b: print("a=b")
# One line if else statement
print(a) if a < b else print(b)
# One line if else statement, with 3 conditions
print(a) if a > b else print(b) if a < b else print(a, b)
# The and keyword is a logical operator, and is used to combine conditional statements
print(c) if (a < b and a < c) else print(b) if (a > b and a > c) else print(a)
# The or keyword is a logical operator, and is used to combine conditional statements
if a < b or a > c: print(c)
# You can have if statements inside if statements, this is called nested if statements
if a < b:
    if a > c:
        print(a)
    else:
        print(b)
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
if a > b:
    pass
