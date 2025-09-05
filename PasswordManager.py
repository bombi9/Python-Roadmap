APP_PASSWORD = "RacemApp2025"

def showPasswords():
    with open('PassWords.txt', 'r') as myFile:
        for line in myFile:
            print(line.rstrip())

def AddPasswords():
    appUsed = input("Application: ")
    userName = input("User Name: ")
    passWord = input("Password: ")
    with open('PassWords.txt', 'a') as myFile:
        myFile.write(f"App: {appUsed} | user: {userName} | pass: {passWord}\n")

userPassword = input("Enter the APP password: ")

while True:
    userChoice = input("Would you like to Show Existing Passwords(S), Add New Password(A) or Quit(Q): ").strip().title()
    if userChoice in ["Show", "Show Existing Passwords", "Show Passwords", "S"]:
        showPasswords()
    elif userChoice in ["Add", "Add New Password", "Add Passwords", "A"]:
        AddPasswords()
    elif userChoice in ["Quit", "Q", "Exit"]:
        exit()
    else:
        continue