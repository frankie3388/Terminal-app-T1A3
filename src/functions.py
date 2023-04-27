import csv


def add_history(file_name, game, random_number):
    with open(file_name, "a") as history_file:
        record = csv.writer(history_file)
        record.writerow([game, random_number])

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