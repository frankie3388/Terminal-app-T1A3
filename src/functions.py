import csv
import random
from data import data_set

# bet = 0
# what_you_bet_on = []
# total_funds = 0
# finished_betting = ""
# random_number = 0
# game = 0
# color = ""
# even_odd = ""
# play_roulette = ""

def add_history(file_name, color, even_odd, random_number):
    with open(file_name, "a") as history_file:
        record = csv.writer(history_file)
        record.writerow([random_number, color, even_odd])

def view_history(file_name):
    with open(file_name, "r") as history_file:
        record = csv.reader(history_file)
        
        for row in record:
            print(row)

def funds(total_funds):
    # total_funds = int(input("Enter funds to start off with - a maximum of $500 can be entered: "))
    # total_funds
    while total_funds == 0:
        try:
            total_funds = int(input("Enter funds to start off with - a maximum of $500 can be entered: "))
            if total_funds > 500:
                total_funds = 0
                print("Please enter amount less than or equal to 500")
            elif total_funds < 0:
                total_funds = 0
                print("Please enter amount greater than 0")
            else:
                return total_funds
        except ValueError:
            print("Please type in numbers only")


def play(what_you_bet_on, bet, file_name, color, even_odd, play_roulette, random_number, total_funds):
    while play_roulette != "yes":
        what_you_bet_on.append(input("Enter what you would like to bet on (Must be either 'even', 'odd', 'black', 'red', or any number between 0 and 36 inclusive): "))
        next_bet = betting(bet, what_you_bet_on, total_funds)
        total_funds -= next_bet
        print(f"funds {total_funds}")
        bet += next_bet
        finished_betting = input("Enter 'yes' to start game or 'no' to continue placing bets: ")
        if finished_betting == "yes":
            display_result(data_set, random_number, color, even_odd, file_name)
            play_roulette = input("Do you wish to exit game? (yes/no): ")
            if play_roulette == "no":
                what_you_bet_on = []
    

def display_result(data_set, random_number, color, even_odd, file_name):
    random_number = random.randint(0, 36)
    for data in data_set:
        if data["number"] == random_number:
            color = data["color"]
            even_odd = data["even_odd"]
            print(f"The number landed on is {random_number} {color} {even_odd}")
            add_history(file_name, color, even_odd, random_number)
            break

def betting(bet, what_you_bet_on, total_funds):
    while True:
        try:
            bet = int(input(f"Enter how much you want to bet on for \"{what_you_bet_on}\": "))
            if bet > total_funds:
                bet = 0
                print(f"Your bet has exceeded the total funds, please enter a bet lower than {total_funds}")
            elif bet < 5:
                bet = 0
                print("Minimum bet is $5, please enter a bet $5 or higher")
            else:
                return bet
        except ValueError:
            print("Please type in numbers only")
