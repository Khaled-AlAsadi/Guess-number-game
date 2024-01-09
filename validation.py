import os
import time
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

# Example text with color
print(Fore.RED + 'This is red text')
print(Back.GREEN + 'This has a green background')
print(Style.BRIGHT + 'This is bright text')
print(Fore.CYAN + Back.YELLOW + 'Cyan text on yellow background')

def checkChoice(text):
    try:
        if int(text) < 0:
            print("Please enter a positive number.")
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
            print("Invalid input. Please enter 'yes' or 'no'.")
            time.sleep(0.1)
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')