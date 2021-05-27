# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc
fruits = ["apple", "banana", "cherry", "kiwi"]
for i in fruits: print(i)
[print(i) for i in fruits]
# With the break statement we can stop the loop before it has looped through all the items
for i in range(len(fruits)):
    if i==2:
        break
    print(fruits[i])
# With the continue statement we can stop the current iteration, and continue with the next
for i in range(len(fruits)):
    if i==2:
        continue
    print(fruits[i])
# The range() Function
for i in range(1, 10, 2): print(i)
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished
for i in range(len(fruits)): print(fruits[i])
else: print("Finally!")
""" (*)Note: The else block will NOT be executed if the loop is stopped by a break statement"""
for i in range(10):
    if i==5:  break
    print(i)
else: print("Finally!")
# Nested Loops
for i in range(1, 10, 3):
    for j in range(i, 10, 2): print(j*i)
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error
for i in [1, 2, 3]:
    pass