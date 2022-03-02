# Start codebase

import time

def inputdatabase():
    # print("start inputdatabase")

def logicinput():
    print("start logicinput")

def logic():
    # print("Logic start")

def userinterface():
    # print("userinterface start")
    time.sleep(2)
    print("Welcome to DatabasePush!")
    time.sleep(1)
    print("Please select an option.")
    option1 = input("1 - Use default settings for database. 2 - Input custom settings.")
    time.sleep(2)
    if option1 == "1":
        print("Option 1 Selected")
    elif option1 == "2":
        print("Option 2 Selected")
    else:
        print("Invalid selection. Try again.")
        userinterface()
