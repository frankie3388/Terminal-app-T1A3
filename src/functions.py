import csv
import random
from data import data_set
from colored import fg, bg, attr



def add_history(file_name, color, even_odd, random_number):
    with open(file_name, "a") as history_file:
        record = csv.writer(history_file)
        record.writerow([random_number, color, even_odd])

def view_history(file_name):
    with open(file_name, "r") as history_file:
        record = csv.reader(history_file)
        for row in record:
            print(row)

def funds(user_input=None):
    while True:
        if user_input is not None:
            user_input_value = user_input
        else:
            user_input_value = input("Enter funds to start off with - a minimum of $5 can be entered: ")
        try:
            total_funds = int(user_input_value)
            if total_funds < 5:
                total_funds = 0
                print("Please enter amount greater than 5")
            else:
                return total_funds
        except ValueError:
            print("Please type in numbers only")
        except Exception as e:
            print(e)


def play(what_you_bet_on, file_name, play_roulette, total_funds):
    while play_roulette != "yes":
        if total_funds >= 5:
            bet_selection(what_you_bet_on)
            next_bet = betting(what_you_bet_on, total_funds)
            total_funds -= next_bet
            print(f"remaining funds ${total_funds}")
            finished_betting = input("Enter 'yes' to start game or 'no' to continue placing bets: ")
            while finished_betting != "yes" and finished_betting != "no":
                finished_betting = input("Invalid input. Enter 'yes' to start game or 'no' to continue placing bets: ")
            if finished_betting == "yes":
                random_number, color, even_odd = display_result(data_set, file_name)
                total_funds = win_lose(what_you_bet_on, random_number, next_bet, total_funds, color, even_odd)
                play_roulette = input("Do you wish to exit game? (yes/no): ")
                while play_roulette != "yes" and play_roulette != "no":
                    play_roulette = input("Invalid input. Please enter 'yes' or 'no': ")
                if play_roulette == "no":
                    what_you_bet_on = []
                elif play_roulette == "yes":
                    break        
        else:
            finished_betting = input("You can't place anymore bets as you have less than $5 in funds. Enter \"yes\" to start game: ")
            while finished_betting != "yes" and finished_betting != "no":
                finished_betting = input("Invalid input. Enter 'yes' to start game or 'no' no to continue placing bets: ")
            if finished_betting == "yes":
                random_number, color, even_odd = display_result(data_set, file_name)
                total_funds = win_lose(what_you_bet_on, random_number, next_bet, total_funds, color, even_odd)
                play_roulette = input("Do you wish to exit game? (yes/no): ")
                while play_roulette != "yes" and play_roulette != "no":
                    play_roulette = input("Invalid input. Please enter 'yes' or no: ")
                if play_roulette == "no":
                        what_you_bet_on = []
                elif play_roulette == "yes":
                    break
    return total_funds
                
    

def display_result(data_set, file_name):
    random_number = random.randint(0, 36)
    for data in data_set:
        if data["number"] == random_number:
            color = data["color"]
            even_odd = data["even_odd"]
            if color == "red":
                print(f"The number landed on is {random_number} {fg('red')}{color}{attr('reset')} {even_odd}")
            else:
                print(f"The number landed on is {random_number} {bg('white')}{fg('black')}{color}{attr('reset')} {even_odd}")
            add_history(file_name, color, even_odd, random_number)
            return random_number, color, even_odd


def betting(what_you_bet_on, total_funds):
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
            print("Invalid bet. Please type in numbers only")
        except Exception as e:
            print(e)


def bet_selection(what_you_bet_on):
    while True:
        try:
            choose_bet = input("Enter what you would like to bet on (Must be either 'even', 'odd', 'black', 'red', or any number between 0 and 36 inclusive): ")
            if choose_bet == 'even':
                return what_you_bet_on.append(choose_bet)
            elif choose_bet == 'odd':
                return what_you_bet_on.append(choose_bet)
            elif choose_bet == 'black':
                return what_you_bet_on.append(choose_bet)
            elif choose_bet == 'red':
                return what_you_bet_on.append(choose_bet)
            for i in range(0, 37):
                if int(choose_bet) == i:
                    return what_you_bet_on.append(int(choose_bet))
            else:
                print("Invalid choice. You can only bet on 'even', 'odd', 'black', 'red', or any number between 0 and 36 inclusive")
        except ValueError:
            print("Invalid bet. Please type in 'even', 'odd', 'black', 'red', or any number between 0 and 36 inclusive")
        except Exception as e:
            print(e)

    
# Need to reset the total funds remaining after a game
def win_lose(what_you_bet_on, random_number, next_bet, total_funds, color, even_odd):  
    winnings = 0
    for element in what_you_bet_on:
        if element == random_number:
            winnings = (next_bet * 18) + next_bet
            amount_won = winnings - next_bet
            print(f"You won ${amount_won} as the number was {element}")
            total_funds += winnings
        elif element == even_odd or element == color:
            winnings = (next_bet * 2)
            total_funds += winnings
            amount_won = winnings - next_bet
            print(f"You won ${amount_won} as the number was {element}")
    print(f"Your remaining funds are ${total_funds}")        
    return total_funds
