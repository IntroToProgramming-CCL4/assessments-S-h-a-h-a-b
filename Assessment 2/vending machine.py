import time
import os

# Function to display a welcome animation
def welcome_animation():
    frames = [
        r"""
 ____      ____  ________  _____       ______    ___    ____    ____  ________   
|_  _|    |_  _||_   __  ||_   _|    .' ___  | .'   `. |_   \  /   _||_   __  | 
  \ \  /\  / /    | |_ \_|  | |     / .'   \_|/  .-.  \  |   \/   |    | |_ \_| 
   \ \/  \/ /     |  _| _   | |   _ | |       | |   | |  | |\  /| |    |  _| _  
    \  /\  /     _| |__/ | _| |__/ |\ `.___.'\\  `-'  / _| |_\/_| |_  _| |__/ | 
     \/  \/     |________||________| `.____ .' `.___.' |_____||_____||________| 
        """,
        r"""
 ____      ____  ________  _____       ______    ___    ____    ____  ________   _  
|_  _|    |_  _||_   __  ||_   _|    .' ___  | .'   `. |_   \  /   _||_   __  | | |
  \ \  /\  / /    | |_ \_|  | |     / .'   \_|/  .-.  \  |   \/   |    | |_ \_| | |
   \ \/  \/ /     |  _| _   | |   _ | |       | |   | |  | |\  /| |    |  _| _  | |
    \  /\  /     _| |__/ | _| |__/ |\ `.___.'\\  `-'  / _| |_\/_| |_  _| |__/ | |_|
     \/  \/     |________||________| `.____ .' `.___.' |_____||_____||________| (_)
        """,
        r"""
 ____      ____  ________  _____       ______    ___    ____    ____  ________   _   _  
|_  _|    |_  _||_   __  ||_   _|    .' ___  | .'   `. |_   \  /   _||_   __  | | | | | 
  \ \  /\  / /    | |_ \_|  | |     / .'   \_|/  .-.  \  |   \/   |    | |_ \_| | | | | 
   \ \/  \/ /     |  _| _   | |   _ | |       | |   | |  | |\  /| |    |  _| _  | | | | 
    \  /\  /     _| |__/ | _| |__/ |\ `.___.'\\  `-'  / _| |_\/_| |_  _| |__/ | |_| |_| 
     \/  \/     |________||________| `.____ .' `.___.' |_____||_____||________| (_) (_) 
        """,
        r"""
 ____      ____  ________  _____       ______    ___    ____    ____  ________   _   _   _  
|_  _|    |_  _||_   __  ||_   _|    .' ___  | .'   `. |_   \  /   _||_   __  | | | | | | | 
  \ \  /\  / /    | |_ \_|  | |     / .'   \_|/  .-.  \  |   \/   |    | |_ \_| | | | | | | 
   \ \/  \/ /     |  _| _   | |   _ | |       | |   | |  | |\  /| |    |  _| _  | | | | | | 
    \  /\  /     _| |__/ | _| |__/ |\ `.___.'\\  `-'  / _| |_\/_| |_  _| |__/ | |_| |_| |_| 
     \/  \/     |________||________| `.____ .' `.___.' |_____||_____||________| (_) (_) (_) 
        """
    ]

    for frame in frames:
        os.system('clear' if os.name == 'posix' else 'cls')  
        print(frame)
        time.sleep(1)  

