# Create modules
# def greeting(name):
#   print("Hello, " + name)
#
# person = {
#   "lastname": "Bao",
#   "firstname": "Thai",
#   "age": 25
# }
#
# x = str()
#
# print(type(x))
import re
def entry_sms():
  sms = input("Enter your string: ")
  return sms

def handle_sms(sms):
  # print(re.findall("[0-9]", sms))
  return "".join(re.findall("[0-9]", sms))

def get_OTP(*file_name):
  with open("myOTP.txt", "w") as f:
    if file_name == (sms,):
      return handle_sms(sms)
    else:
      f.write(handle_sms(sms))
      return handle_sms(sms)

if __name__=="__main__":
  print("1. return OTP, k lưu file")
  print("2. return OTP và lưu vào file")
  print("0. Exit")
  choose = int(input("Enter your choose: "))
  while choose != 0:

    # nếu người dùng gọi get_OTP(sms) => return OTP, k lưu file
    if choose == 1:
      sms = entry_sms()
      print(get_OTP(sms))
    # nếu người dùng gọi get_OTP(sms, "myOTP.txt") => return OTP và lưu vào file
    if choose == 2:
      sms = entry_sms()
      print(get_OTP(sms, "myOTP.txt"))

    choose = int(input("Enter your choose: "))
  print("Exit")


