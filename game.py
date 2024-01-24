import os
import time
import gspread
from random import randint
from tabulate import tabulate
import validation
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Guess-Number-Game")
Blad1 = SHEET.worksheet("Blad1")

choice = ""
level = 1
max_number = 100
name = ""
score = 0
credits = 100


def rules():
    """
    Function that displays the rules of the game
    """
    validation.clear_console()
    print(
        f"""
Rule 1 : The player guess the number\n
Rule 2 : On each level the max number increaases\n
Rule 3 : On level completion the player gets 50 points\n
Rule 5: Each wrong guess costs 20 credits\n
Rule 6: if the player is out of credits the player loses
        """
    )
    while True:
        choice = input("Return to menu by typing 0 and press enter\n")

        if validation.checkRulesChoice(choice):
            validation.clear_console()
            menu()
            break
        else:
            print(Fore.RED + "Please enter a valid choice" + Style.RESET_ALL)


def menu():
    """
    Main Menu function that runs first
    """
    print(Fore.WHITE + "1. Start Game\n" "2. Rules\n" "3. Leaderboard")
    choice = input(Style.NORMAL +
                   """
Please choose an option from the menu and type
the number of the choice and press enter\n
                   """
                   )
    while not validation.checkChoice(choice):
        choice = input(
            Fore.RED +
            """
Please choose a valid option from the menu and type
the number of the choice\n
1. Start Game
2. Rules
3. Leaderboard
            """
            + Style.RESET_ALL
        )
    if int(choice) == 1:
        validation.clear_console()
        start_game(level, max_number)
    if int(choice) == 2:
        rules()
    if int(choice) == 3:
        results()


def results():
    """
    Function that shows the leaderboard
    """
    validation.clear_console()
    data_range = Blad1.get_all_values()
    print(Style.NORMAL +
          "If you don't see your score then you did not get a high enogh score"
          )
    headers = data_range[0]
    data = data_range[1:]
    table = tabulate(data, headers=headers, tablefmt="fancy_grid")
    print(table)
    while True:
        choice = input("Return to menu by typing 0 and press enter\n")
        if validation.checkRulesChoice(choice):
            validation.clear_console()
            menu()
            break
        else:
            print(Fore.RED + "Please enter a valid choice" + Style.RESET_ALL)


def start_game(level, max_number):
    """
    Function that handles the game logic and saving to spreadsheet
    """
    global score
    global name
    global credits
    name = (
        input(Fore.WHITE + f"Please type your name and press enter\n")
        if level == 1
        else name
    )

    while validation.check_name(name):
        name = (
            input(Fore.WHITE + "Please type your name and press enter\n")
            if level == 1
            else name
        )
    validation.clear_console()
    print("Level:", level)
    print("Score:", score)
    print("Credits:", credits)
    random_number = randint(1, max_number)
    print("Guess a number between 1 and " + str(max_number))
    guess = input("Enter your guess:\n ")
    while random_number != guess and credits > 0:
        if not guess.isdigit():
            print(f"Please enter a valid number between 1 and {max_number}.")
            guess = input("Enter your guess:\n ")
        elif int(guess) > max_number:
            print(f"Please enter a valid number between 1 and {max_number}.")
            guess = input("Enter your guess:\n ")
        elif int(guess) < random_number:
            print("low number")
            credits -= 20
            guess = (
                int(input("Enter your guess again:\n "))
                if int(credits) > 0
                else print(
                    Fore.RED
                    + f"Unfortunately, you are out of credits"
                    + Style.RESET_ALL
                )
            )
            input("Press Enter to return to menu.") if credits == 0 else None
            validation.clear_console() if credits == 0 else None
            menu() if credits == 0 else None
        elif int(guess) > random_number:
            print("Too high number")
            credits -= 20
            guess = (
                int(input("Enter your guess again:\n "))
                if int(credits) > 0
                else print(
                    Fore.RED
                    + f"Unfortunately, you are out of credits"
                    + Style.RESET_ALL
                )
            )
            input("Press Enter to return to menu.") if credits == 0 else None
            validation.clear_console() if credits == 0 else None
            menu() if credits == 0 else None
    print(
        Fore.GREEN
        + "Congrats you guessed the number. The number is "
        + str(random_number)
        + Style.RESET_ALL
    )
    if random_number == guess:
        score += 50

    if validation.check_input():
        print(Style.RESET_ALL)
        max_number += 5
        print(max_number)
        level += 1
        credits += 100
        start_game(level, max_number)
        print(max_number)
    else:
        credits += 100
        print("processing...")
        NEW_DATA = [name, level, score, credits]
        Blad1.append_row(NEW_DATA)
        data_range = Blad1.get_all_values()
        header = data_range[0]
        data = data_range[1:]
        data.sort(key=lambda x: int(x[2]), reverse=True)
        top_10_data = data[:10]
        Blad1.clear()
        Blad1.append_row(header)
        print("Saving results...")
        for row, index in enumerate(top_10_data):
            Blad1.append_row(index)
            if row == 9:
                print("Results are saved...")
                time.sleep(1.0)
                validation.clear_console()
                return
        print("Results are saved...")
        time.sleep(5.0)
        validation.clear_console()
        menu()


menu()