# Function for suggesting items based on the previous purchase
def suggest_purchase(previous_purchase_item):
    suggestions = {
        'Chips': [('21', 'Soda', 2.00, 8), ('23', 'Juice', 2.25, 10), ('41', 'Cookies', 1.80, 12)],
        'Popcorn': [('21', 'Soda', 2.00, 8), ('22', 'Water', 1.00, 20), ('31', 'Chocolate', 1.75, 10)],
        'Pretzels': [('21', 'Soda', 2.00, 8), ('23', 'Juice', 2.25, 10), ('41', 'Cookies', 1.80, 12)],
        'Soda': [('11', 'Chips', 1.50, 10), ('12', 'Popcorn', 1.90, 15), ('31', 'Chocolate', 1.75, 10)],
        'Water': [('12', 'Popcorn', 1.90, 15), ('23', 'Juice', 2.25, 10), ('42', 'Crackers', 1.60, 15)],
        'Juice': [('11', 'Chips', 1.50, 10), ('12', 'Popcorn', 1.90, 15), ('41', 'Cookies', 1.80, 12)],
        'Coffee': [('41', 'Cookies', 1.80, 12), ('42', 'Crackers', 1.60, 15), ('26', 'Milkshake', 2.75, 12)],
        'Tea': [('41', 'Cookies', 1.80, 12), ('42', 'Crackers', 1.60, 15), ('24', 'Coffee', 2.50, 15)],
        'Milkshake': [('24', 'Coffee', 2.50, 15), ('41', 'Cookies', 1.80, 12), ('31', 'Chocolate', 1.75, 10)],
        'Chocolate': [('12', 'Popcorn', 1.90, 15), ('21', 'Soda', 2.00, 8), ('26', 'Milkshake', 2.75, 12)],
        'Caramel': [('41', 'Cookies', 1.80, 12), ('42', 'Crackers', 1.60, 15), ('24', 'Coffee', 2.50, 15)],
        'Brownie': [('26', 'Milkshake', 2.75, 12), ('31', 'Chocolate', 1.75, 10), ('24', 'Coffee', 2.50, 15)],
        'Cookies': [('25', 'Tea', 1.75, 18), ('24', 'Coffee', 2.50, 15), ('26', 'Milkshake', 2.75, 12)],
        'Crackers': [('25', 'Tea', 1.75, 18), ('22', 'Water', 1.00, 20), ('23', 'Juice', 2.25, 10)],
    }

    return suggestions.get(previous_purchase_item, [])

# Function to display the items and their details and categories
def display_items():
    print("\n-------- Welcome to the Vending Machine! --------\n")
    print("Please select any of the following items:")

    categories = set(item['category'] for item in items.values())
    
    bold = "\033[1m"
    reset = "\033[0m"

    for category in categories:
        print(f"\n{bold}{category}:{reset}")
        for key, item in items.items():
            if item['category'] == category:
                print(f"{key}. {item['name']:15} - ${item['price']:.2f} - Stock: {item['stock']}")

# Function to insert the initial amount of money
def insert_money():
    while True:
        try:
            initial_payment = float(input("\nPlease insert money: $"))
            if initial_payment < 0:
                print("Invalid amount. Please insert a valid amount.")
                continue
            return initial_payment
        except ValueError:
            print("Please enter a valid number for the payment.")

# Function to process money, update balance and stock
def process_payment(total_payment, amount_due, selected_item):
    if total_payment >= amount_due:
        print(f"\nThe {selected_item['name']} is/are dispensed. Thank you for your purchase!")

        remaining_balance = total_payment - amount_due
        print(f"\nMoney left: ${remaining_balance:.2f}")

        selected_item['stock'] -= 1
        transaction_history.append({
            'item': selected_item['name'],
            'price': selected_item['price'],
        })

        global total_money_spent
        total_money_spent += selected_item['price']

        return remaining_balance, True
    else:
        print("\nInsufficient payment. Please insert more money or the Transaction will be canceled.")
        return total_payment, False

# Function to input more money if the current balance is insufficient
def insert_more_money(total_payment):
    while True:
        try:
            additional_payment = float(input("\nPlease insert more money: $"))
            if additional_payment < 0:
                print("Invalid amount. Please insert a valid amount.")
                continue
            return total_payment + additional_payment
        except ValueError:
            print("Please enter a valid number for the payment.")

# Function to ask user if they want to buy anything else
def buy_more_items():
    while True:
        buy_more_input = input("\nDo you want to buy anything else? (yes/no): ").lower()
        if buy_more_input in ['yes', 'no']:
            return buy_more_input == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


