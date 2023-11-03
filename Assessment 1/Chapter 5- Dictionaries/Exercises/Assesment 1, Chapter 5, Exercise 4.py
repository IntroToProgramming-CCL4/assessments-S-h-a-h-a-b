# Create a dictionary of rivers and the countries they run through
rivers = {'Nile': 'Egypt','Amazon': 'Brazil','Indus': 'Pakistan'}

# Print a sentence about each river
for key, value in rivers.items():
    print("The",key,"runs through",value+".")

# Print the name of each river
print("\nRivers:")
for key in rivers.keys():
    print(key)

# Print the name of each country
print("\nCountries:")
for value in rivers.values():
    print(value)