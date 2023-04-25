from data import data_set

# print(data_set[1]["color"])

bet = 0
what_you_bet_on = []
total_funds = 0
finished_betting = ""


def funds():
    # total_funds = int(input("Enter funds to start off with - a maximum of $500 can be entered: "))
    global total_funds
    while total_funds == 0:
        total_funds = int(input("Enter funds to start off with - a maximum of $500 can be entered: "))
        if total_funds > 500:
            total_funds = 0
            print("Please enter amount less than or equal to 500")
        elif total_funds < 0:
            total_funds = 0
            print("Please enter amount greater than 0")
        else:
            return total_funds
        

print(funds())
# print(total_funds)

print(f"This is a game of Roulette where you can bet on even number, odd number, black, red, and/or individual numbers from 0 to 36 inclusive")
print(f"")

while finished_betting != "yes":
    what_you_bet_on.append(input("Enter what you would like to bet on (Must be either 'even', 'odd', 'black', 'red', or any number between 0 and 36 inclusive): "))
    bet += int(input(f"Enter how much you want to bet on for \"{what_you_bet_on}\": "))
    finished_betting = input("Enter 'yes' to start game or 'no' to continue placing bets: ")

print(what_you_bet_on)
print(bet)


