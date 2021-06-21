# list_a = [1, 2, 3, 4, 5]
# print(list_a[100:])

# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
# list1 = extendList(1) #1
# print(list1)
# # list2 = extendList(555,[])
# # print(list2)
# list3 = extendList('Z') #3
# print(list3)

# def haha(mood="hihi"):
#     return "{}".format(mood)
#
# print(haha())

# print((10 ** 3))
# import datetime
#
# x = datetime.date(2013, 6, 1)
# # print(type(x))
# print(x.year)
# print(x.month)
writeyourcodehere = [1, 2, 3, 4, 5, 6]
first, *middle, last = writeyourcodehere
print(first, middle, last)
print(type(middle))