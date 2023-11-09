# List of sandwich orders with 'pastrami' appearing at least three times
sandwich_orders = ['egg', 'pastrami', 'chicken', 'pastrami', 'veggie', 'pastrami', 'ham']
# List to store finished sandwiches
finished_sandwiches = []

# Inform customers that the deli has run out of pastrami
print("Sorry, we've run out of pastrami!\n")

# Use a while loop to remove all occurrences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through each sandwich order.
while sandwich_orders:
    
    # Take the first order from the list.
    current_order = sandwich_orders.pop(0)  

    # Print a message indicating the sandwich is being made.
    print("I made your",current_order,"sandwich.")

    # Move the finished sandwich to the list of finished sandwiches.
    finished_sandwiches.append(current_order)

# Print a message listing each finished sandwich.
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
