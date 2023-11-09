# a function called make_shirt() in which shirts are large by default with a message that reads I love Python.
def make_shirt(size="large", message="I love Python"):
    # Prints a sentence summarizing the size and message of a shirt.
    print("Making a", size+"-sized shirt with the message:",message+".")

# Call the function to make a large shirt with the default message
make_shirt()

# Call the function to make a medium shirt with the default message
make_shirt(size="medium")

# Call the function to make a shirt of any size with a different message
make_shirt(size="small", message="Hellooo")
