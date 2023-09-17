# © Rayyan Hodges, TAFE NSW, Gelos Enterprises 2022
# rayyan.hodges@studytafensw.edu.au
# This program is coded in Python and designed to provide a simple login system with the ability to append to accounts and a simple menu.


import time

# Defining User Credentials within a Database
user_list = {
"fredsmart1":"12345678",
"jrobertson4":"r@=%8(_W=1",
"bob101":"1234598",
"popeyedd" : "1989eidjce",
"junkman00": "p3*(kd8&ld",
"sbj2021" : "$d5e(ep2(d",
"robotman" : "7777Spy007",
"bob101":"1234598",
}

active = True
while active == True:
#Main menu which provides options to register a new account or use an existing one to sign in.
    print("Welcome to Gelos Enterprises.")
    menu_prompt=input("You have reached the main menu, please select from the following options: \n 'A' to login using existing credentials \n 'B' to create new credentials. \n ADMIN ONLY: Type C to list out the user database \n Please make a selection: \n ")


    if menu_prompt == 'A' or menu_prompt == 'a':
        # Grabbing user credentials for an existing user
        Username = input("Please enter your username: \n")
        Password = input("Please enter your password: \n")


        key_list = list(user_list.keys())

        for key in key_list:
            if Username == key and Password == user_list[key]:
                print("User details confirmed, opening files.")
                active = False
                

    # Registering new user credentials and appending them to the user list.
    elif menu_prompt == 'B' or menu_prompt == 'b':
        newuser = input("Please enter the new employee's username: \n ")
        newpass = input("Please enter the new user's password: \n")
        user_list[newuser] = newpass
        print("User credentials added, please login with the new credentials to access the document.")
        print("Returning to main menu.")


# Displaying list of user logins (presuming an admin is using this program.)

    if menu_prompt == 'C' or menu_prompt == 'c':
        print("Loading user credential list:")
        print(user_list)
        print("Returning to main menu.")



time.sleep(2)

 