# Dtails of all the items in the vending machine (their code, name, category, price, and stock)
items = {
    '11': {'name': 'Chips', 'category': 'Snacks', 'price': 1.50, 'stock': 10},
    '12': {'name': 'Popcorn', 'category': 'Snacks', 'price': 1.90, 'stock': 15},
    '13': {'name': 'Pretzels', 'category': 'Snacks', 'price': 2.10, 'stock': 12},
    '21': {'name': 'Soda', 'category': 'Beverages', 'price': 2.00, 'stock': 8},
    '22': {'name': 'Water', 'category': 'Beverages', 'price': 1.00, 'stock': 20},
    '23': {'name': 'Juice', 'category': 'Beverages', 'price': 2.25, 'stock': 10},
    '24': {'name': 'Coffee', 'category': 'Beverages', 'price': 2.50, 'stock': 15},
    '25': {'name': 'Tea', 'category': 'Beverages', 'price': 1.75, 'stock': 18},
    '26': {'name': 'Milkshake', 'category': 'Beverages', 'price': 2.75, 'stock': 12},
    '31': {'name': 'Chocolate', 'category': 'Chocolates', 'price': 1.75, 'stock': 10},
    '32': {'name': 'Caramel', 'category': 'Chocolates', 'price': 1.95, 'stock': 15},
    '33': {'name': 'Brownie', 'category': 'Chocolates', 'price': 2.20, 'stock': 10},
    '41': {'name': 'Cookies', 'category': 'Biscuits', 'price': 1.80, 'stock': 12},
    '42': {'name': 'Crackers', 'category': 'Biscuits', 'price': 1.60, 'stock': 15},
}

# List to store all the items purchased bby the user
transaction_history = []

# Initialize Total money spent variable
total_money_spent = 0.0

# Call the function to display welcome animation
welcome_animation()

# Call the funtion to display items and their details
display_items()

# Initialize buy more variable to check if the user wants to buy more items
buy_more = True

# Initialize total payment variable
total_payment = insert_money()

# Initialize variable to store the last purchased item
previous_purchase_item = None


while buy_more:

    selection = input("\nEnter the code of the item you wish to purchase: ")

    # Check if the item selected or the code of the item is valid
    if selection in items:
        selected_item = items[selection]
        # Check if item is in stock
        if selected_item['stock'] > 0:
            amount_due = selected_item['price']

            # Call function to process payments
            total_payment, success = process_payment(total_payment, amount_due, selected_item)

            # If money is insufficient for the purchase
            if not success:
                while True:
                    # Ask user if they want to insert more money or cancel transaction
                    more_money_input = input("\nDo you want to insert more money? (yes/no): ").lower()
                    if more_money_input in ['yes', 'no']:
                        if more_money_input == 'yes':
                            total_payment = insert_more_money(total_payment)
                        else:
                            print("\nTransaction canceled. Returning change.")
                            buy_more = False
                        break
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
            else:
                # Store the item in variable for suggestions
                previous_purchase_item = selected_item['name']
    
                # Give suggestions to the user based on their purchse
                suggestions = suggest_purchase(previous_purchase_item)
                if suggestions:
                    print("\nYou might also like:")
                    for suggestion_code, suggestion_name, price, stock in suggestions:
                        print(f" - {suggestion_code}. {suggestion_name} - Price: ${price:.2f} - Stock: {stock}")

                # Call function to ask the user if they want to buy something else 
                buy_more = buy_more_items()
        else:
            print("\nSorry, this item is out of stock.")
    else:
        print("\nInvalid selection. Please try again.")

# Claculate total money inserted by the user
total_money_inserted = total_money_spent + total_payment

# Print Transaction History of the purchases made by the user
print("\nTransaction History:")
for transaction in transaction_history:
    print(f"{transaction['item']} - ${transaction['price']:.2f}")
    
# Print Total Money inserted by the user 
print(f"\nTotal money inserted: ${total_money_inserted:.2f}")

# Print Total Money Spent by the user
print(f"\nTotal money spent: ${total_money_spent:.2f}")


# Return change if there is any
if total_payment > 0:
    print(f"\nReturning change: ${total_payment:.2f}")
else:
    print("\nNo change to return.")
    
# Thank you message at the end 
print("\nThank you for using the vending machine.")