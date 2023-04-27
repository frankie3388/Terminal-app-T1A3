from data import data_set
import random
from functions import add_history, view_history, funds

# print(data_set[1]["color"])

# Create the file that holds the history of results from each game
file_name = "history.csv"

try:
    history_file = open(file_name, "r")
    history_file.close()
    print("In try block")

except FileNotFoundError as e:
    history_file = open(file_name, "w")
    history_file.write("Game,Result\n")
    history_file.close()
    print("In except block")

# Global variables
bet = 0
what_you_bet_on = []
total_funds = 0
finished_betting = ""
random_number = 0
game = 0
    

# print(funds())
# print(total_funds)

print(f"This is a game of Roulette where you can bet on even number, odd number, black, red, and/or individual numbers from 0 to 36 inclusive")
print(f"")

def nav_menu():
    print("1. Enter 1 to play Roulette")
    print("2. Enter 2 to view history of results")
    print("3. Enter 3 to exit the App")
    user_choice = input("Enter you selection: ")
    return user_choice

user_selection = ""

while user_selection != "3":
    user_selection = nav_menu()

    if user_selection == "1":
        funds(total_funds)
        input("Enter: ")
    elif user_selection == "2":
        view_history(file_name)
    elif user_selection == "3":
        continue
    else:
        print("Invalid Input")

print("Thanks for playing Roulette")

# while play_roulette != "yes":
# while finished_betting != "yes":
#     what_you_bet_on.append(input("Enter what you would like to bet on (Must be either 'even', 'odd', 'black', 'red', or any number between 0 and 36 inclusive): "))
#     bet += int(input(f"Enter how much you want to bet on for \"{what_you_bet_on}\": "))
#     finished_betting = input("Enter 'yes' to start game or 'no' to continue placing bets: ")
#     if finished_betting == "yes":
#         game += 1
#         random_number = random.randint(0, 36)
#         print(f"The number landed on is {random_number}")
#         add_history(file_name, game, random_number)
#         # play_roulette = input("Do you wish to exit game? (yes/no): ")
# print(what_you_bet_on)
# print(bet)


