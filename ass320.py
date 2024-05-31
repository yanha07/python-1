'''Created by Yanha Loharwad.
Python program to replace values in tuple.'''
# Define the original tuple with lists as elements
tuple1 = ([1, 2, 3], [4, 5, 6], [7, 8, 9])

# Display the original tuple
print("Original Tuple:", tuple1)

# Replace the second list with a new list
lis = [10, 11, 12]
tuple2 = tuple1[:1] + (lis,) + tuple1[2:]

# Display the modified tuple
print("Modified Tuple:", tuple2)

