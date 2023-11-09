# a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
def make_shirt(size, message):
    # Prints a sentence summarizing the size and message of a shirt.
    print("Making a", size+"-sized shirt with the message:",message+".")

# Call the function using positional arguments
make_shirt("medium", "Hehehehehe")

# Call the function using keyword arguments
make_shirt(size="large", message="Helloo")
