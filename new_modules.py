from Tutorials import mymodules, mymodules as md

# Use a Module
mymodules.greeting(name="Bao")

# Variables in Module
for i in mymodules.person.keys(): print(i)
print()
for i in mymodules.person.values(): print(i)
print()
for i, j in mymodules.person.items(): print(i, j)
print()
mymodules.person["lastname"] = "Y"
mymodules.person["firstname"] = "Huynh Nhu"
for i in mymodules.person.values(): print(i)

# Naming a Module
"""You can name the module file whatever you like, but it must have the file extension .py"""

# Re-naming a Module
"""You can create an alias when you import a module, by using the as keyword"""
md.greeting("Thai Tits")

# Using the dir() Function
"""list all the function names (or variable names) in a module"""
import math
print(dir(math))

# Import From Module
from Tutorials.mymodules import greeting
greeting(name="Thai Bao")