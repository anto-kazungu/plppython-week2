# Create an empty list
my_list = []

# Elements to append
elements_to_add = [10, 20, 30, 40]

# Append elements using a for loop
for element in elements_to_add:
    my_list.append(element)

# Insert the value 15 at the second position
my_list.insert(1, 15)

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from my_list
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("The index of 30 is:", index_of_30)

# Print the final list for verification
print("Final list:", my_list)