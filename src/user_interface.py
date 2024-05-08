import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def welcome_message():
    print("Welcome to the Baker 3000. I can't wait to bake you a tasty treat!")

def goodbye_message():
    print("Thank you for using the Baker 3000. Have a nice day!")

def user_menu():
    clear()
    print("What would you like to do?\n \nPlease select a number from the list below\n")
    print("1. Bake a Treat!")
    print("2. View Supply Levels")
    print("3. Refill Ingredients")
    print("4. Add a Recipe")
    print("5. Clean Machine")
    print("6. View Log")
    print("7. Turn Off")


