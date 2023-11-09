# a loop in which you ask users their age, and then tell them the cost of their movie ticket.
while True:
    # Ask the user for their age.
    age = int(input("Enter your age or enter '0' if you dont want any tickets: "))

    # Check if the user wants to exit.
    if age == 0:
        print("You have opted not to buy any tickets.")
        break

    # Determine the ticket cost based on the age.
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15

    # Print the ticket cost.
    print("Your ticket costs",cost,"dollars.")