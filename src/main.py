from data import data_set
from colored import fg, attr
from functions import view_history, funds, play

# Create the file variable that holds the history of results from each game
file_name = "history.csv"

try:
    history_file = open(file_name, "r")
    history_file.close()

except FileNotFoundError as e:
    # If file has not been created, create it and apply the headings
    history_file = open(file_name, "w")
    history_file.write("Number, Colour, Even/Odd\n")
    history_file.close()

# Global variables
total_funds = 0
play_roulette = ""
user_selection = ""

# Statement of What type of game this is
print(f"This is a game of Roulette where you can bet on even number, "
      "odd number, black, red, and/or individual numbers from 0 to 36 inclusive")
print("")


def nav_menu():
    # Navigation menu function
    print(f"{fg('blue')}Menu")
    print("1. Enter 1 to play Roulette")
    print("2. Enter 2 to view history of results")
    print("3. Enter 3 to exit the App")
    user_choice = input(f"Enter your selection: {attr('reset')}")
    return user_choice

while user_selection != "3":
    user_selection = nav_menu()

    if user_selection == "1":
        # This condition allows you to play roulette, the total_funds variable
        # is reset to 0 everytime the user starts the game.
        # total_funds variable is overridden as the user plays the game.
        total_funds = 0
        what_you_bet_on = []
        total_funds = funds()
        total_funds = play(what_you_bet_on, file_name, play_roulette, total_funds)
        print(f"{fg('yellow')}You exited the game with ${total_funds}{attr('reset')}")
    elif user_selection == "2":
        view_history(file_name)
    elif user_selection == "3":
        continue
    else:
        print("Invalid Input")

print("Thanks for playing Roulette")



