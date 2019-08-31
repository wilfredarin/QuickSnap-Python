# All the constants/literals will be stored in env_variables
from configs import env_variables
from user_profile.login import Login
# JSON library will be used to parse json responses
import json
import database_actions
import getpass


def snap_main():
    print("@@@Welcome to QuickSnap@@@")
    choice = int(input("Enter 1: Login\nEnter 2: Sign-up\n"))
    if choice == 1:
        counter = 0
        while (counter < env_variables.MAX_LOGIN_RETRY_LIMIT):
            counter += 1
            if (counter == env_variables.MAX_LOGIN_RETRY_LIMIT):
                print("You Fraud")
            else:
                try:
                    username = input("Enter your username: ")
                    password = getpass.getpass()
                    print(username + "\n" + password)
                    Login.validate_user(username, password)
                except Exception as err:
                    print(err)
    elif choice == 2:
        print("Signup")
    else:
        print("Invalid Input")
            
            
snap_main()