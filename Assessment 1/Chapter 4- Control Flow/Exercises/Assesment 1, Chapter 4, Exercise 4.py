# Set the value for the variable 'age'
age = 13

# Determine the person's stage of life based on age
if age < 0:
    print("Invalid age")
elif age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
