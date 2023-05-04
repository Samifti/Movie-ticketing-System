import os
import sys
import main_Page
def menue():
        user=input("Are you already a user? ")

        if user == "Yes" or user == "yes":
             Login()
        elif user =="No" or user =="no":
             Register()
def log():
       pass 
        
def Register():
            print("Hello! You need to register an account before you can begin")
            username = input("Please enter a username: ")
            password = input("Now please enter a password: ")
            file = open("Login.txt","a")
            file.write (username)
            file.write (",")
            file.write (password)
            file.write("\n")
            file.close()
            print ("Your login details have been saved. ")
            print("You will now need to login")
            Login() 
def Login():
    print("Please enter your details to log in")
    username1 = input("Please enter your username: ")
    password1 = input("Please enter your password: ")

    file = open("Login.txt","r")
    for row in file:
        field = row.split(",")
        username = field[0]
        password = field[1]
        lastchar = len(password)-1
        password = password[0:lastchar]
        if username1 == username and password1 == password:
            print("Hello",username)
            main_Page.city()
            log ()
            break
        else:
            print("incorrect")

