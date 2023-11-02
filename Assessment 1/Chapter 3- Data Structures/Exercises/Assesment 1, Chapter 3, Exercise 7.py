# Create a list of places to visit
places_to_visit = ["Tokyo", "Paris", "Lahore", "Sydney", "Rome"]

# Print the list in its original order
print("Original order:", places_to_visit)

# Use sorted() to print the list in alphabetical order without modifying the actual list
print("Alphabetical order:", sorted(places_to_visit))

# Print the list to show it's still in its original order
print("Original order:", places_to_visit)

# Use sorted() to print the list in reverse alphabetical order without changing the original list
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Print the list to show it's still in its original order
print("Original order:", places_to_visit)

# Use reverse() to change the order of the list
places_to_visit.reverse()
print("Reversed order:", places_to_visit)

# Use reverse() again to change the order back to the original order
places_to_visit.reverse()
print("Original order:", places_to_visit)

# Use sort() to change the list to alphabetical order
places_to_visit.sort()
print("Sorted in alphabetical order:", places_to_visit)

# Use sort() again to change the list to reverse alphabetical order
places_to_visit.sort(reverse=True)
print("Sorted in reverse alphabetical order:", places_to_visit)

