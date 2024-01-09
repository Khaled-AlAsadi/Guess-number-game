from random import randint
import validation
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Guess-Number-Game')
Blad1 = SHEET.worksheet('Blad1')
data = Blad1.get_all_values()

print(data)


choice = ""
level = 1
max_number = 10
def rules():
  print(
    "Rule 1 : No\n"
    "Rule 2 : Yes\n"
  )
  global choice
  choice = input("Return to menu by typing 0 and press enter\n")
  if not validation.checkChoice(choice):
     print("please enter a valid choice")
  elif int(choice) == 0:
     menu()

def menu():
  print(
  "1. Start Game\n"
  "2. Rules"
  )
  choice = input(
    """Please choose an option from the menu and type the number of the choice and press enter\n""")  
  while not validation.checkChoice(choice):
        choice = input("Please choose a valid option from the menu and type the number of the choice\n")
  if int(choice) == 1:
     startGame(level,max_number)
  if int(choice) == 2:
     rules()

def startGame(level,max_number):
   validation.clear_console()
   print("Level:" , level) 
   random_number = randint(1, max_number)
   print("Guess a number between 1 and " + str(max_number))
   guess = int(input("Enter your guess:\n "))
   while random_number != guess:
        if guess < random_number:
            print("low number")
            guess = int(input("Enter your guess again:\n "))
        elif guess > random_number:
            print("Too high number")
            guess = int(input("Enter your guess again:\n "))
   print("Congrats you guessed the number. The number is " + str(random_number))


   if validation.check_input():
       max_number += 5
       print(max_number)
       level += 1
       startGame(level,max_number)
       print(max_number)
   else:
       validation.clear_console()
       menu()

menu()