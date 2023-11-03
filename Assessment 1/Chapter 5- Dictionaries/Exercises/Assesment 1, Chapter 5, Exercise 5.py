# Create a list of dictionaries, each representing a different pet
pet1 = {"animal": "Dog", "owner": "Asad"}
pet2 = {"animal": "Tiger", "owner": "Tayyab"}
pet3 = {"animal": "Cat", "owner": "Mohsin"}
pet4 = {"animal": "Bunny", "owner": "Sudais"}

# Store these dictionaries in a list called pets.
pets = [pet1,pet2,pet3,pet4]

# Loop through the list and print information about each pet
for pet in pets:
    print("Animal:",pet["animal"]+", Owner:",pet["owner"])
