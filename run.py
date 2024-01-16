import sys
import game
def main():
    if sys.stdin.isatty():
        input("Hit enter to start the program...")
        game.menu()

if __name__ == "__main__":
    main()