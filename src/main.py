from data import data_set
# import random
from functions import add_history, view_history, funds, play, display_result


# print(data_set[1]["color"])

# Create the file that holds the history of results from each game
file_name = "history.csv"

try:
    history_file = open(file_name, "r")
    history_file.close()
    print("In try block")

except FileNotFoundError as e:
    history_file = open(file_name, "w")
    history_file.write("Number, Colour, Even/Odd\n")
    history_file.close()
    print("In except block")

# Global variables
bet = 0
what_you_bet_on = []
# total_funds = 0
finished_betting = ""
random_number = 0
game = 0
color = ""
even_odd = ""
play_roulette = ""


# print(funds())
# print(total_funds)

print(f"This is a game of Roulette where you can bet on even number, odd number, black, red, and/or individual numbers from 0 to 36 inclusive")
print(f"")

def nav_menu():
    print("1. Enter 1 to play Roulette")
    print("2. Enter 2 to view history of results")
    print("3. Enter 3 to exit the App")
    user_choice = input("Enter your selection: ")
    return user_choice

user_selection = ""

while user_selection != "3":
    user_selection = nav_menu()

    if user_selection == "1":
        # Had to reset the total funds to 0
        total_funds = 0
        total_funds = funds(total_funds)
        # print(total_funds)
        play(what_you_bet_on, bet, file_name, color, even_odd, play_roulette, random_number, total_funds)
        # print(color, even_odd, random_number)
        
    elif user_selection == "2":
        view_history(file_name)
    elif user_selection == "3":
        continue
    else:
        print("Invalid Input")

print("Thanks for playing Roulette")



