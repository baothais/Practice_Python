"""Dictionaries"""
"""A dictionary is a collection which is ordered*, changeable and does not allow duplicates"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["brand"] = "Vinfast"
thisdict["model"] = "Lux a 2.0"
thisdict["year"] = 2019
print(thisdict["brand"])
print(thisdict)
# Get the value of the key
print(thisdict.get("model"))
# key() will return a list of all the keys in the dictionary
print(thisdict.keys())
# add key and value in thisdict
thisdict["color"] = "Black"
print(thisdict)
print(thisdict.keys())
# values() will return a list of all the values in the dictionary
print(thisdict.values())
# The items() method will return each item in a dictionary, as tuples in a list
print(thisdict.items())
if "brand" in thisdict.keys():
    print("Yes")
# update() will update the dictionary with the items from the given argument
thisdict.update({"color": "Blue"})
print(thisdict)
# update() will be added If the item does not exist
thisdict.update({"price": "35,000$"})
print(thisdict)
# pop() method removes the item with the specified key name
thisdict.pop("year")
print(thisdict)
# popitem() method removes the last inserted item
thisdict.popitem()
print(thisdict)
# del keyword removes the item with the specified key name
del thisdict["model"]
print(thisdict)
# clear() method empties the dictionary
thisdict.clear()
print(thisdict)
# Print all key names in the dictionary, one by one
[print(x) for x in thisdict]
# Print all values in the dictionary, one by one
[print(thisdict[x]) for x in thisdict]
# Print all values in the dictionary, one by one
[print(i) for i in thisdict.values()]
# Print all key names in the dictionary, one by one
[print(i) for i in thisdict.keys()]
# Print all key and value in the dictionary
[print(x, y) for x, y in thisdict.items()]
# Make a copy of a dictionary with the copy() method
thisdict2 = thisdict.copy()
print(thisdict2)
# Make a copy of a dictionary with the dict() function
thisdict3 = dict(thisdict)
print(thisdict3)
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries
child1 = {
  "name": "Emil",
  "year": 2004
}
child2 = {
  "name": "Tobias",
  "year": 2007
}
child3 = {
  "name": "Linus",
  "year": 2011
}

myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}
print(myfamily)


