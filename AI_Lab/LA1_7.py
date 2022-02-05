import re

pwd = input("Enter the Password: ")

flag = 0
while True:
    if not re.search("[a-z]", pwd):
        flag = -1
        print("Invalid password")
        print("Enter at least 1 lowercase alphabet\n")
        break
    elif not re.search("[A-Z]", pwd):
        flag = -1
        print("Invalid password")
        print("Enter at least 1 uppercase alphabet\n")
        break
    elif not re.search("[0-9]", pwd):
        flag = -1
        print("Invalid password")
        print("Enter at least 1 number\n")
        break
    elif not re.search("[$#@]", pwd):
        flag = -1
        print("Invalid password")
        print("Enter at least 1 special character\n")
        break
    elif len(pwd) < 6:
        flag = -1
        print("Invalid password")
        print("Enter length between 6-16\n")
        break
    elif len(pwd) > 16:
        flag = -1
        print("Invalid password")
        print("Enter length between 6-16\n")
        break
    else:
        flag = 0
        print("Valid Password")
        break
