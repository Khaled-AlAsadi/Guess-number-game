import os
import time
from colorama import Fore, Back, Style

def checkChoice(text):
    try:
        if int(text) < 0:
            print(Fore.WHITE + Back.RED + "Please enter a positive number.")
            return False
        elif int(text) > 2:
            return False
        else:
            return True
    except ValueError:
        print("Please enter a valid number.")
        return False

def check_input():
    while True:
        answer = input("Do you want to proceed to the next level? (yes/no): ").lower()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print(Fore.RED + "Invalid input. Please enter 'yes' or 'no'.")
            time.sleep(0.1)
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')