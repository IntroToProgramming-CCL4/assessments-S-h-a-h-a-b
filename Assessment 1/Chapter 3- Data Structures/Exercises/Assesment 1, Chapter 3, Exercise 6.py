# list of people invited to dinner in exercise 4
name = ["Tayyab", "Asad", "Mohsin", "Sudais"]

# print name of person that can not attend the dinner
print(name[0],"will not be able to attend the dinner due to an emergency.\n")

# replacing the name of the guest who can’t make it with the name of the new person you are inviting.
name.remove(name[0])
name.insert(0,"Anas")

# Send new dinner invitations
for person in name:
    print("Dear",person,"you are invited to dinner. Please join us for a wonderful evening.")

# Print a message that you can invite only two people
print("\nUnfortunately, the dinner table won't arrive in time, and we can only invite two people for dinner.\n")

# Use pop() to remove guests until only two names remain
while len(name) > 2:
    removed_person = name.pop()
    print("Sorry,",removed_person+'.',"We can't invite you to dinner this time.")

print("\n")

# Send dinner invitations to the two remaining guests
for person in name:
    print("Dear", person+',', "you are still invited to dinner. Please join us for a wonderful evening.")

# Use del to remove the last two names
del name[:]

# Print the list to ensure it's empty
print("\nThe guest list is now empty:",name)
