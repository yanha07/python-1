'''Created by Yanha Loharwad.
Python program to set value in tuple.'''
# Create the tuple with 15 elements
x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

# Convert the tuple to a list
x_list = list(x)

# Set the 3rd element to 'Python'
x_list[2] = 'Python'

# Convert the list back to a tuple
x_modified = tuple(x_list)

#Print original tuple
print("Original tuple:", x)

# Print the modified tuple
print("Modified tuple:", x_modified)
