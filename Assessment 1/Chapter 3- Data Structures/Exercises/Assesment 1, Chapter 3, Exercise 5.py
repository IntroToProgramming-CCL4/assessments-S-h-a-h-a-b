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
