import os
import time
from colorama import Fore, Back, Style


def checkChoice(text):
    try:
        if int(text) < 0:
            print(
                Fore.WHITE
                + Back.RED
                + "Please enter a positive number."
                + Style.RESET_ALL
            )
            return False
        elif int(text) > 2:
            return False
        else:
            return True
    except ValueError:
        print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)
        return False


def check_input():
    while True:
        answer = input(
            "Do you want to proceed to the next level? (yes/no): \n").lower()
        if answer == "yes":
            print(Style.RESET_ALL)
            return True
        elif answer == "no":
            print(Style.RESET_ALL)
            return False
        else:
            print(Fore.RED + "Invalid input. Please enter 'yes' or 'no'.")
            print(Style.RESET_ALL)
            time.sleep(0.1)


def check_name(name):
    if len(name.strip()) == 0:
        print(Fore.RED + "Please enter a valid name" + Style.RESET_ALL)
        return True
    else:
        return False


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
