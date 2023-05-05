# Francis Lam's Terminal Application - Roulette (T1A3)

## R4 - Link to GitHub Repository
- [GitHub repo](https://github.com/frankie3388/Terminal-app-T1A3.git)

## R5 - Style Guide
I used the PEP8 style guide to structure or style my code. It can be seen in the code that each line does not exceed 79 characters, which is the standard for PEP8 (Rossum, Warsaw & Coghlan 2001). Indentation has been implemented on the the function below, the parameters were indented by 4 spaces to distinguish it from the rest of the function, which is the standard for PEP8:-
```
def win_lose(
        what_you_bet_on, random_number, next_bet, total_funds, color, even_odd):  
    # This function displays if the user has won and how much
    # they have won.
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
```
Other lines of code that exceeded 79 characters were indented and aligned with the opening delimiter(Rossum, Warsaw & Coghlan 2001). Also, added in block comments inside the function to describe the features of each function, which is good practice in PEP8.  


## R6 - Develop a list of features that will be included in the application  
There are a total of six features in this application. These are:-
- Terminal Menu (Navigation menu) - This 




# Reference List
- Rossum, G, Warsaw, B, Coghlan, N 2001, *PEP 8 – Style Guide for Python Code*, viewed 5 May 2023, https://peps.python.org/pep-0008/