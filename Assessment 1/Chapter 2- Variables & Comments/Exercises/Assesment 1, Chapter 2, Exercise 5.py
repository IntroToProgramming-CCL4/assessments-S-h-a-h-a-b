# Define the total budget and the price of each USB stick
budget = 50
price = 6

# Calculate the number of USB sticks she can buy
No_of_usb = budget // price

# Calculate how many pounds she will have left
money_left = budget % price

# Print the results
print("She can buy",No_of_usb,"USB sticks.")
print("She will have",money_left,"pounds left.")
