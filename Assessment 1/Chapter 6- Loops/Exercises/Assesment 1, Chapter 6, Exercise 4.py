# Create a list of sandwich orders.
sandwich_orders = ['egg', 'chicken', 'veggie', 'ham']

# Create an empty list for finished sandwiches.
finished_sandwiches = []

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
