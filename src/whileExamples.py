# This program was written by Sue on 26th September
# Some examples of while loops

def whileBored():
    areYouBored = "n"
    while areYouBored == "n":
        areYouBored = input("Are you bored yet? (Enter y or n)  ")
    print("OK - I'll stop asking!")

def passwordProgIfOnly():
    password = "secret"
    userPassword = input("Enter password? ")
    if userPassword == password:
        print("That is correct. Enter the system.")
    else:
        print("That is not correct")
        
def passwordProg():
    password = "secret"
    userPassword = ""
    while userPassword != password:
        userPassword = input("Enter password? ")

        if userPassword == password:
            print("That is correct. Enter the system.")
        else:
            print("That is not correct. Try again")
        

