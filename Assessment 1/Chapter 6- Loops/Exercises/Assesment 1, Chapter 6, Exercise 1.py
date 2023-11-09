# a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
while True:
    # Get user input for a pizza topping or the 'quit' command to finish.
    topping = input("Enter a pizza topping you want to add or type 'quit' to finish: ")
    
    # Check if the user wants to quit, print a message and break out of the loop.
    if topping == 'quit':
        print("Okay, your pizza is ready!")
        break
    
    # If a topping is entered, print a message indicating the topping will be added to the pizza.
    print("We will add", topping, "to your pizza.")