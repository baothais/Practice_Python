import json

def add_entry(my_info):
    while True:
        name = input("Enter scientist’s name: ").title()
        birthday = input("Enter scientist’s birthday: ")
        my_info[name] = birthday
        with open("file_json/info_scientist.json", "w") as f:
            json.dump(my_info, f, indent=2)
        ask = input("Do you want to continue adding? (Y/N) ").upper()
        if ask != "Y":
            break

def search_birthday():
    while True:
        with open("file_json/info_scientist.json", "r") as f:
            data = json.load(f)
            print(data)
            break

if __name__=="__main__":
    my_info = {}
    choose = int(input("Enter your job: "))
    while choose != 0:

        if choose == 1:
            add_entry(my_info)

        if choose == 2:
            search_birthday()

        choose = int(input("Enter your job: "))
    print("exit")
