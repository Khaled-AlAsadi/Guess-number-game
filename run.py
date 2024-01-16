import sys
import game

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--run-game":
        input("Hit enter to start the program...")
        game.menu()
    else:
        print("Game not started. Use '--run-game' as a command-line argument to start the game.")

if __name__ == "__main__":
    main()