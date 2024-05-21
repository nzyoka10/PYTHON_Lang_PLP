# Accept user input to create the first set of integers
input_set1 = input("Enter the elements of the first set separated by spaces: ")
set1 = set(map(int, input_set1.split()))

# Accept user input to create the second set of integers
input_set2 = input("Enter the elements of the second set separated by spaces: ")
set2 = set(map(int, input_set2.split()))

# Create a new set containing elements common to both sets
common_elements = set1.intersection(set2)

# Print the common elements
print("Common elements:", common_elements)
