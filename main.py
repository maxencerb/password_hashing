from encrypt_password import save_to_database, check_password
import os

def register_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    save_to_database(username, password)
    print("User successfully registered")

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if check_password(username, password):
        print("You are successfully logged in")
    else:
        print("Wrong password")

def main():
    while True:
        # Print separate lines
        print("\n==============================\n")
        # print in blue
        print("\033[1;34mWelcome to Password Locker \033[0m")
        # print("Welcome to Password Locker")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        option = input("Enter option: ")
        if option == "1":
            register_user()
        elif option == "2":
            login_user()
        elif option == "3":
            break
        else:
            print("Wrong option")

if __name__ == "__main__":
    main()