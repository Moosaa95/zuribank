import random
import string
import sys

def init():
    isValidOptionSelected = False
    print("welcome to bank PHP")
    while isValidOptionSelected == False:
        haveAccount = int(input("do you have an account with us: 1 (yes) 2 (no) \n"))
        if (haveAccount == 1):
            isValidOptionSelected = True 
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            register()
        else:
            print("you have selected wrong input")
        

usernames = ["moosa", "abu", "jubril"]
password_try = ["moosa123", "abu123", "abd123"]
def login():
    print("this is the login function")
    name = input("enter username:")
    if (name in usernames):
        password  = input('your password \n')
        userId = usernames.index(name)
        for __ in range(2):
            if (password == password_try[userId]):
                return "you have successfully logged on"
            password  = input("incorrect, try again: ")
        else:
            print("locked out")
            return False

def register():
    print("this is register function")
    name = input("what is your name?")
    usernames.append(name)
    password = input("enter your password:")
    confirm_password = input("confirm your password:")
    if password == confirm_password:
        password_try.append(password)
        generateAccountNumber()
    else:
        print("password not matched")

def generateAccountNumber():
    print("account number generator")
    
    account_number = ''.join(random.choice(string.digits) for _ in range(8))
    print(f"account number generated successfully and your account number is {account_number}")

init()