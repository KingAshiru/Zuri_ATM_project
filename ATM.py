from datetime import datetime
from Database import database_user
from Complaint import complaint_log
import random
now = datetime.now()
curBal = 0

def login():
    name = input("What is your name? \n")
    password = input("Please enter your password. \n")
    if name in database_user and database_user[name] == password:
        print("Welcome " + name)
        print("Today's date is ")
        print(now.date())
        print("Time is")
        print(now.time())
        return True
    else:
        print("Your name and password does not match, please try again")
        return False

def validPassword(check):
    if len(check) >= 8:
        return True
    return False

def register():
    name = input("What is your name? \n")
    print("Hello " + name)
    password = input("please enter a password of at least 8 characters \n")
    while not validPassword(password):
        print("Your password is not up to 8 characters")
        register()
    database_user[name] = password
    print("Would your like to generate an account number now?")
    create_acc_no = input("Enter 1 for YES or any other character for NO \n")
    if create_acc_no == '1':
        acc_no = ""
        while len(acc_no) < 11:
            n = random.randint(0,9)
            acc_no += str(n)
        print("Your account number is " + acc_no)
    else:
        print("Thank you for your time")
        exit()

def bankOperations():
    print("What would you like to do today?")
    print("1- Make Withdrawals")
    print("2- Make Deposits")
    print("3- Lodge a complaint")
    print("4- Logout")
    userOption = input("You can select from the options above.\n")
    if userOption == '1':
        amount = int(input("How much would you like to withdraw? \n"))
        print("Please take your cash #" + str(amount))
    elif userOption == '2':
        amount = int(input("How much would you like to deposit? \n"))
        curBal = curBal + amount
        print("Your current balance is #" + str(curBal))
    elif userOption == '3':
        complaint = (input("What issue would you like to report? \n"))
        complaint_log.append(complaint)
        print("Thank you for contacting us")
    elif userOption == '4':
        exit()
    else:
        print("You have entered an invalid input, enter option 1, 2 or 3")

def main():
    print("Welcome, what would you like to do?")
    print("1. Login")
    print("2. Register")

    action = int(input("Select an option \n"))

    if action == 1:
        successfulLogin = False

        while not successfulLogin:
            successfulLogin = login()

        bankOperations()

    elif action == 2:
        register()  

    else:
        print('You need to either login or register')

main()