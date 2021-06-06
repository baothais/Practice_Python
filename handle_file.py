# """
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists
# """
#
# # # open file demo1.txt and read file
# # f = open("demo1.txt", "r")
# #
# # # reading the content of the file
# # print(f.read())
# #
# # # print 5 first characters
# # print(f.read(5))
# #
# # # To read a text file one line at a time
# # print(f.readline())
# #
# # # To read a list of lines in a text file
# # print(f.readlines())
# #
# # # close file
# # f.close()
#
# # file = open("demo2.txt", "w+")
# #
# # file.write("Hello Thai Bao\n")
# # file.write("What is your age?\n")
# # file.write("I love you!\n")
# # file.write("Hello")
# #
# # file.close()
# #
# # file = open("demo2.txt", "r")
# #
# # # print(file.read())
# #
# # # print(file.readline())
# #
# # # print(file.readlines())
# #
# # # for i in file:
# # #     print(i)
# #
# # s = ""
# # for i in file.readlines():
# #     s += i
# # print(s.split("\n"))
# #
# # file.close()
#
# # lines = ["Hello Thai Bao\n", "You very handsome\n", "I love you"]
# # f = open("demo3.txt", "w")
# # for line in lines:
# #     f.write(line)
# #
# # f.close()
#
# # with open("demo3.txt", "r") as f1:
# #     with open("demo2.txt", "r") as f2:
# #         for i in f1.readlines():
# #             if i in f2.readlines():
# #                 print(i)
#
#
#
# # # print(f.read())
# #
# # # print(f.readline())
# #
# # # print(f.readlines())
# # s = ""
# # for i in f.readlines():
# #     s += i
# #
# # print(s.split("\n"))
# #
# # l = s.split("\n")
# # # for i in range(len(l)):
# # #     print(l[i])
# #
# # print(l[1])
# # line = f.readline()
# # count = 0
# # while line:
# #     print(line)
# #     line = f.readline()
# # print(count)
# # print(len(f.readlines()))
#
# # for i in f.readlines():
# #     print(i)
# #
# # for i in f1.readlines():
# #     print(i)
# # import random
# #
# # list_number1 = random.sample(range(1, 10), 5)
# # list_number2 = random.sample(range(1, 1000), 7)
with open("file_txt/one.txt", "r") as f:
    print(f.read().split("\n"))
# # with open("two.txt", "r") as f:
# #     for number in list_number2:
# #         f.write(str(number))
# #     f.close()
#
# # f = open("demo2.txt", "r")
# # string = f.read()
# # print(string)
# # print(string.split("\n"))
# # f = open("demo4.txt", "w")
# # f.write("Hello")
# # f.write("What is your name?")
# # f.close()
# #
# f = open("demo4.txt", "r")
# l = f.read()
# print(type(l))
# # f.close()
# import random
#
# # with open("sowpods.txt") as f:
# #     l = f.read().split()
# #     print(l)
# # #     # l = list(f)
# # #     # print(l)
# # #     # print(f.readlines())
# #     f.close()
# #
# # print(random.choice(l).strip())
#
# # s = "asdasd\n\n\n\n\n\n\nasdasdasd\nasdasd\nasda"
# # print(s.split())
# import random
#
# def choose_random_word():
#     words=[]
#     with open('sowpods.txt', 'r') as file:
#         line = file.readline()
#         while line:
#             words.append(line.replace("\n","".strip()))
#             line = file.readline()
#     choice=words[random.randint(0,len(words)-1)]
#     return choice
#
#
#
#
#
# print("Welcome to Hangman!")
# secret_word=choose_random_word()
# dashes=list(secret_word)
# display_list=[]
# for i in dashes:
#     display_list.append("_")
# count=len(secret_word)
# guesses=0
# letter = 0
# used_list=[]
# while count != 0 and letter != "exit":
#     print(" ".join(display_list))
#     letter=input("Guess your letter: ")
#
#     if letter.upper() in used_list:
#         print("Oops! Already guessed that letter.")
#     else:
#         for i in range(0,len(secret_word)):
#             if letter.upper() == secret_word[i]:
#                 display_list[i]=letter.upper()
#                 count -= 1
#         guesses +=1
#     used_list.append(letter.upper())
#
# if letter == "exit":
#     print("Thanks!")
# else:
#     print(" ".join(display_list))
#     print("Good job! You figured that the word is "+secret_word+" after guessing %s letters!" % guesses)
#
#
# import json
#
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
#
# # convert into JSON:
# y = json.dumps(x)
#
# # the result is a JSON string:
# print(y)
# print(x)
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))
import json

# with open("states.json", "r") as f:
#   data = json.load(f)
#
# for state in data["states"]:
#   for x in state:
#     print(state[x])

# my_info = {
#   "Albert Einstein": "03/14/1879",
#   "Benjamin Franklin": "01/17/1706",
#   "Ada Lovelace": "12/10/1815",
#   'Donald Trump': '06/14/1946',
#   'Rowan Atkinson': '01/6/1955'
# }
#
# with open("info.json", "w") as f:
#   json.dump(my_info, f, indent=2, sort_keys=True)
#
# with open("info.json", "r") as f:
#   data = json.load(f)
#
# for key in data.keys():
#   print(key, data[key])

import json
# from urllib.request import urlopen
#
# with urlopen("https://jsonplaceholder.typicode.com/posts") as f:
#   source = f.read()
#   # print(source)
#
# data = json.loads(source)
# print(type(data))
# print(json.dumps(data, indent=2))

# with open("posts.json", "w") as f:
#   json.dump(data, f, indent=2)
#
# my_string = "hello a Bao dep zai"
# with open("demo5.json", "w") as f:
#   json.dump(my_string, f)
#
# with open("file_json/demo5.json", "r") as f:
#   # print(type(f))
#   data = json.load(f)
#   print(type(data))
#
# print(json.dumps(data))
# #
# # with open("demo5.txt", "w") as f:
# #   f.write(my_string)
# #
# # with open("demo5.txt", "r") as f:
# #   print(f)
# #   data = f.read()
# #   print(type(data))
#
# # my_string = """[{
# #   "name": "Thai Bao",
# #   "age": 25,
# #   "sex": "Male"
# # },
# # {"name": "Thai Tits",
# #   "age": 1,
# #   "sex": "Male"
# # }]"""
# #
# # data = json.loads(my_string)
# # print(json.dumps(data, indent=2))
# #
# # with open("demo6.json", "w") as f:
# #   json.dump(data, f, indent=2)
# #
# with open("file_json/demo6.json", "r") as f:
#   new_data = json.load(f)
#   print(type(new_data))
#
# print(json.dumps(new_data, indent=2))
#
# # my_str = "hello a Bao dep zai"
# #
# # with open("demo7.json", "w") as f:
# #   json.dump(my_str, f)
# #
# # with open("demo7.json", "r") as f:
# #   new_str = json.load(f)
# #
# # print(new_str)
#
# with open("file_txt/demo2.txt", "r") as f:
#   data = f.read()
#
# print(type(data))
# with open("file_json/demo2.json", "w") as f:
#   json.dump(data, f, indent=2)



# print(json.dumps(data, indent=2))

